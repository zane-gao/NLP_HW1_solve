from __future__ import annotations

import json
import math
import os
import re
import time
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple


def load_config(path: str | Path) -> Any:
    text = Path(path).read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore
    except Exception:
        yaml = None
    if yaml is not None:
        try:
            return yaml.safe_load(text)
        except Exception:
            pass
    return json.loads(text)


def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def read_jsonl(path: str | Path) -> List[Dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        return []
    rows: List[Dict[str, Any]] = []
    with p.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: str | Path, rows: Iterable[Dict[str, Any]]) -> None:
    ensure_parent(path)
    with Path(path).open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl(path: str | Path, row: Dict[str, Any]) -> None:
    ensure_parent(path)
    with Path(path).open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def utc_now_iso() -> str:
    return datetime.utcnow().isoformat(timespec="seconds") + "Z"


def resolve_chat_endpoint(api_base: str) -> str:
    base = api_base.rstrip("/")
    if base.endswith("/chat/completions"):
        return base
    if base.endswith("/v1"):
        return base + "/chat/completions"
    return base + "/v1/chat/completions"


def resolve_responses_endpoint(api_base: str) -> str:
    base = api_base.rstrip("/")
    if base.endswith("/responses"):
        return base
    if base.endswith("/v1"):
        return base + "/responses"
    return base + "/v1/responses"


def chat_completion(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    stop: Optional[List[str]] = None,
    timeout_sec: int = 120,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Tuple[bool, str, int, str]:
    endpoint = resolve_chat_endpoint(api_base)
    payload: Dict[str, Any] = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    if stop:
        payload["stop"] = stop
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        # Some third-party OpenAI-compatible gateways reject urllib's default client fingerprint.
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    if extra_headers:
        headers.update(extra_headers)

    start = time.perf_counter()
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
        latency_ms = int((time.perf_counter() - start) * 1000)
        parsed = json.loads(raw)
        content = parsed["choices"][0]["message"]["content"]
        if isinstance(content, list):
            content = "".join(
                chunk.get("text", "") if isinstance(chunk, dict) else str(chunk) for chunk in content
            )
        return True, str(content), latency_ms, ""
    except urllib.error.HTTPError as e:
        latency_ms = int((time.perf_counter() - start) * 1000)
        body = e.read().decode("utf-8", errors="replace")
        return False, "", latency_ms, f"HTTP {e.code}: {body}"
    except Exception as e:
        latency_ms = int((time.perf_counter() - start) * 1000)
        return False, "", latency_ms, str(e)


def responses_completion(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    timeout_sec: int = 120,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Tuple[bool, str, int, str]:
    endpoint = resolve_responses_endpoint(api_base)
    input_text = "\n\n".join(f"{m.get('role', 'user')}: {m.get('content', '')}" for m in messages)
    payload: Dict[str, Any] = {
        "model": model,
        "input": input_text,
        "temperature": temperature,
        "max_output_tokens": max_tokens,
    }
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    if extra_headers:
        headers.update(extra_headers)

    start = time.perf_counter()
    req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=timeout_sec) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
        latency_ms = int((time.perf_counter() - start) * 1000)
        parsed = json.loads(raw)
        if isinstance(parsed.get("output_text"), str):
            return True, parsed["output_text"], latency_ms, ""
        parts: List[str] = []
        for item in parsed.get("output", []):
            for content in item.get("content", []) if isinstance(item, dict) else []:
                if isinstance(content, dict):
                    if isinstance(content.get("text"), str):
                        parts.append(content["text"])
                    elif isinstance(content.get("content"), str):
                        parts.append(content["content"])
        return True, "".join(parts), latency_ms, ""
    except urllib.error.HTTPError as e:
        latency_ms = int((time.perf_counter() - start) * 1000)
        body = e.read().decode("utf-8", errors="replace")
        return False, "", latency_ms, f"HTTP {e.code}: {body}"
    except Exception as e:
        latency_ms = int((time.perf_counter() - start) * 1000)
        return False, "", latency_ms, str(e)


def retry_chat_completion(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    stop: Optional[List[str]] = None,
    timeout_sec: int = 120,
    max_retries: int = 3,
    retry_sleep_sec: float = 1.5,
    extra_headers: Optional[Dict[str, str]] = None,
) -> Tuple[bool, str, int, str]:
    last: Tuple[bool, str, int, str] = (False, "", 0, "unknown error")
    for attempt in range(1, max_retries + 1):
        ok, content, latency_ms, err = chat_completion(
            api_base=api_base,
            api_key=api_key,
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            timeout_sec=timeout_sec,
            extra_headers=extra_headers,
        )
        if ok:
            return ok, content, latency_ms, err
        last = (ok, content, latency_ms, err)
        if attempt < max_retries:
            time.sleep(retry_sleep_sec * attempt)
    return last


def retry_completion_with_fallback(
    api_base: str,
    api_key: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    stop: Optional[List[str]] = None,
    timeout_sec: int = 120,
    max_retries: int = 3,
    retry_sleep_sec: float = 1.5,
    extra_headers: Optional[Dict[str, str]] = None,
    allow_responses_fallback: bool = False,
) -> Tuple[bool, str, int, str, str]:
    ok, content, latency_ms, err = retry_chat_completion(
        api_base=api_base,
        api_key=api_key,
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        stop=stop,
        timeout_sec=timeout_sec,
        max_retries=max_retries,
        retry_sleep_sec=retry_sleep_sec,
        extra_headers=extra_headers,
    )
    if ok or not allow_responses_fallback:
        return ok, content, latency_ms, err, "chat_completions"
    ok2, content2, latency_ms2, err2 = responses_completion(
        api_base=api_base,
        api_key=api_key,
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout_sec=timeout_sec,
        extra_headers=extra_headers,
    )
    return ok2, content2, latency_ms + latency_ms2, err2 if not ok2 else "", "responses"


def extract_json_object(raw_text: Any) -> Optional[Dict[str, Any]]:
    if isinstance(raw_text, dict):
        return raw_text
    if raw_text is None:
        return None
    text = str(raw_text).strip()
    if not text:
        return None

    try:
        parsed = json.loads(text)
        return parsed if isinstance(parsed, dict) else None
    except Exception:
        pass

    fenced = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, flags=re.S | re.I)
    for candidate in fenced:
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, dict):
                return parsed
        except Exception:
            continue

    start_indices = [m.start() for m in re.finditer(r"\{", text)]
    for start in start_indices:
        depth = 0
        for idx in range(start, len(text)):
            ch = text[idx]
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    candidate = text[start : idx + 1]
                    try:
                        parsed = json.loads(candidate)
                        if isinstance(parsed, dict):
                            return parsed
                    except Exception:
                        break
    return None


def to_half_width(text: str) -> str:
    out = []
    for ch in text:
        code = ord(ch)
        if code == 12288:
            out.append(" ")
        elif 65281 <= code <= 65374:
            out.append(chr(code - 65248))
        else:
            out.append(ch)
    return "".join(out)


def normalize_spaces(text: str) -> str:
    text = re.sub(r"[\u200b\u200c\u200d\ufeff]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_company(text: str) -> str:
    s = normalize_spaces(to_half_width(str(text)))
    for token in ["《", "》", "“", "”", "\"", "'", "`", "*", "_", "[", "]", "(", ")", "（", "）"]:
        s = s.replace(token, "")
    return s


CN_DIGIT_MAP = {
    "零": 0,
    "〇": 0,
    "一": 1,
    "二": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
}


def cn_number_to_int(text: str) -> Optional[int]:
    text = text.strip()
    if not text:
        return None
    if all(ch in CN_DIGIT_MAP for ch in text):
        value = 0
        for ch in text:
            value = value * 10 + CN_DIGIT_MAP[ch]
        return value
    if text == "十":
        return 10
    if "十" in text:
        parts = text.split("十")
        tens = 1 if parts[0] == "" else CN_DIGIT_MAP.get(parts[0])
        ones = 0 if parts[1] == "" else CN_DIGIT_MAP.get(parts[1])
        if tens is None or ones is None:
            return None
        return tens * 10 + ones
    return None


def normalize_date(value: str) -> str:
    s = normalize_spaces(to_half_width(str(value)))
    s = s.replace("年", "-").replace("月", "-").replace("日", "")
    s = s.replace("/", "-").replace(".", "-")
    s = re.sub(r"-+", "-", s).strip("-")
    m = re.search(r"(\d{4})-(\d{1,2})-(\d{1,2})", s)
    if m:
        year, month, day = (int(m.group(1)), int(m.group(2)), int(m.group(3)))
        return f"{year:04d}-{month:02d}-{day:02d}"

    m_cn = re.search(r"([零〇一二三四五六七八九]{4})年([零〇一二三四五六七八九十]{1,3})月([零〇一二三四五六七八九十]{1,3})日?", value)
    if m_cn:
        year_str, month_str, day_str = m_cn.group(1), m_cn.group(2), m_cn.group(3)
        year = cn_number_to_int(year_str)
        month = cn_number_to_int(month_str)
        day = cn_number_to_int(day_str)
        if year and month and day:
            return f"{year:04d}-{month:02d}-{day:02d}"
    return s


def normalize_amount(value: str) -> str:
    s = normalize_spaces(to_half_width(str(value)))
    s = s.replace(",", "")
    s = s.replace("人民币", "")
    s = s.replace("元整", "元")
    s = s.replace(" ", "")
    return s


LABEL_ALIASES = {
    "支持": "支持",
    "是": "支持",
    "yes": "支持",
    "true": "支持",
    "entailment": "支持",
    "不支持": "不支持",
    "否": "不支持",
    "no": "不支持",
    "false": "不支持",
    "contradiction": "不支持",
}


def normalize_label(value: str) -> Optional[str]:
    s = normalize_spaces(to_half_width(str(value))).lower()
    s = s.replace("。", "").replace(".", "")
    if s in LABEL_ALIASES:
        return LABEL_ALIASES[s]
    if "不支持" in s:
        return "不支持"
    if "支持" in s:
        return "支持"
    return None


def mcnemar_exact_p_value(n01: int, n10: int) -> float:
    n = n01 + n10
    if n == 0:
        return 1.0
    k = min(n01, n10)
    cdf = sum(math.comb(n, i) for i in range(0, k + 1)) / (2**n)
    p = min(1.0, 2 * cdf)
    return p
