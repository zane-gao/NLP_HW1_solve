from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.api_credentials import load_provider_credential
from scripts.common import retry_completion_with_fallback


MODEL_BY_PROVIDER = {
    "gmn": "gpt-5.2",
    "siliconflow": "zai-org/GLM-4.6",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="安全检查本地 API 配置，不输出密钥。")
    parser.add_argument("--provider", choices=["gmn", "siliconflow"], required=True)
    parser.add_argument("--api-doc", default="../HW1_begin/api.md")
    parser.add_argument("--model", default="")
    parser.add_argument("--allow-responses-fallback", action="store_true")
    parser.add_argument("--timeout-sec", type=int, default=45)
    args = parser.parse_args()

    credential = load_provider_credential(args.provider, api_doc=args.api_doc)
    if not credential:
        raise RuntimeError(f"未找到 {args.provider} 的可用本地配置。")

    ok, content, latency_ms, err, endpoint_kind = retry_completion_with_fallback(
        api_base=credential.api_base,
        api_key=credential.api_key,
        model=args.model or MODEL_BY_PROVIDER[args.provider],
        messages=[
            {"role": "system", "content": "你是格式严格的测试助手。"},
            {"role": "user", "content": "只输出 JSON：{\"ok\":true}"},
        ],
        temperature=0.0,
        max_tokens=64,
        timeout_sec=args.timeout_sec,
        max_retries=1,
        allow_responses_fallback=args.allow_responses_fallback,
    )
    print(
        json.dumps(
            {
                "provider": args.provider,
                "api_base": credential.api_base,
                "source": "local_private",
                "endpoint_kind": endpoint_kind,
                "ok": ok,
                "latency_ms": latency_ms,
                "error": "" if ok else err[:240],
                "response_preview": content[:80] if ok else "",
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
