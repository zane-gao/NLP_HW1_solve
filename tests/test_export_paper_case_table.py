import tempfile
import unittest
from pathlib import Path

from scripts.export_paper_case_table import (
    build_body_markdown,
    build_paper_rows,
    build_appendix_markdown,
    read_csv_rows,
    select_body_rows,
)


class ExportPaperCaseTableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.case_rows = read_csv_rows("runs/flip_cases_focus3_cross_model.csv")
        self.summary_rows = read_csv_rows("runs/flip_summary_focus3_3models.csv")

    def test_select_body_rows(self) -> None:
        rows = select_body_rows(self.case_rows)
        self.assertEqual(len(rows), 3)
        self.assertEqual([row["pair_id"] for row in rows], [
            "pair_cls_full_half_width_001",
            "pair_ex_minor_typo_002",
            "pair_ex_simp_trad_003",
        ])

    def test_build_outputs(self) -> None:
        body_rows = select_body_rows(self.case_rows)
        body_md = build_body_markdown(self.summary_rows, body_rows)
        appendix_md = build_appendix_markdown(self.case_rows)
        paper_rows = build_paper_rows(self.case_rows)

        self.assertIn("### 3.4 Focus3 跨模型初筛结果", body_md)
        self.assertIn("### 4.1 代表性翻转样例", body_md)
        self.assertIn("### A.1 Focus3 八条翻转案例总表", appendix_md)
        self.assertEqual(len(paper_rows), 8)

        with tempfile.TemporaryDirectory() as tmpdir:
            body_path = Path(tmpdir) / "body.md"
            appendix_path = Path(tmpdir) / "appendix.md"
            body_path.write_text(body_md, encoding="utf-8")
            appendix_path.write_text(appendix_md, encoding="utf-8")
            self.assertTrue(body_path.exists())
            self.assertTrue(appendix_path.exists())


if __name__ == "__main__":
    unittest.main()
