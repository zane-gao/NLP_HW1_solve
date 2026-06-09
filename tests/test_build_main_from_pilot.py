import unittest

from scripts.build_main_from_pilot import split_task_counts


class BuildMainFromPilotTest(unittest.TestCase):
    def test_split_task_counts_totals(self) -> None:
        pair_total = {f"s{i}": 30 for i in range(10)}
        counts = split_task_counts(pair_total, extraction_target=200)
        ex = sum(v["extraction"] for v in counts.values())
        cls = sum(v["classification"] for v in counts.values())
        self.assertEqual(ex, 200)
        self.assertEqual(cls, 100)


if __name__ == "__main__":
    unittest.main()

