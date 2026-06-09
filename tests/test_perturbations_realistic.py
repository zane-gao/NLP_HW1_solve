import unittest

from scripts.common import load_config
from scripts.generate_problem_bank import build_problem_bank, quality_report


class PerturbationRealisticTest(unittest.TestCase):
    def setUp(self) -> None:
        self.phenomenon_cfg = load_config("configs/phenomenon_bank.yaml")
        self.experiment_cfg = load_config("configs/experiment.yaml")
        self.domain_cfg = load_config("configs/domain_template_bank.yaml")
        self.perturb_cfg = load_config("configs/perturb_profile.yaml")
        self.rows, _ = build_problem_bank(
            phenomenon_cfg=self.phenomenon_cfg,
            experiment_cfg=self.experiment_cfg,
            domain_cfg=self.domain_cfg,
            perturb_cfg=self.perturb_cfg,
            seed=42,
        )

    def test_each_subtype_has_primary_hit(self) -> None:
        report = quality_report(self.rows, self.phenomenon_cfg)
        for subtype, hit in report["subtype_hit"].items():
            self.assertTrue(hit, msg=f"subtype missing hit: {subtype}")

    def test_emoji_markdown_mix_ratio(self) -> None:
        perturbed = [
            r
            for r in self.rows
            if r["variant"] == "perturbed" and r["subtype_id"] == "emoji_markdown_wrap" and r["perturb_ops"]
        ]
        mode_count = {"emoji_only": 0, "markdown_only": 0, "both": 0}
        for row in perturbed:
            mode = str(row["perturb_ops"][0]).split(":", 1)[1]
            mode_count[mode] += 1
        total = len(perturbed)
        self.assertGreater(total, 0)
        self.assertAlmostEqual(mode_count["emoji_only"] / total, 0.5, delta=0.2)
        self.assertAlmostEqual(mode_count["markdown_only"] / total, 0.3, delta=0.2)
        self.assertAlmostEqual(mode_count["both"] / total, 0.2, delta=0.2)

    def test_composite_ratio(self) -> None:
        perturbed = [r for r in self.rows if r["variant"] == "perturbed"]
        composite = [r for r in perturbed if r.get("is_composite", False)]
        ratio = len(composite) / len(perturbed)
        self.assertAlmostEqual(ratio, 0.1, delta=0.03)


if __name__ == "__main__":
    unittest.main()

