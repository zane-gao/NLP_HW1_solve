import os
import tempfile
import unittest

from scripts.api_credentials import parse_api_doc
from scripts.run_eval import parse_model_ids, provider_for_model, select_models, select_prompts


class RunEvalModelSelectionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.model_cfg = {
            "models": [
                {"model_id": "gpt-5.2", "enabled": True, "role": "candidate"},
                {"model_id": "gemini-3-flash", "enabled": True, "role": "candidate"},
                {"model_id": "DeepSeek-V3.2", "enabled": False, "role": "candidate"},
                {"model_id": "judge", "enabled": True, "role": "judge"},
            ],
            "pilot_model_ids": ["gpt-5.2"],
        }
        self.prompt_cfg = {
            "prompts": [
                {"prompt_id": "P1"},
                {"prompt_id": "P2"},
                {"prompt_id": "P3"},
                {"prompt_id": "P4"},
            ],
            "pilot_prompt_ids": ["P1", "P2"],
            "main_prompt_ids": ["P1", "P2", "P3", "P4"],
        }

    def test_parse_model_ids(self) -> None:
        self.assertEqual(parse_model_ids("gpt-5.2, gemini-3-flash"), ["gpt-5.2", "gemini-3-flash"])
        self.assertEqual(parse_model_ids(""), [])

    def test_select_models_uses_pilot_default(self) -> None:
        models = select_models(self.model_cfg, stage="pilot")
        self.assertEqual([model["model_id"] for model in models], ["gpt-5.2"])

    def test_select_models_overrides_with_requested_ids(self) -> None:
        models = select_models(self.model_cfg, stage="pilot", model_ids=["gemini-3-flash"])
        self.assertEqual([model["model_id"] for model in models], ["gemini-3-flash"])

    def test_select_models_requires_enabled_candidates(self) -> None:
        with self.assertRaises(RuntimeError):
            select_models(self.model_cfg, stage="pilot", model_ids=["DeepSeek-V3.2"])

    def test_select_prompts_uses_stage_default(self) -> None:
        prompts = select_prompts(self.prompt_cfg, stage="pilot")
        self.assertEqual([prompt["prompt_id"] for prompt in prompts], ["P1", "P2"])

    def test_select_prompts_overrides_with_requested_ids(self) -> None:
        prompts = select_prompts(self.prompt_cfg, stage="pilot", prompt_ids=["P1"])
        self.assertEqual([prompt["prompt_id"] for prompt in prompts], ["P1"])

    def test_select_prompts_requires_configured_ids(self) -> None:
        with self.assertRaises(RuntimeError):
            select_prompts(self.prompt_cfg, stage="pilot", prompt_ids=["P9"])

    def test_provider_for_model_prefers_known_local_provider(self) -> None:
        self.assertEqual(provider_for_model({"model_id": "gpt-5.2", "api_key_env": "GMN_API_KEY"}), "gmn")
        self.assertEqual(provider_for_model({"model_id": "GLM-4.6", "api_key_env": "SILICONFLOW_API_KEY"}), "siliconflow")

    def test_parse_api_doc_handles_prose_without_logging_secret(self) -> None:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as f:
            f.write(
                "gpt全系列\n"
                "sk-gmn-test-secret-1234567890\n"
                "url：https://gmn.example/v1\n\n"
                "SiliconFlow\n"
                "api_key: sf-test-secret-1234567890\n"
                "api_base: https://api.siliconflow.cn\n"
            )
            path = f.name
        try:
            parsed = parse_api_doc(path)
            self.assertEqual(parsed["gmn"].api_base, "https://gmn.example/v1")
            self.assertTrue(parsed["gmn"].api_key.startswith("sk-gmn"))
            self.assertEqual(parsed["siliconflow"].api_base, "https://api.siliconflow.cn")
            self.assertNotIn("api_key", parsed["gmn"].safe_dict())
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()
