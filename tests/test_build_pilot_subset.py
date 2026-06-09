import unittest

from scripts.build_pilot_subset import build_subset
from scripts.common import read_jsonl


class BuildPilotSubsetTest(unittest.TestCase):
    def test_subtype_balanced_40_counts(self) -> None:
        rows = read_jsonl("data/pilot_problem_bank.jsonl")
        subset = build_subset(rows, mode="subtype_balanced_40")

        self.assertEqual(len(subset), 40)
        self.assertEqual(len({row["pair_id"] for row in subset}), 20)
        self.assertEqual(len({row["subtype_id"] for row in subset}), 10)

        for subtype_id in {row["subtype_id"] for row in subset}:
            subtype_rows = [row for row in subset if row["subtype_id"] == subtype_id]
            self.assertEqual(len(subtype_rows), 4)
            self.assertEqual(len({row["pair_id"] for row in subtype_rows}), 2)
            self.assertEqual({row["task_type"] for row in subtype_rows}, {"extraction", "classification"})
            for pair_id in {row["pair_id"] for row in subtype_rows}:
                pair_rows = [row for row in subtype_rows if row["pair_id"] == pair_id]
                self.assertEqual(len(pair_rows), 2)
                self.assertEqual({row["variant"] for row in pair_rows}, {"control", "perturbed"})

    def test_focus_subtypes_counts(self) -> None:
        rows = read_jsonl("data/pilot_problem_bank.jsonl")
        subset = build_subset(
            rows,
            mode="focus_subtypes",
            subtypes=["simp_trad", "minor_typo", "full_half_width"],
        )

        self.assertEqual(len(subset), 24)
        self.assertEqual(len({row["pair_id"] for row in subset}), 12)
        self.assertEqual({row["subtype_id"] for row in subset}, {"simp_trad", "minor_typo", "full_half_width"})

        for subtype_id in {row["subtype_id"] for row in subset}:
            subtype_rows = [row for row in subset if row["subtype_id"] == subtype_id]
            self.assertEqual(len(subtype_rows), 8)
            self.assertEqual(len({row["pair_id"] for row in subtype_rows}), 4)
            for pair_id in {row["pair_id"] for row in subtype_rows}:
                pair_rows = [row for row in subtype_rows if row["pair_id"] == pair_id]
                self.assertEqual(len(pair_rows), 2)
                self.assertEqual({row["variant"] for row in pair_rows}, {"control", "perturbed"})


if __name__ == "__main__":
    unittest.main()
