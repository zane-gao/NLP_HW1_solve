import unittest

from scripts.common import extract_json_object, mcnemar_exact_p_value, normalize_date


class CommonUtilsTest(unittest.TestCase):
    def test_extract_json_object_from_wrapped_text(self) -> None:
        raw = "模型回答如下：```json\n{\"label\":\"支持\"}\n```"
        parsed = extract_json_object(raw)
        self.assertEqual(parsed, {"label": "支持"})

    def test_normalize_date_cn(self) -> None:
        self.assertEqual(normalize_date("二〇二六年三月三日"), "2026-03-03")

    def test_mcnemar_symmetry(self) -> None:
        p1 = mcnemar_exact_p_value(8, 2)
        p2 = mcnemar_exact_p_value(2, 8)
        self.assertAlmostEqual(p1, p2, places=8)


if __name__ == "__main__":
    unittest.main()

