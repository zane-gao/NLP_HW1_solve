from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    append_jsonl,
    extract_json_object,
    load_config,
    read_jsonl,
    retry_completion_with_fallback,
    utc_now_iso,
)
from scripts.api_credentials import load_provider_credential


def build_few_shot(task_type: str) -> str:
    if task_type == "extraction":
        return (
            "输入：根据公告，华星科技于2026年03月03日完成1200万元融资，项目编号AX1024。\n"
            '输出：{"company":"华星科技","date":"2026-03-03","amount":"1200万元"}\n\n'
            "输入：根据公告，蓝海数据于2026年07月11日完成900万元融资，项目编号AX3401。\n"
            '输出：{"company":"蓝海数据","date":"2026-07-11","amount":"900万元"}'
        )
    return (
        "输入：文本：华星科技于2026年03月03日完成1200万元融资。\\n断言：华星科技在2026-03-03完成了1200万元融资。\n"
        '输出：{"label":"支持"}\n\n'
        "输入：文本：蓝海数据于2026年07月11日完成900万元融资。\\n断言：蓝海数据在2026-07-11完成了1000万元融资。\n"
        '输出：{"label":"不支持"}'
    )


def build_user_prompt(prompt_cfg: Dict, sample: Dict, task_instruction: Dict, output_schema: Dict) -> str:
    task_type = sample["task_type"]
    schema = json.dumps(output_schema[task_type], ensure_ascii=False)
    return prompt_cfg["user_template"].format(
        task_type=task_type,
        task_instruction=task_instruction[task_type],
        input_text=sample["input"],
        output_schema=schema,
        few_shot=build_few_shot(task_type),
    )


def parse_model_ids(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def select_models(model_cfg: Dict, stage: str, model_ids: Optional[List[str]] = None) -> List[Dict]:
    all_models = [m for m in model_cfg["models"] if m.get("enabled", True)]
    candidates = [m for m in all_models if m.get("role", "candidate") == "candidate"]
    if model_ids:
        wanted = set(model_ids)
        selected = [m for m in candidates if m["model_id"] in wanted]
        selected_ids = {m["model_id"] for m in selected}
        missing = [model_id for model_id in model_ids if model_id not in selected_ids]
        if missing:
            raise RuntimeError(f"requested model_ids are not enabled candidates: {missing}")
        return selected
    if stage == "pilot":
        pilot_ids = set(model_cfg.get("pilot_model_ids", []))
        return [m for m in candidates if m["model_id"] in pilot_ids]
    return candidates


def select_prompts(prompt_cfg: Dict, stage: str, prompt_ids: Optional[List[str]] = None) -> List[Dict]:
    configured_prompts = prompt_cfg["prompts"]
    if prompt_ids:
        wanted = set(prompt_ids)
        selected = [prompt for prompt in configured_prompts if prompt["prompt_id"] in wanted]
        selected_ids = {prompt["prompt_id"] for prompt in selected}
        missing = [prompt_id for prompt_id in prompt_ids if prompt_id not in selected_ids]
        if missing:
            raise RuntimeError(f"requested prompt_ids are not configured: {missing}")
        return selected
    stage_prompt_ids = set(prompt_cfg["pilot_prompt_ids"] if stage == "pilot" else prompt_cfg["main_prompt_ids"])
    return [prompt for prompt in configured_prompts if prompt["prompt_id"] in stage_prompt_ids]


def provider_for_model(model: Dict) -> str:
    provider = str(model.get("provider", "")).lower()
    model_id = str(model.get("model_id", "")).lower()
    api_key_env = str(model.get("api_key_env", "")).lower()
    if "siliconflow" in api_key_env or "glm" in model_id or "qwen" in model_id or "deepseek" in model_id:
        return "siliconflow"
    if "gmn" in api_key_env or model_id.startswith("gpt"):
        return "gmn"
    if "openrouter" in api_key_env or "openrouter" in provider:
        return "openrouter"
    if "newapi" in api_key_env:
        return "newapi"
    return provider or "openai_compatible"


def resolve_model_endpoint(model: Dict, api_doc: str) -> Tuple[str, str, str]:
    api_key = os.getenv(model.get("api_key_env", ""))
    api_base = str(model.get("api_base") or "").strip()
    source = f"env:{model.get('api_key_env')}" if api_key else ""
    if api_key and api_base:
        return api_key, api_base, source

    provider = provider_for_model(model)
    credential = load_provider_credential(provider, api_doc=api_doc)
    if credential:
        return api_key or credential.api_key, api_base or credential.api_base, credential.source
    return api_key, api_base, source


def load_existing_keys(path: str) -> Set[Tuple[str, str, str]]:
    rows = read_jsonl(path)
    keys: Set[Tuple[str, str, str]] = set()
    for row in rows:
        keys.add((row["qid"], row["model_id"], row["prompt_id"]))
    return keys


def main() -> None:
    parser = argparse.ArgumentParser(description="运行模型评测")
    parser.add_argument("--stage", choices=["pilot", "main"], default="main")
    parser.add_argument("--model-registry", default="configs/model_registry.yaml")
    parser.add_argument("--prompt-bank", default="configs/prompt_bank.yaml")
    parser.add_argument("--problem-bank", default="")
    parser.add_argument("--output", default="")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--max-rows", type=int, default=0, help="仅调试时使用")
    parser.add_argument("--model-ids", default="", help="Comma-separated model ids to run.")
    parser.add_argument("--prompt-ids", default="", help="Comma-separated prompt ids to run.")
    parser.add_argument("--timeout-sec", type=int, default=120)
    parser.add_argument("--sleep-ms", type=int, default=0)
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--api-doc", default="../HW1_begin/api.md", help="本地私有 API 说明文件；只读取，不写入输出。")
    parser.add_argument("--allow-responses-fallback", action="store_true", help="Chat Completions 失败后尝试 OpenAI Responses API。")
    parser.add_argument("--smoke", action="store_true", help="只执行每个模型第一条样本和第一条提示。")
    args = parser.parse_args()

    model_cfg = load_config(args.model_registry)
    prompt_cfg = load_config(args.prompt_bank)
    models = select_models(model_cfg, args.stage, model_ids=parse_model_ids(args.model_ids))
    prompts = select_prompts(prompt_cfg, args.stage, prompt_ids=parse_model_ids(args.prompt_ids))
    if not models:
        raise RuntimeError("没有可用候选模型，请检查 model_registry.yaml。")
    if not prompts:
        raise RuntimeError("没有可用提示模板，请检查 prompt_bank.yaml。")

    problem_bank = args.problem_bank or (
        "data/pilot_problem_bank.jsonl" if args.stage == "pilot" else "data/problem_bank.jsonl"
    )
    if args.output:
        output = args.output
    else:
        output = "runs/responses_pilot.jsonl" if args.stage == "pilot" else "runs/responses.jsonl"
    rows = read_jsonl(problem_bank)
    if args.max_rows > 0:
        rows = rows[: args.max_rows]
    if args.smoke:
        rows = rows[:1]
        prompts = prompts[:1]
    if not rows:
        raise RuntimeError(f"问题库为空：{problem_bank}")

    existing_keys: Set[Tuple[str, str, str]] = set()
    if args.resume and Path(output).exists():
        existing_keys = load_existing_keys(output)

    task_instruction = prompt_cfg["task_instruction"]
    output_schema = prompt_cfg["output_schema"]

    total_calls = len(rows) * len(models) * len(prompts)
    print(f"[start] stage={args.stage} rows={len(rows)} models={len(models)} prompts={len(prompts)} total_calls={total_calls}")
    done = 0

    for model in models:
        model_id = model["model_id"]
        api_key, api_base, credential_source = resolve_model_endpoint(model, args.api_doc)
        if not api_key or not api_base:
            print(f"[skip] model={model_id} 缺少可用 provider 配置或 api_base")
            continue
        for prompt in prompts:
            prompt_id = prompt["prompt_id"]
            for sample in rows:
                key = (sample["qid"], model_id, prompt_id)
                if key in existing_keys:
                    done += 1
                    continue
                user_prompt = build_user_prompt(prompt, sample, task_instruction, output_schema)
                messages = [
                    {"role": "system", "content": prompt["system_prompt"]},
                    {"role": "user", "content": user_prompt},
                ]
                ok, content, latency_ms, err, endpoint_kind = retry_completion_with_fallback(
                    api_base=api_base,
                    api_key=api_key,
                    model=model.get("api_model", model_id),
                    messages=messages,
                    temperature=float(model.get("temperature", 0.0)),
                    max_tokens=int(model.get("max_tokens", 512)),
                    stop=model.get("stop"),
                    timeout_sec=args.timeout_sec,
                    max_retries=args.max_retries,
                    retry_sleep_sec=1.5,
                    allow_responses_fallback=args.allow_responses_fallback,
                )

                parsed = extract_json_object(content) if ok else None
                row = {
                    "qid": sample["qid"],
                    "model_id": model_id,
                    "prompt_id": prompt_id,
                    "raw_output": content if ok else "",
                    "parsed_output": parsed,
                    "latency_ms": latency_ms,
                    "status": "ok" if ok else "error",
                    "error": err,
                    "endpoint_kind": endpoint_kind,
                    "credential_source": "local_private" if credential_source else "",
                    "created_at": utc_now_iso(),
                }
                append_jsonl(output, row)
                done += 1
                if done % 100 == 0 or done == total_calls:
                    print(f"[progress] {done}/{total_calls}")
                if args.sleep_ms > 0:
                    time.sleep(args.sleep_ms / 1000.0)

    print(f"[done] output={output}")


if __name__ == "__main__":
    main()
