import unittest

from scripts.generate_problem_bank import build_problem_bank


class GenerateProblemBankTest(unittest.TestCase):
    def test_counts(self) -> None:
        phenomenon_cfg = {
            "subtypes": [{"subtype_id": f"s{i}"} for i in range(10)],
        }
        rows, pilot_rows = build_problem_bank(phenomenon_cfg)
        pair_ids = {row["pair_id"] for row in rows}
        pilot_pair_ids = {row["pair_id"] for row in pilot_rows}
        self.assertEqual(len(pair_ids), 120)
        self.assertEqual(len(rows), 240)
        self.assertEqual(len(pilot_pair_ids), 40)
        self.assertEqual(len(pilot_rows), 80)


if __name__ == "__main__":
    unittest.main()
