from scripts.normalization_repair import (
    build_company_registry,
    registry_match_company,
    repair_amount_value,
    repair_date_value,
    repair_extraction_output,
    simplify_script,
)
from scripts.score_outputs_repaired import resolve_registry_rows


def test_simplify_script_handles_focus3_company() -> None:
    assert simplify_script("藍海數據") == "蓝海数据"


def test_ocr_numeric_slots_repair_date_and_amount() -> None:
    assert repair_date_value("Z026-08-04") == "2026-08-04"
    assert repair_amount_value("IS00万元") == "1500万元"
    assert repair_amount_value("S00万元") == "500万元"


def test_company_registry_repairs_ocr_suffix_without_deleting_suffix() -> None:
    company, reason = registry_match_company("蓝海数据AI", "确认 蓝海数据AI 在2026年完成融资", ["蓝海数据A1"])
    assert company == "蓝海数据A1"
    assert reason == "ocr_equivalent_registry"


def test_company_english_suffix_is_preserved_when_not_confusable() -> None:
    company, reason = registry_match_company("远景智能Lab", "远景智能Lab于2026年完成融资", ["远景智能Lab"])
    assert company == "远景智能Lab"
    assert reason is None


def test_field_aware_repair_uses_registry_for_company() -> None:
    parsed = {"company": "华澄资讯8B", "date": "2026-10-10", "amount": "1800万元"}
    sample = {"input": "【融资公告】华澄资讯8B于2026年10月10日完成1800万元融资"}
    repaired = repair_extraction_output(
        parsed,
        sample,
        repair_mode="field_aware",
        registry=["华澄资讯B8"],
    )
    assert repaired.output == {"company": "华澄资讯B8", "date": "2026-10-10", "amount": "1800万元"}
    assert repaired.actions[0]["field"] == "company"


def test_strict_registry_requires_independent_bank() -> None:
    try:
        resolve_registry_rows(
            repair_mode="field_aware",
            registry_scope="strict",
            registry_problem_bank="",
            main_problem_rows=[],
        )
    except RuntimeError as exc:
        assert "calibration" in str(exc)
    else:
        raise AssertionError("strict field_aware must reject missing calibration registry")


def test_oracle_registry_is_explicit() -> None:
    rows = [
        {"task_type": "extraction", "gold": {"company": "测试公司A1"}},
        {"task_type": "extraction", "gold": {"company": "测试公司A1"}},
    ]
    registry_rows, source = resolve_registry_rows(
        repair_mode="field_aware",
        registry_scope="oracle",
        registry_problem_bank="",
        main_problem_rows=rows,
    )
    assert source == "oracle:test_gold"
    assert build_company_registry(registry_rows) == ["测试公司A1"]
