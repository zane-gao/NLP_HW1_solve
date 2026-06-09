#!/usr/bin/env python3
from __future__ import annotations

import argparse
import base64
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import time
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import requests


ROOT = Path(__file__).resolve().parents[1]
MANUAL_DIR = ROOT / "paper" / "figures" / "manual"
LOG_ROOT = MANUAL_DIR / "logs"
SKILLS_ROOT = Path.home() / ".codex" / "skills"

SCHEMATIC_SKILL = SKILLS_ROOT / "scientific-schematics" / "scripts" / "generate_schematic_ai.py"
INFOGRAPHIC_SKILL = SKILLS_ROOT / "infographics" / "scripts" / "generate_infographic_ai.py"
IMAGE_SKILL = SKILLS_ROOT / "generate-image" / "scripts" / "generate_image.py"

IMAGE_MODEL_CANDIDATES = [
    "google/gemini-3-pro-image-preview",
    "gemini-3-pro-image-preview",
]
REVIEW_MODEL_CANDIDATES = [
    "google/gemini-3-pro",
    "gemini-3-pro-preview",
    "gemini-3-pro",
]

PROXY_ENV_KEYS = [
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
    "http_proxy",
    "https_proxy",
    "all_proxy",
]


FIGURE_SPECS: Dict[str, Dict[str, Any]] = {
    "problem_framework_ai": {
        "backend": "scientific-schematics",
        "output": MANUAL_DIR / "problem_framework_ai.png",
        "doc_type": "conference",
        "iterations": 2,
        "prompt": (
            "publication-quality scientific schematic, white background, AI conference paper style, "
            "Chinese NLP robustness study, six real input sources including announcement, customer service transcript, "
            "social media post, email memo, instant message chat, form OCR, flowing into three normalization-gap mechanisms: "
            "simplified-traditional script variation, full-width half-width character mixing, OCR confusable characters, "
            "then into five frontier representative language models, then split into structured extraction and factual classification, "
            "final panel highlights output flip and field mismatch, emphasize fact unchanged but surface form changed, "
            "clean vector layout, high contrast, colorblind-safe palette, minimal text, no decorative clutter, no prompt text"
        ),
        "negative_prompt": (
            "watermark, photorealistic, 3d, glossy gradients, dense paragraphs, layout instruction text, "
            "prompt leakage, low resolution, decorative background, unrelated icons, extra labels"
        ),
    },
    "data_pipeline_ai": {
        "backend": "scientific-schematics",
        "output": MANUAL_DIR / "data_pipeline_ai.png",
        "doc_type": "conference",
        "iterations": 2,
        "prompt": (
            "publication-quality scientific flowchart, white background, horizontal pipeline layout, "
            "Chinese NLP robustness dataset construction workflow, source templates and scenario slots, "
            "control and perturbed pairing, calibration gate for semantic preservation and parse quality, "
            "Focus3 main set, five models times four prompt templates evaluation, scoring summary layer analysis and flip analysis, "
            "clean academic schematic, vector style, subtle blue orange accents, high contrast, minimal labels, publication ready, no prompt text"
        ),
        "negative_prompt": (
            "watermark, photorealistic, 3d, cluttered background, dense paragraphs, layout instruction text, "
            "prompt leakage, low resolution, decorative arrows, unrelated charts"
        ),
    },
    "noise_landscape": {
        "backend": "infographics",
        "output": MANUAL_DIR / "noise_landscape.png",
        "doc_type": "report",
        "iterations": 3,
        "infographic_type": "comparison",
        "style": "education",
        "palette": "wong",
        "background": "white",
        "research": False,
        "prompt": (
            "publication-quality infographic, real-world Chinese noisy text landscape, six panels for announcement, customer service, "
            "social media, email memo, instant message chat, form OCR, each panel shows semantically equivalent but visually perturbed "
            "Chinese text examples, highlight simplified-traditional variants, full-width half-width mixing, OCR confusable characters, "
            "flat vector poster style, white background, clean grid layout, subtle blue orange accents, colorblind-safe palette, minimal labels"
        ),
        "negative_prompt": (
            "watermark, photorealistic, 3d, dense paragraphs, decorative icons, prompt leakage, "
            "layout instruction text, low resolution, unrelated charts"
        ),
    },
    "graphical_abstract": {
        "backend": "generate-image",
        "output": MANUAL_DIR / "graphical_abstract.png",
        "prompt": (
            "clean AI conference style graphical abstract, Chinese NLP robustness study, real noisy text from OCR chat social email form "
            "flows into five large language models, outputs structured extraction and factual classification, highlight normalization gap "
            "in simplified-traditional characters, full-width half-width numbers, OCR confusable characters, white background, vector-like "
            "flat design, high contrast, colorblind-safe palette, minimal labels, publication quality, do not include any text showing the prompt or instructions"
        ),
        "negative_prompt": (
            "watermark, photorealistic, 3d, cluttered background, dense paragraphs, decorative icons, glossy gradients, "
            "extra labels, prompt leakage, layout instruction text, low resolution"
        ),
    },
}


def normalize_api_base(api_base: str) -> str:
    base = api_base.strip().rstrip("/")
    if not base.endswith("/v1"):
        base = f"{base}/v1"
    return base


def now_str() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def ensure_paths() -> None:
    MANUAL_DIR.mkdir(parents=True, exist_ok=True)
    LOG_ROOT.mkdir(parents=True, exist_ok=True)


class ProxyBypass:
    def __init__(self) -> None:
        self._saved: Dict[str, str] = {}
        self._had_no_proxy = False
        self._no_proxy_value = ""

    def __enter__(self):
        for key in PROXY_ENV_KEYS:
            if key in os.environ:
                self._saved[key] = os.environ.pop(key)
        self._had_no_proxy = "NO_PROXY" in os.environ
        self._no_proxy_value = os.environ.get("NO_PROXY", "")
        os.environ["NO_PROXY"] = "*"
        return self

    def __exit__(self, exc_type, exc, tb):
        for key, value in self._saved.items():
            os.environ[key] = value
        if self._had_no_proxy:
            os.environ["NO_PROXY"] = self._no_proxy_value
        else:
            os.environ.pop("NO_PROXY", None)


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Failed to load module from {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pick_model(available: Iterable[str], candidates: List[str]) -> str:
    available_list = [item for item in available if item]
    available_lower = {item.lower(): item for item in available_list}
    for candidate in candidates:
        exact = available_lower.get(candidate.lower())
        if exact:
            return exact
    for candidate in candidates:
        cand_lower = candidate.lower()
        for item in available_list:
            lower = item.lower()
            if lower.endswith(cand_lower) or cand_lower.endswith(lower):
                return item
    return candidates[0]


def discover_models(api_base: str, api_key: str) -> Dict[str, Any]:
    url = f"{api_base}/models"
    result: Dict[str, Any] = {
        "api_base": api_base,
        "status": "fallback",
        "available_models": [],
        "image_model": IMAGE_MODEL_CANDIDATES[0],
        "review_model": REVIEW_MODEL_CANDIDATES[0],
        "error": None,
    }
    try:
        session = requests.Session()
        session.trust_env = False
        response = session.get(url, headers={"Authorization": f"Bearer {api_key}"}, timeout=30)
        response.raise_for_status()
        payload = response.json()
        data = payload.get("data", [])
        available = [item.get("id", "") for item in data if isinstance(item, dict)]
        result["available_models"] = available
        result["image_model"] = pick_model(available, IMAGE_MODEL_CANDIDATES)
        result["review_model"] = pick_model(available, REVIEW_MODEL_CANDIDATES)
        result["status"] = "ok"
    except Exception as exc:
        result["error"] = str(exc)
    return result


def combine_prompt(prompt: str, negative_prompt: str) -> str:
    return (
        f"{prompt}\n\n"
        "Hard constraints:\n"
        "- white background\n"
        "- publication-quality composition\n"
        "- keep labels minimal\n"
        "- do not include any text showing the prompt, instructions, metadata, layout descriptions, or style directives\n"
        f"- avoid: {negative_prompt}"
    )


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def sanitize_results(result: Dict[str, Any]) -> Dict[str, Any]:
    text = json.dumps(result, ensure_ascii=False)
    if len(text) <= 20000:
        return result
    compact = dict(result)
    compact["note"] = "trimmed_for_log"
    compact.pop("iterations", None)
    return compact


def run_with_captured_output(log_dir: Path, fn, *args, **kwargs):
    log_dir.mkdir(parents=True, exist_ok=True)
    out_path = log_dir / "stdout.log"
    with out_path.open("a", encoding="utf-8") as stream, redirect_stdout(stream), redirect_stderr(stream):
        return fn(*args, **kwargs)


def generate_schematic_figure(
    spec_name: str,
    spec: Dict[str, Any],
    api_base: str,
    api_key: str,
    model_info: Dict[str, Any],
) -> Dict[str, Any]:
    module = load_module("focus3_schematic_skill", SCHEMATIC_SKILL)
    generator = module.ScientificSchematicGenerator(api_key=api_key, verbose=True)
    generator.base_url = api_base
    generator.image_model = model_info["image_model"]
    generator.review_model = model_info["review_model"]

    log_dir = LOG_ROOT / spec_name
    temp_output = log_dir / f"{spec_name}.png"
    prompt = combine_prompt(spec["prompt"], spec["negative_prompt"])
    with ProxyBypass():
        results = run_with_captured_output(
            log_dir,
            generator.generate_iterative,
            prompt,
            str(temp_output),
            spec["iterations"],
            spec["doc_type"],
        )
    if not Path(temp_output).exists():
        raise RuntimeError(f"{spec_name}: final image was not generated")
    shutil.copy2(temp_output, spec["output"])
    payload = {
        "figure": spec_name,
        "backend": spec["backend"],
        "status": "ok",
        "output": str(spec["output"]),
        "temp_output": str(temp_output),
        "image_model": model_info["image_model"],
        "review_model": model_info["review_model"],
        "doc_type": spec["doc_type"],
        "iterations_requested": spec["iterations"],
        "results": sanitize_results(results),
    }
    write_json(log_dir / "result.json", payload)
    return payload


def generate_infographic_figure(
    spec_name: str,
    spec: Dict[str, Any],
    api_base: str,
    api_key: str,
    model_info: Dict[str, Any],
) -> Dict[str, Any]:
    module = load_module("focus3_infographic_skill", INFOGRAPHIC_SKILL)
    generator = module.InfographicGenerator(api_key=api_key, verbose=True)
    generator.base_url = api_base
    generator.image_model = model_info["image_model"]
    generator.review_model = model_info["review_model"]

    log_dir = LOG_ROOT / spec_name
    temp_output = log_dir / f"{spec_name}.png"
    prompt = combine_prompt(spec["prompt"], spec["negative_prompt"])
    with ProxyBypass():
        results = run_with_captured_output(
            log_dir,
            generator.generate_iterative,
            prompt,
            str(temp_output),
            spec["infographic_type"],
            spec["style"],
            spec["palette"],
            spec["background"],
            spec["iterations"],
            spec["doc_type"],
            spec["research"],
        )
    if not Path(temp_output).exists():
        raise RuntimeError(f"{spec_name}: final image was not generated")
    shutil.copy2(temp_output, spec["output"])
    payload = {
        "figure": spec_name,
        "backend": spec["backend"],
        "status": "ok",
        "output": str(spec["output"]),
        "temp_output": str(temp_output),
        "image_model": model_info["image_model"],
        "review_model": model_info["review_model"],
        "doc_type": spec["doc_type"],
        "iterations_requested": spec["iterations"],
        "results": sanitize_results(results),
    }
    write_json(log_dir / "result.json", payload)
    return payload


def generate_image_figure(
    spec_name: str,
    spec: Dict[str, Any],
    api_base: str,
    api_key: str,
    model_info: Dict[str, Any],
) -> Dict[str, Any]:
    module = load_module("focus3_image_skill", IMAGE_SKILL)
    log_dir = LOG_ROOT / spec_name
    log_dir.mkdir(parents=True, exist_ok=True)
    temp_output = log_dir / f"{spec_name}.png"
    prompt = combine_prompt(spec["prompt"], spec["negative_prompt"])

    request_payload = {
        "model": model_info["image_model"],
        "messages": [{"role": "user", "content": prompt}],
        "modalities": ["image", "text"],
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    with (log_dir / "stdout.log").open("a", encoding="utf-8") as stream:
        stream.write(f"[{now_str()}] generating {spec_name} with {model_info['image_model']}\n")

    session = requests.Session()
    session.trust_env = False
    response = session.post(
        f"{api_base}/chat/completions",
        headers=headers,
        json=request_payload,
        timeout=180,
    )
    response.raise_for_status()
    result = response.json()

    if not result.get("choices"):
        raise RuntimeError(f"{spec_name}: response has no choices")
    message = result["choices"][0]["message"]
    images = []
    if message.get("images"):
        images = message["images"]
    elif message.get("content") and isinstance(message["content"], list):
        for part in message["content"]:
            if isinstance(part, dict) and part.get("type") == "image":
                images.append(part)
    if not images:
        raise RuntimeError(f"{spec_name}: no image found in response")

    image_obj = images[0]
    if "image_url" in image_obj:
        image_data = image_obj["image_url"]["url"]
    elif "url" in image_obj:
        image_data = image_obj["url"]
    else:
        raise RuntimeError(f"{spec_name}: unsupported image payload shape")

    module.save_base64_image(image_data, str(temp_output))
    shutil.copy2(temp_output, spec["output"])

    message_copy = dict(message)
    if "images" in message_copy:
        message_copy["images"] = f"<{len(images)} image payload(s) omitted>"
    payload = {
        "figure": spec_name,
        "backend": spec["backend"],
        "status": "ok",
        "output": str(spec["output"]),
        "temp_output": str(temp_output),
        "image_model": model_info["image_model"],
        "response_preview": {"choices": [{"message": message_copy}]},
    }
    write_json(log_dir / "result.json", payload)
    return payload


def render_one_figure(
    spec_name: str,
    spec: Dict[str, Any],
    api_base: str,
    api_key: str,
    model_info: Dict[str, Any],
) -> Dict[str, Any]:
    attempts: List[Dict[str, Any]] = []
    for attempt in range(1, 3):
        try:
            if spec["backend"] == "scientific-schematics":
                payload = generate_schematic_figure(spec_name, spec, api_base, api_key, model_info)
            elif spec["backend"] == "infographics":
                payload = generate_infographic_figure(spec_name, spec, api_base, api_key, model_info)
            elif spec["backend"] == "generate-image":
                payload = generate_image_figure(spec_name, spec, api_base, api_key, model_info)
            else:
                raise RuntimeError(f"Unsupported backend: {spec['backend']}")
            payload["attempts"] = attempts + [{"attempt": attempt, "status": "ok"}]
            return payload
        except Exception as exc:
            error_payload = {"attempt": attempt, "status": "error", "error": str(exc)}
            attempts.append(error_payload)
            write_json(LOG_ROOT / spec_name / f"attempt_{attempt}_error.json", error_payload)
            if attempt == 2:
                return {
                    "figure": spec_name,
                    "backend": spec["backend"],
                    "status": "error",
                    "output": str(spec["output"]),
                    "attempts": attempts,
                }
            time.sleep(2)
    raise RuntimeError("unreachable")


def compile_report() -> Dict[str, Any]:
    paper_dir = ROOT / "paper"
    log_path = LOG_ROOT / "latexmk.log"
    cmd = ["latexmk", "-xelatex", "-interaction=nonstopmode", "focus3_report.tex"]
    result = subprocess.run(
        cmd,
        cwd=paper_dir,
        capture_output=True,
        text=True,
        errors="replace",
    )
    log_path.write_text(result.stdout + "\n\n[stderr]\n" + result.stderr, encoding="utf-8")
    payload = {
        "command": cmd,
        "cwd": str(paper_dir),
        "returncode": result.returncode,
        "log": str(log_path),
        "pdf": str(paper_dir / "focus3_report.pdf"),
    }
    if result.returncode != 0:
        raise RuntimeError(f"latexmk failed, see {log_path}")
    return payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate external manual figures for Focus3 paper.")
    parser.add_argument(
        "--only",
        help="Comma-separated figure ids to generate. Default: all four figures.",
    )
    parser.add_argument(
        "--skip-compile",
        action="store_true",
        help="Generate images only and skip LaTeX compilation.",
    )
    return parser.parse_args()


def validate_env() -> Tuple[str, str]:
    api_key = os.getenv("FIGURE_API_KEY")
    api_base = os.getenv("FIGURE_API_BASE")
    if not api_key or not api_base:
        raise SystemExit("Missing FIGURE_API_KEY or FIGURE_API_BASE")
    return api_key, normalize_api_base(api_base)


def selected_specs(only_arg: str | None) -> List[str]:
    if not only_arg:
        return list(FIGURE_SPECS.keys())
    names = [item.strip() for item in only_arg.split(",") if item.strip()]
    unknown = [name for name in names if name not in FIGURE_SPECS]
    if unknown:
        raise SystemExit(f"Unknown figure ids: {', '.join(unknown)}")
    return names


def main() -> int:
    args = parse_args()
    ensure_paths()
    api_key, api_base = validate_env()
    targets = selected_specs(args.only)
    model_info = discover_models(api_base, api_key)

    manifest: Dict[str, Any] = {
        "started_at": now_str(),
        "api_base": api_base,
        "targets": targets,
        "model_discovery": model_info,
        "figures": [],
        "compile": None,
    }

    for figure_name in targets:
        spec = FIGURE_SPECS[figure_name]
        result = render_one_figure(figure_name, spec, api_base, api_key, model_info)
        manifest["figures"].append(result)
        write_json(LOG_ROOT / "run_manifest.json", manifest)

    if not args.skip_compile:
        manifest["compile"] = compile_report()
        write_json(LOG_ROOT / "run_manifest.json", manifest)

    manifest["finished_at"] = now_str()
    write_json(LOG_ROOT / "run_manifest.json", manifest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
