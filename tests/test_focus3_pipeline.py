import csv
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.analyze_focus3_layers import build_pair_bucket, build_rows
from scripts.common import read_jsonl
from scripts.generate_focus3_problem_bank import build_rows as build_focus_rows
from scripts.common import load_config


class Focus3GeneratorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.study_cfg = load_config("configs/focus3_study.yaml")
        self.template_cfg = load_config("configs/focus3_template_bank.yaml")

    def test_focus3_counts(self) -> None:
        main_rows, _ = build_focus_rows("main", self.study_cfg, self.template_cfg)
        calibration_rows, _ = build_focus_rows("calibration", self.study_cfg, self.template_cfg)
        self.assertEqual(len(main_rows), 240)
        self.assertEqual(len({row["pair_id"] for row in main_rows}), 120)
        self.assertEqual(len(calibration_rows), 36)
        self.assertEqual(len({row["pair_id"] for row in calibration_rows}), 18)

    def test_focus3_metadata_fields(self) -> None:
        main_rows, _ = build_focus_rows("main", self.study_cfg, self.template_cfg)
        perturbed = [row for row in main_rows if row["variant"] == "perturbed"]
        self.assertTrue(all(row["target_field"] in {"company", "date", "amount"} for row in perturbed))
        self.assertTrue(all(row["intensity"] in {"light", "medium", "hard"} for row in perturbed))
        self.assertAlmostEqual(sum(1 for row in perturbed if row["is_composite"]) / len(perturbed), 0.1, delta=0.03)


class AggregateSummaryTaskTypeTest(unittest.TestCase):
    def test_task_type_filter(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            problem_bank = tmp / "problem.jsonl"
            scores = tmp / "scores.jsonl"
            summary = tmp / "summary.csv"
            c_summary = tmp / "c_summary.csv"
            problem_bank.write_text(
                "\n".join(
                    [
                        '{"qid":"q1","pair_id":"p1","task_type":"extraction","subtype_id":"simp_trad","variant":"control","input":"a","gold":{"company":"甲","date":"2026-01-01","amount":"100万元"}}',
                        '{"qid":"q2","pair_id":"p1","task_type":"extraction","subtype_id":"simp_trad","variant":"perturbed","input":"b","gold":{"company":"甲","date":"2026-01-01","amount":"100万元"}}',
                        '{"qid":"q3","pair_id":"p2","task_type":"classification","subtype_id":"simp_trad","variant":"control","input":"c","gold":{"label":"支持"}}',
                        '{"qid":"q4","pair_id":"p2","task_type":"classification","subtype_id":"simp_trad","variant":"perturbed","input":"d","gold":{"label":"支持"}}',
                    ])
                    + "\n",
                encoding="utf-8",
            )
            scores.write_text(
                "\n".join(
                    [
                        '{"qid":"q1","model_id":"m1","prompt_id":"P1","is_correct":1,"error_type":"ok","score_source":"rule"}',
                        '{"qid":"q2","model_id":"m1","prompt_id":"P1","is_correct":0,"error_type":"mismatch_company","score_source":"rule"}',
                        '{"qid":"q3","model_id":"m1","prompt_id":"P1","is_correct":1,"error_type":"ok","score_source":"rule"}',
                        '{"qid":"q4","model_id":"m1","prompt_id":"P1","is_correct":1,"error_type":"ok","score_source":"rule"}',
                    ])
                    + "\n",
                encoding="utf-8",
            )
            subprocess.run(
                [
                    "python",
                    "scripts/aggregate_summary.py",
                    "--problem-bank",
                    str(problem_bank),
                    "--scores",
                    str(scores),
                    "--summary",
                    str(summary),
                    "--c-summary",
                    str(c_summary),
                    "--task-type",
                    "extraction",
                ],
                check=True,
            )
            with summary.open("r", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["pair_count"], "1")


class Focus3LayerAnalysisTest(unittest.TestCase):
    def test_build_rows(self) -> None:
        problem_rows = [
            {
                "qid": "q1",
                "pair_id": "p1",
                "task_type": "extraction",
                "subtype_id": "simp_trad",
                "variant": "control",
                "domain": "announcement",
                "source_style": "doc",
                "target_field": "company",
                "intensity": "light",
                "is_composite": False,
            },
            {
                "qid": "q2",
                "pair_id": "p1",
                "task_type": "extraction",
                "subtype_id": "simp_trad",
                "variant": "perturbed",
                "domain": "announcement",
                "source_style": "doc",
                "target_field": "company",
                "intensity": "light",
                "is_composite": False,
            },
        ]
        score_rows = {
            ("q1", "m1", "P1"): {"qid": "q1", "model_id": "m1", "prompt_id": "P1", "is_correct": 1},
            ("q2", "m1", "P1"): {"qid": "q2", "model_id": "m1", "prompt_id": "P1", "is_correct": 0},
        }
        bucket = build_pair_bucket(problem_rows, score_rows, task_type="extraction")
        rows = build_rows(bucket)
        self.assertTrue(rows)
        self.assertEqual(rows[0]["group_type"], "composition")


if __name__ == "__main__":
    unittest.main()
