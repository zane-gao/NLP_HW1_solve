from __future__ import annotations

import argparse
import random
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from scripts.common import load_config, write_jsonl


COMPANIES = [
    "华星科技",
    "远景智能",
    "蓝海数据",
    "晨曦医疗",
    "北辰网络",
    "天穹软件",
    "星河电商",
    "云杉资本",
    "长风教育",
    "新纪元物流",
    "银杉制造",
    "深蓝能源",
    "明德生物",
    "博远安全",
    "恒启机器人",
    "迅达互联",
    "智元科技",
    "万象云服",
    "金石材料",
    "瑞光芯片",
    "青禾农业",
    "凌云航科",
    "启真咨询",
    "华策文旅",
    "格致系统",
    "澄明支付",
    "沐川健康",
    "卓信智造",
    "青石出行",
    "远拓国际",
]

AMOUNTS = ["800万元", "900万元", "1000万元", "1200万元", "1500万元", "1800万元", "2000万元", "2200万元"]

PURPOSES = ["算法研发", "海外扩张", "渠道建设", "产线升级", "算力采购", "合规投入", "市场投放", "生态合作"]
CHANNELS = ["产品群", "项目群", "客户群", "运营群", "销售群", "投资群"]
PLATFORMS = ["财经热榜", "行业观察", "科技速递", "创业讨论区", "企业动态榜", "投融资圈"]
USERS = ["小林", "王敏", "李哲", "陈璐", "赵航", "唐宁"]
AGENTS = ["客服A12", "客服B07", "坐席C18", "坐席D03", "客服E21", "客服F05"]
CITIES = ["北京", "上海", "深圳", "杭州", "成都", "苏州"]

EMOJI_SET = ["📌", "✅", "🧾", "📣", "📝", "🤖", "💬", "📈"]


def default_experiment_cfg() -> Dict[str, Any]:
    return {
        "dataset": {
            "pair_count_total": 120,
            "rows_total": 240,
            "task_ratio": {"extraction_pairs": 80, "classification_pairs": 40},
            "min_pairs_per_subtype": 10,
            "human_semantic_check_ratio": 0.15,
        },
        "pipeline": {
            "pilot_pairs_per_subtype": 4,
            "pilot_extraction_per_subtype": 3,
            "pilot_classification_per_subtype": 1,
        },
        "thresholds": {
            "pilot_delta_err_pp": 10.0,
            "pilot_semantic_pass_rate": 0.9,
            "A_delta_err_pp": 15.0,
            "A_p_value": 0.05,
            "B_min_prompt_count": 3,
            "C_min_model_count": 5,
        },
    }


def default_perturb_cfg() -> Dict[str, Any]:
    return {
        "composite_ratio": 0.1,
        "emoji_markdown_mix": {"emoji_only": 0.5, "markdown_only": 0.3, "both": 0.2},
        "minor_typo_pairs": [
            ["公告", "公搞"],
            ["项目", "项木"],
            ["编号", "编呺"],
            ["完成", "宛成"],
            ["融资", "融姿"],
        ],
        "simp_trad_map": {
            "据": "據",
            "于": "於",
            "发": "發",
            "后": "後",
            "并": "並",
            "号": "號",
            "项": "項",
            "资": "資",
            "会": "會",
            "实": "實",
            "转": "轉",
            "网": "網",
            "录": "錄",
            "为": "為",
        },
        "ocr_confusable_map": {"0": "O", "1": "I", "2": "Z", "5": "S", "8": "B", "O": "0", "I": "1", "Z": "2", "S": "5"},
    }


def default_domain_cfg() -> Dict[str, Any]:
    return load_config("configs/domain_template_bank.yaml")


@dataclass
class BaseRecord:
    company: str
    year: int
    month: int
    day: int
    amount: str
    code: str
    purpose: str
    channel: str
    user: str
    agent: str
    city: str
    platform: str
    ticket_id: str

    @property
    def date_cn(self) -> str:
        return f"{self.year}年{self.month:02d}月{self.day:02d}日"

    @property
    def date_iso(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


def make_base_record(index: int) -> BaseRecord:
    return BaseRecord(
        company=COMPANIES[index % len(COMPANIES)],
        year=2026,
        month=(index % 12) + 1,
        day=(index % 27) + 1,
        amount=AMOUNTS[index % len(AMOUNTS)],
        code=f"AX{(index * 37) % 9000 + 1000}",
        purpose=PURPOSES[index % len(PURPOSES)],
        channel=CHANNELS[index % len(CHANNELS)],
        user=USERS[index % len(USERS)],
        agent=AGENTS[index % len(AGENTS)],
        city=CITIES[index % len(CITIES)],
        platform=PLATFORMS[index % len(PLATFORMS)],
        ticket_id=f"T{10000 + index}",
    )


def to_full_width_char(ch: str) -> str:
    code = ord(ch)
    if ch == " ":
        return "\u3000"
    if 33 <= code <= 126:
        return chr(code + 65248)
    return ch


def amount_bump(amount: str, step: int = 100) -> str:
    m = re.match(r"(\d+)(.+)", amount)
    if not m:
        return amount
    bumped = int(m.group(1)) + step
    return f"{bumped}{m.group(2)}"


def context_from_record(record: BaseRecord) -> Dict[str, str]:
    return {
        "company": record.company,
        "date_cn": record.date_cn,
        "date_iso": record.date_iso,
        "amount": record.amount,
        "code": record.code,
        "purpose": record.purpose,
        "channel": record.channel,
        "user": record.user,
        "agent": record.agent,
        "city": record.city,
        "platform": record.platform,
        "ticket_id": record.ticket_id,
    }


def render_extraction_text(domain_cfg: Dict[str, Any], domain_index: int, template_index: int, record: BaseRecord) -> Tuple[str, str, str]:
    domains = domain_cfg["domains"]
    domain = domains[domain_index % len(domains)]
    templates = domain["extraction_templates"]
    template_id = f"{domain['domain']}.ex.{template_index % len(templates)}"
    text = templates[template_index % len(templates)].format(**context_from_record(record))
    if not text.endswith(("。", ".", "！", "!", "？", "?")):
        text += "。"
    return text, domain["domain"], domain["source_style"]


def render_classification_input(
    domain_cfg: Dict[str, Any],
    domain_index: int,
    template_index: int,
    record: BaseRecord,
    supported: bool,
) -> Tuple[str, Dict[str, str], str, str]:
    evidence, domain_name, source_style = render_extraction_text(domain_cfg, domain_index, template_index, record)
    claim_amount = record.amount if supported else amount_bump(record.amount, step=100)
    claim = f"{record.company}在{record.date_iso}完成了{claim_amount}融资。"
    label = "支持" if supported else "不支持"

    domain = domain_cfg["domains"][domain_index % len(domain_cfg["domains"])]
    wrappers = domain["classification_wrappers"]
    wrapper_idx = template_index % len(wrappers)
    wrapper = wrappers[wrapper_idx]
    input_text = wrapper.format(text=evidence, claim=claim, **context_from_record(record))
    return input_text, {"label": label}, domain_name, source_style


def perturb_full_half_width(text: str, rng: random.Random) -> str:
    out: List[str] = []
    changed = False
    for ch in text:
        if ch.isdigit() or ("A" <= ch <= "Z") or ("a" <= ch <= "z"):
            if rng.random() < 0.75:
                fw = to_full_width_char(ch)
                out.append(fw)
                if fw != ch:
                    changed = True
            else:
                out.append(ch)
        else:
            out.append(ch)
    new_text = "".join(out)
    if changed:
        return new_text
    if "0" in text:
        return text.replace("0", "０", 1)
    return text + " "


def perturb_punctuation_style(text: str, rng: random.Random) -> str:
    mapping = [("，", ", "), ("。", "."), ("：", ":"), ("；", ";"), ("（", "("), ("）", ")"), ("【", "["), ("】", "]")]
    changed = False
    new_text = text
    for src, dst in mapping:
        if src in new_text and rng.random() < 0.65:
            new_text = new_text.replace(src, dst)
            changed = True
    if changed:
        return new_text
    if "。" in text:
        return text.replace("。", ".", 1)
    return text + " ;"


def perturb_whitespace_newline(text: str, rng: random.Random) -> str:
    candidates = [("，", "，\n"), ("。", "。\n"), ("：", "：\n"), ("；", "；\n"), ("|", " |\n")]
    new_text = text
    changed = False
    for src, dst in candidates:
        if src in new_text and rng.random() < 0.6:
            new_text = new_text.replace(src, dst, 1)
            changed = True
            break
    if "完成" in new_text and rng.random() < 0.7:
        newer = new_text.replace("完成", "完  成", 1)
        changed = changed or newer != new_text
        new_text = newer
    if changed:
        return new_text
    mid = max(1, len(text) // 2)
    return text[:mid] + "\n" + text[mid:]


def insert_zero_width(text: str, token: str) -> str:
    if token and token in text and len(token) > 1:
        noisy = token[0] + "\u200b" + token[1:]
        return text.replace(token, noisy, 1)
    return text


def perturb_zero_width_char(text: str, record: BaseRecord) -> str:
    new_text = insert_zero_width(text, record.company)
    if new_text != text:
        return new_text
    new_text = insert_zero_width(text, record.code)
    if new_text != text:
        return new_text
    return text + "\u200b"


def perturb_ocr_confusable(text: str, record: BaseRecord, mapping: Dict[str, str], rng: random.Random) -> str:
    new_text = text
    changed = False
    for token in [record.code, record.amount, record.date_iso]:
        if token not in new_text:
            continue
        converted = "".join(mapping.get(ch, ch) if rng.random() < 0.75 else ch for ch in token)
        if converted != token:
            new_text = new_text.replace(token, converted, 1)
            changed = True
            break
    if changed:
        return new_text
    for src, dst in mapping.items():
        if src in new_text:
            return new_text.replace(src, dst, 1)
    return new_text + " "


def perturb_simp_trad(text: str, mapping: Dict[str, str], rng: random.Random) -> str:
    out: List[str] = []
    changed = False
    for ch in text:
        if ch in mapping and rng.random() < 0.7:
            out.append(mapping[ch])
            changed = True
        else:
            out.append(ch)
    new_text = "".join(out)
    if changed:
        return new_text
    for src, dst in mapping.items():
        if src in text:
            return text.replace(src, dst, 1)
    return text


def perturb_quote_bracket_style(text: str, record: BaseRecord, rng: random.Random) -> str:
    pairs = [("《", "》"), ("“", "”"), ("\"", "\""), ("「", "」"), ("【", "】"), ("(", ")"), ("（", "）")]
    left, right = pairs[rng.randrange(len(pairs))]
    new_text = text
    if record.company in new_text:
        new_text = new_text.replace(record.company, f"{left}{record.company}{right}", 1)
    if new_text != text:
        return new_text
    if record.code in new_text:
        return new_text.replace(record.code, f"{left}{record.code}{right}", 1)
    return f"{left}{text}{right}"


def perturb_minor_typo(text: str, typo_pairs: List[List[str]], rng: random.Random) -> str:
    candidates = typo_pairs[:]
    rng.shuffle(candidates)
    for src, dst in candidates:
        if src in text:
            return text.replace(src, dst, 1)
    return text.replace("。", "。。", 1) if "。" in text else text + "。"


def perturb_markdown_wrap(text: str, rng: random.Random) -> str:
    styles = [f"- {text}", f"> {text}", f"**{text}**", f"`{text}`", f"```text\n{text}\n```"]
    return styles[rng.randrange(len(styles))]


def perturb_emoji_markdown_wrap(text: str, mode: str, rng: random.Random) -> str:
    left = EMOJI_SET[rng.randrange(len(EMOJI_SET))]
    right = EMOJI_SET[rng.randrange(len(EMOJI_SET))]
    if mode == "emoji_only":
        return f"{left} {text} {right}"
    if mode == "markdown_only":
        return perturb_markdown_wrap(text, rng)
    return f"> {left} **{text}** {right}"


def apply_single_perturb(
    text: str,
    subtype_id: str,
    record: BaseRecord,
    perturb_cfg: Dict[str, Any],
    rng: random.Random,
    emoji_mode: Optional[str] = None,
) -> Tuple[str, str]:
    if subtype_id == "full_half_width":
        return perturb_full_half_width(text, rng), "full_half_width"
    if subtype_id == "punctuation_style":
        return perturb_punctuation_style(text, rng), "punctuation_style"
    if subtype_id == "whitespace_newline":
        return perturb_whitespace_newline(text, rng), "whitespace_newline"
    if subtype_id == "zero_width_char":
        return perturb_zero_width_char(text, record), "zero_width_char"
    if subtype_id == "ocr_confusable":
        return perturb_ocr_confusable(text, record, perturb_cfg["ocr_confusable_map"], rng), "ocr_confusable"
    if subtype_id == "simp_trad":
        return perturb_simp_trad(text, perturb_cfg["simp_trad_map"], rng), "simp_trad"
    if subtype_id == "quote_bracket_style":
        return perturb_quote_bracket_style(text, record, rng), "quote_bracket_style"
    if subtype_id == "minor_typo":
        return perturb_minor_typo(text, perturb_cfg["minor_typo_pairs"], rng), "minor_typo"
    if subtype_id == "markdown_wrap":
        return perturb_markdown_wrap(text, rng), "markdown_wrap"
    if subtype_id == "emoji_markdown_wrap":
        mode = emoji_mode or "emoji_only"
        return perturb_emoji_markdown_wrap(text, mode, rng), f"emoji_markdown_wrap:{mode}"
    # fallback for tests with synthetic subtype ids.
    return perturb_punctuation_style(text, rng), "generic_noise"


def build_composite_flags(total_pairs: int, composite_ratio: float) -> List[bool]:
    count = int(round(total_pairs * composite_ratio))
    if count <= 0:
        return [False] * total_pairs
    flags = [False] * total_pairs
    used = set()
    for i in range(count):
        idx = int((i + 1) * total_pairs / count) - 1
        idx = max(0, min(total_pairs - 1, idx))
        while idx in used and idx + 1 < total_pairs:
            idx += 1
        if idx in used:
            idx = min(set(range(total_pairs)) - used)
        used.add(idx)
        flags[idx] = True
    return flags


def build_emoji_mode_schedule(total: int, mix: Dict[str, float], rng: random.Random) -> List[str]:
    n_emoji = int(round(total * float(mix["emoji_only"])))
    n_markdown = int(round(total * float(mix["markdown_only"])))
    n_both = total - n_emoji - n_markdown
    if n_both < 0:
        n_both = 0
    schedule = ["emoji_only"] * n_emoji + ["markdown_only"] * n_markdown + ["both"] * n_both
    while len(schedule) < total:
        schedule.append("emoji_only")
    if len(schedule) > total:
        schedule = schedule[:total]
    rng.shuffle(schedule)
    return schedule


def choose_secondary_subtype(primary: str, all_subtypes: List[str], rng: random.Random) -> Optional[str]:
    safe = [
        "full_half_width",
        "punctuation_style",
        "whitespace_newline",
        "zero_width_char",
        "ocr_confusable",
        "simp_trad",
        "quote_bracket_style",
        "markdown_wrap",
    ]
    candidates = [s for s in safe if s in all_subtypes and s != primary]
    if not candidates:
        return None
    return candidates[rng.randrange(len(candidates))]


def split_task_counts(total_pairs: Dict[str, int], extraction_target: int) -> Dict[str, Dict[str, int]]:
    subtypes = sorted(total_pairs.keys())
    expected = {s: total_pairs[s] * 2 / 3 for s in subtypes}
    extraction = {s: int(expected[s]) for s in subtypes}
    diff = extraction_target - sum(extraction.values())
    if diff > 0:
        order = sorted(subtypes, key=lambda s: expected[s] - extraction[s], reverse=True)
        for s in order:
            if diff == 0:
                break
            extraction[s] += 1
            diff -= 1
    elif diff < 0:
        order = sorted(subtypes, key=lambda s: expected[s] - extraction[s])
        for s in order:
            if diff == 0:
                break
            if extraction[s] > 0:
                extraction[s] -= 1
                diff += 1
    return {
        s: {"extraction": extraction[s], "classification": total_pairs[s] - extraction[s]} for s in subtypes
    }


def default_subtype_task_counts(phenomenon_cfg: Dict[str, Any], experiment_cfg: Dict[str, Any]) -> Dict[str, Dict[str, int]]:
    subtypes = [item["subtype_id"] for item in phenomenon_cfg["subtypes"]]
    dataset_cfg = experiment_cfg["dataset"]
    total_pairs = int(dataset_cfg["pair_count_total"])
    min_pairs = int(dataset_cfg["min_pairs_per_subtype"])
    extraction_target = int(dataset_cfg["task_ratio"]["extraction_pairs"])
    if min_pairs * len(subtypes) > total_pairs:
        raise ValueError("min_pairs_per_subtype 超过总 pair 数。")

    pair_total = {s: min_pairs for s in subtypes}
    extra = total_pairs - min_pairs * len(subtypes)
    for i in range(extra):
        pair_total[subtypes[i % len(subtypes)]] += 1
    return split_task_counts(pair_total, extraction_target=extraction_target)


def build_problem_bank_with_counts(
    phenomenon_cfg: Dict[str, Any],
    subtype_task_counts: Dict[str, Dict[str, int]],
    domain_cfg: Optional[Dict[str, Any]] = None,
    perturb_cfg: Optional[Dict[str, Any]] = None,
    pilot_cfg: Optional[Dict[str, Any]] = None,
    seed: int = 42,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    domain_cfg = domain_cfg or default_domain_cfg()
    perturb_cfg = perturb_cfg or default_perturb_cfg()
    pilot_cfg = pilot_cfg or {"pilot_pairs_per_subtype": 4, "pilot_extraction_per_subtype": 3, "pilot_classification_per_subtype": 1}

    subtypes = [item["subtype_id"] for item in phenomenon_cfg["subtypes"]]
    total_pairs = sum(int(v["extraction"]) + int(v["classification"]) for v in subtype_task_counts.values())
    composite_flags = build_composite_flags(total_pairs, float(perturb_cfg.get("composite_ratio", 0.1)))

    rows: List[Dict[str, Any]] = []
    pair_index: Dict[str, Dict[str, List[str]]] = {s: {"extraction": [], "classification": []} for s in subtypes}
    rng = random.Random(seed)
    global_record_index = 0
    global_pair_index = 0

    for subtype in subtypes:
        ex_count = int(subtype_task_counts[subtype]["extraction"])
        cls_count = int(subtype_task_counts[subtype]["classification"])
        pair_total_this = ex_count + cls_count
        local_rng = random.Random(seed + hash(subtype) % 100000 + pair_total_this)
        emoji_modes: List[Optional[str]] = [None] * pair_total_this
        if subtype == "emoji_markdown_wrap":
            emoji_modes = build_emoji_mode_schedule(pair_total_this, perturb_cfg["emoji_markdown_mix"], local_rng)
        local_idx = 0

        for i in range(ex_count):
            record = make_base_record(global_record_index)
            domain_index = global_pair_index % len(domain_cfg["domains"])
            template_index = (global_pair_index // len(domain_cfg["domains"])) % 3
            control_text, domain_name, source_style = render_extraction_text(domain_cfg, domain_index, template_index, record)

            pair_id = f"pair_ex_{subtype}_{i + 1:03d}"
            qid_c = f"{pair_id}_control"
            qid_p = f"{pair_id}_perturbed"
            pair_rng = random.Random(seed + global_pair_index * 13 + 7)
            primary_mode = emoji_modes[local_idx]
            perturbed_text, primary_op = apply_single_perturb(
                control_text, subtype, record, perturb_cfg, pair_rng, emoji_mode=primary_mode
            )
            perturb_ops = [primary_op]

            is_composite = composite_flags[global_pair_index]
            if is_composite:
                secondary = choose_secondary_subtype(subtype, subtypes, pair_rng)
                if secondary:
                    sec_mode = None
                    if secondary == "emoji_markdown_wrap":
                        sec_mode = build_emoji_mode_schedule(1, perturb_cfg["emoji_markdown_mix"], pair_rng)[0]
                    perturbed_text, secondary_op = apply_single_perturb(
                        perturbed_text, secondary, record, perturb_cfg, pair_rng, emoji_mode=sec_mode
                    )
                    perturb_ops.append(secondary_op)

            if perturbed_text == control_text:
                perturbed_text = control_text + "\n"
                perturb_ops.append("fallback_whitespace")

            gold = {"company": record.company, "date": record.date_iso, "amount": record.amount}
            rows.append(
                {
                    "qid": qid_c,
                    "pair_id": pair_id,
                    "task_type": "extraction",
                    "subtype_id": subtype,
                    "variant": "control",
                    "input": control_text,
                    "gold": gold,
                    "domain": domain_name,
                    "template_id": f"{domain_name}.ex.{template_index}",
                    "source_style": source_style,
                    "perturb_ops": [],
                    "is_composite": False,
                }
            )
            rows.append(
                {
                    "qid": qid_p,
                    "pair_id": pair_id,
                    "task_type": "extraction",
                    "subtype_id": subtype,
                    "variant": "perturbed",
                    "input": perturbed_text,
                    "gold": gold,
                    "domain": domain_name,
                    "template_id": f"{domain_name}.ex.{template_index}",
                    "source_style": source_style,
                    "perturb_ops": perturb_ops,
                    "is_composite": is_composite,
                }
            )
            pair_index[subtype]["extraction"].append(pair_id)
            global_pair_index += 1
            local_idx += 1
            global_record_index += 1

        for i in range(cls_count):
            record = make_base_record(global_record_index)
            domain_index = global_pair_index % len(domain_cfg["domains"])
            template_index = (global_pair_index // len(domain_cfg["domains"])) % 3
            supported = (i % 2) == 0
            control_text, gold, domain_name, source_style = render_classification_input(
                domain_cfg, domain_index, template_index, record, supported=supported
            )

            pair_id = f"pair_cls_{subtype}_{i + 1:03d}"
            qid_c = f"{pair_id}_control"
            qid_p = f"{pair_id}_perturbed"
            pair_rng = random.Random(seed + global_pair_index * 13 + 19)
            primary_mode = emoji_modes[local_idx]
            perturbed_text, primary_op = apply_single_perturb(
                control_text, subtype, record, perturb_cfg, pair_rng, emoji_mode=primary_mode
            )
            perturb_ops = [primary_op]

            is_composite = composite_flags[global_pair_index]
            if is_composite:
                secondary = choose_secondary_subtype(subtype, subtypes, pair_rng)
                if secondary:
                    sec_mode = None
                    if secondary == "emoji_markdown_wrap":
                        sec_mode = build_emoji_mode_schedule(1, perturb_cfg["emoji_markdown_mix"], pair_rng)[0]
                    perturbed_text, secondary_op = apply_single_perturb(
                        perturbed_text, secondary, record, perturb_cfg, pair_rng, emoji_mode=sec_mode
                    )
                    perturb_ops.append(secondary_op)

            if perturbed_text == control_text:
                perturbed_text = control_text + "\n"
                perturb_ops.append("fallback_whitespace")

            rows.append(
                {
                    "qid": qid_c,
                    "pair_id": pair_id,
                    "task_type": "classification",
                    "subtype_id": subtype,
                    "variant": "control",
                    "input": control_text,
                    "gold": gold,
                    "domain": domain_name,
                    "template_id": f"{domain_name}.cls.{template_index}",
                    "source_style": source_style,
                    "perturb_ops": [],
                    "is_composite": False,
                }
            )
            rows.append(
                {
                    "qid": qid_p,
                    "pair_id": pair_id,
                    "task_type": "classification",
                    "subtype_id": subtype,
                    "variant": "perturbed",
                    "input": perturbed_text,
                    "gold": gold,
                    "domain": domain_name,
                    "template_id": f"{domain_name}.cls.{template_index}",
                    "source_style": source_style,
                    "perturb_ops": perturb_ops,
                    "is_composite": is_composite,
                }
            )
            pair_index[subtype]["classification"].append(pair_id)
            global_pair_index += 1
            local_idx += 1
            global_record_index += 1

    pilot_pairs_per_subtype = int(pilot_cfg.get("pilot_pairs_per_subtype", 4))
    pilot_ex = int(pilot_cfg.get("pilot_extraction_per_subtype", max(1, int(pilot_pairs_per_subtype * 0.75))))
    pilot_cls = int(pilot_cfg.get("pilot_classification_per_subtype", max(1, pilot_pairs_per_subtype - pilot_ex)))
    pilot_pair_ids = set()
    for subtype in subtypes:
        pilot_pair_ids.update(pair_index[subtype]["extraction"][: min(pilot_ex, len(pair_index[subtype]["extraction"]))])
        pilot_pair_ids.update(pair_index[subtype]["classification"][: min(pilot_cls, len(pair_index[subtype]["classification"]))])
    pilot_rows = [row for row in rows if row["pair_id"] in pilot_pair_ids]
    return rows, pilot_rows


def build_problem_bank(
    phenomenon_cfg: Dict[str, Any],
    experiment_cfg: Optional[Dict[str, Any]] = None,
    domain_cfg: Optional[Dict[str, Any]] = None,
    perturb_cfg: Optional[Dict[str, Any]] = None,
    seed: int = 42,
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    experiment_cfg = experiment_cfg or default_experiment_cfg()
    subtype_task_counts = default_subtype_task_counts(phenomenon_cfg, experiment_cfg)
    return build_problem_bank_with_counts(
        phenomenon_cfg=phenomenon_cfg,
        subtype_task_counts=subtype_task_counts,
        domain_cfg=domain_cfg,
        perturb_cfg=perturb_cfg,
        pilot_cfg=experiment_cfg.get("pipeline"),
        seed=seed,
    )


def quality_report(rows: List[Dict[str, Any]], phenomenon_cfg: Dict[str, Any]) -> Dict[str, Any]:
    required = {"qid", "pair_id", "task_type", "subtype_id", "variant", "input", "gold"}
    required_ok = sum(1 for row in rows if required.issubset(set(row.keys())))
    pair_bucket: Dict[str, Dict[str, str]] = {}
    for row in rows:
        pair_bucket.setdefault(row["pair_id"], {})[row["variant"]] = row["input"]
    changed_pairs = sum(1 for _, v in pair_bucket.items() if "control" in v and "perturbed" in v and v["control"] != v["perturbed"])

    perturbed = [r for r in rows if r["variant"] == "perturbed"]
    non_empty_ops = sum(1 for r in perturbed if isinstance(r.get("perturb_ops"), list) and len(r["perturb_ops"]) > 0)
    composite_cnt = sum(1 for r in perturbed if bool(r.get("is_composite", False)))

    subtypes = [item["subtype_id"] for item in phenomenon_cfg["subtypes"]]
    subtype_hit = {}
    for subtype in subtypes:
        subtype_rows = [r for r in perturbed if r["subtype_id"] == subtype]
        hit = any(
            len(r.get("perturb_ops", [])) > 0
            and str(r["perturb_ops"][0]).startswith("emoji_markdown_wrap" if subtype == "emoji_markdown_wrap" else subtype)
            for r in subtype_rows
        )
        subtype_hit[subtype] = hit

    mode_bucket = {"emoji_only": 0, "markdown_only": 0, "both": 0}
    for row in perturbed:
        if row["subtype_id"] != "emoji_markdown_wrap":
            continue
        if not row.get("perturb_ops"):
            continue
        op = str(row["perturb_ops"][0])
        if ":" in op:
            mode = op.split(":", 1)[1]
            if mode in mode_bucket:
                mode_bucket[mode] += 1

    return {
        "rows_total": len(rows),
        "pair_total": len(pair_bucket),
        "required_field_ok_ratio": required_ok / max(1, len(rows)),
        "perturb_hit_ratio": changed_pairs / max(1, len(pair_bucket)),
        "perturbed_non_empty_ops_ratio": non_empty_ops / max(1, len(perturbed)),
        "composite_ratio": composite_cnt / max(1, len(perturbed)),
        "subtype_hit": subtype_hit,
        "emoji_markdown_mode_count": mode_bucket,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="生成真实场景扰动问题库（main + pilot）")
    parser.add_argument("--phenomenon", default="configs/phenomenon_bank.yaml")
    parser.add_argument("--experiment", default="configs/experiment.yaml")
    parser.add_argument("--domain-template", default="configs/domain_template_bank.yaml")
    parser.add_argument("--perturb-profile", default="configs/perturb_profile.yaml")
    parser.add_argument("--output", default="data/problem_bank.jsonl")
    parser.add_argument("--pilot-output", default="data/pilot_problem_bank.jsonl")
    parser.add_argument("--quality-report", default="")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    phenomenon_cfg = load_config(args.phenomenon)
    experiment_cfg = load_config(args.experiment)
    domain_cfg = load_config(args.domain_template)
    perturb_cfg = load_config(args.perturb_profile)

    rows, pilot_rows = build_problem_bank(
        phenomenon_cfg=phenomenon_cfg,
        experiment_cfg=experiment_cfg,
        domain_cfg=domain_cfg,
        perturb_cfg=perturb_cfg,
        seed=args.seed,
    )
    write_jsonl(args.output, rows)
    write_jsonl(args.pilot_output, pilot_rows)

    summary = quality_report(rows, phenomenon_cfg)
    if args.quality_report:
        Path(args.quality_report).write_text(str(summary), encoding="utf-8")

    total_pairs = len({row["pair_id"] for row in rows})
    pilot_pairs = len({row["pair_id"] for row in pilot_rows})
    print(f"[done] main rows={len(rows)} pairs={total_pairs} -> {Path(args.output)}")
    print(f"[done] pilot rows={len(pilot_rows)} pairs={pilot_pairs} -> {Path(args.pilot_output)}")
    print(
        "[quality] required_field_ok_ratio={:.3f} perturb_hit_ratio={:.3f} composite_ratio={:.3f}".format(
            summary["required_field_ok_ratio"], summary["perturb_hit_ratio"], summary["composite_ratio"]
        )
    )


if __name__ == "__main__":
    main()

