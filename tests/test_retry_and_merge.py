import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.build_retry_bank import build_retry_rows, collect_retry_qids


class RetryBankTest(unittest.TestCase):
    def test_collect_retry_qids_latest_only(self) -> None:
        response_rows = [
            {"qid": "q1", "model_id": "m1", "prompt_id": "P1", "status": "error"},
            {"qid": "q1", "model_id": "m1", "prompt_id": "P1", "status": "ok"},
            {"qid": "q2", "model_id": "m1", "prompt_id": "P1", "status": "error"},
            {"qid": "q3", "model_id": "m1", "prompt_id": "P2", "status": "error"},
        ]
        self.assertEqual(collect_retry_qids(response_rows, model_id="m1", prompt_id="P1"), ["q2"])

    def test_build_retry_rows(self) -> None:
        problem_rows = [
            {"qid": "q1", "pair_id": "p1"},
            {"qid": "q2", "pair_id": "p2"},
            {"qid": "q3", "pair_id": "p3"},
        ]
        out = build_retry_rows(problem_rows, ["q3", "q1"])
        self.assertEqual([row["qid"] for row in out], ["q1", "q3"])


class MergeJsonlTest(unittest.TestCase):
    def test_merge_jsonl_cli(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp = Path(tmpdir)
            a = tmp / "a.jsonl"
            b = tmp / "b.jsonl"
            out = tmp / "out.jsonl"
            a.write_text('{"x":1}\n{"x":2}\n', encoding="utf-8")
            b.write_text('{"x":3}\n', encoding="utf-8")
            subprocess.run(
                [
                    "python",
                    "scripts/merge_jsonl.py",
                    "--inputs",
                    f"{a},{b}",
                    "--output",
                    str(out),
                ],
                check=True,
            )
            self.assertEqual(out.read_text(encoding="utf-8").strip().splitlines(), ['{"x":1}', '{"x":2}', '{"x":3}'])


if __name__ == "__main__":
    unittest.main()
