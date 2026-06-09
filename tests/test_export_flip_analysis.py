import unittest

from scripts.common import read_jsonl
from scripts.export_flip_analysis import build_analysis


class ExportFlipAnalysisTest(unittest.TestCase):
    def test_gpt_focus3_analysis(self) -> None:
        problem_rows = read_jsonl("data/pilot_problem_bank.jsonl")
        response_rows = read_jsonl("runs/responses_pilot_full_gpt52.jsonl")
        score_rows = read_jsonl("runs/scores_pilot_full_gpt52.jsonl")

        case_rows, summary_rows = build_analysis(
            problem_rows,
            response_rows,
            score_rows,
            ["simp_trad", "minor_typo", "full_half_width"],
        )

        self.assertEqual(len(case_rows), 6)
        self.assertEqual(len(summary_rows), 6)

        case_by_key = {(row["prompt_id"], row["pair_id"]): row for row in case_rows}
        self.assertEqual(
            case_by_key[("P1", "pair_cls_full_half_width_001")]["trigger_shape"],
            "mixed_width_numeric_field",
        )
        self.assertEqual(
            case_by_key[("P1", "pair_ex_minor_typo_002")]["trigger_shape"],
            "entity_boundary_overattach",
        )
        self.assertEqual(
            case_by_key[("P1", "pair_ex_simp_trad_003")]["trigger_shape"],
            "script_variant_preserved",
        )

        summary_by_key = {(row["prompt_id"], row["subtype_id"]): row for row in summary_rows}
        self.assertEqual(summary_by_key[("P1", "full_half_width")]["flip_pairs"], "1")
        self.assertEqual(summary_by_key[("P2", "minor_typo")]["flip_pairs"], "1")
        self.assertEqual(summary_by_key[("P2", "simp_trad")]["flip_pairs"], "1")


if __name__ == "__main__":
    unittest.main()
