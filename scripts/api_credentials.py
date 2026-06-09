from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


DEFAULT_API_DOC = Path(__file__).resolve().parents[2] / "HW1_begin" / "api.md"


@dataclass(frozen=True)
class ProviderCredential:
    provider: str
    api_key: str
    api_base: str
    source: str

    def safe_dict(self) -> Dict[str, str]:
        return {"provider": self.provider, "api_base": self.api_base, "source": self.source, "has_key": "1"}


PROVIDER_DEFAULT_BASE = {
    "gmn": "https://gmn.chuangzuoli.com",
    "siliconflow": "https://api.siliconflow.cn",
    "openrouter": "https://openrouter.ai/api/v1",
    "newapi": "https://new.12ai.org/v1",
}


PROVIDER_ENV = {
    "gmn": "GMN_API_KEY",
    "siliconflow": "SILICONFLOW_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
    "newapi": "NEWAPI_API_KEY",
}


def _looks_like_key(line: str) -> bool:
    stripped = line.strip().strip("`").strip()
    if len(stripped) < 16:
        return False
    if stripped.lower().startswith(("http://", "https://", "url", "api_base")):
        return False
    if re.search(r"(sk-|sf-|key|token|api)", stripped, flags=re.I):
        return True
    return bool(re.fullmatch(r"[A-Za-z0-9_\-\.]{24,}", stripped))


def _extract_url(line: str) -> Optional[str]:
    match = re.search(r"https?://[^\s`，,]+", line)
    return match.group(0).rstrip("/\"'}）)") if match else None


def _provider_from_text(text: str) -> Optional[str]:
    lowered = text.lower()
    if "siliconflow" in lowered or "硅基" in lowered:
        return "siliconflow"
    if any(name in lowered for name in ["deepseek", "qwen", "kimi", "glm"]):
        return "siliconflow"
    if "gmn" in lowered or "gpt" in lowered:
        return "gmn"
    if "claude" in lowered:
        return "openrouter"
    if "openrouter" in lowered:
        return "openrouter"
    if "newapi" in lowered or "gemini mirror" in lowered or "谷歌" in lowered:
        return "newapi"
    return None


def parse_api_doc(path: str | Path = DEFAULT_API_DOC) -> Dict[str, ProviderCredential]:
    p = Path(path)
    if not p.exists():
        return {}
    providers: Dict[str, Dict[str, str]] = {}
    current: Optional[str] = None
    for raw_line in p.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line:
            continue
        # 私有文档末尾可能含整段 JSON 连接信息。这里不解析它，避免覆盖上方人工标注的 provider。
        if line.startswith("{") and line.endswith("}"):
            continue
        provider = _provider_from_text(line)
        if provider:
            current = provider
            providers.setdefault(current, {})
        url = _extract_url(line)
        if url and current:
            providers.setdefault(current, {})["api_base"] = url
        if _looks_like_key(line) and current:
            # 支持 "- key: sk-..."、"api_key=..." 和独立一行 key。
            key = re.sub(r"^[-*\s`]*(api[_ -]?key|key|token)\s*[:：=]\s*", "", line, flags=re.I).strip(" `")
            providers.setdefault(current, {})["api_key"] = key

    credentials: Dict[str, ProviderCredential] = {}
    for provider_name, values in providers.items():
        api_key = values.get("api_key", "")
        if not api_key:
            continue
        credentials[provider_name] = ProviderCredential(
            provider=provider_name,
            api_key=api_key,
            api_base=values.get("api_base") or PROVIDER_DEFAULT_BASE.get(provider_name, ""),
            source=str(p),
        )
    return credentials


def load_provider_credential(provider: str, *, api_doc: str | Path = DEFAULT_API_DOC) -> Optional[ProviderCredential]:
    provider = provider.lower()
    env_name = PROVIDER_ENV.get(provider)
    if env_name and os.getenv(env_name):
        return ProviderCredential(
            provider=provider,
            api_key=os.environ[env_name],
            api_base=os.getenv(env_name.replace("_KEY", "_BASE"), PROVIDER_DEFAULT_BASE.get(provider, "")),
            source=f"env:{env_name}",
        )
    return parse_api_doc(api_doc).get(provider)
