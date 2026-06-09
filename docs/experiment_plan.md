# SCCP 实验计划与结果口径

本文档记录 `HW1_solve` 的可复现实验命令。论文正文只使用 strict registry 结果；oracle registry 仅作为上界放入附录。

## 1. 离线主实验

离线实验复用五模型四提示的固定 responses，只改变投影/修复阶段，避免新模型调用带来的版本和随机性影响。

```bash
cd /Users/zane/Desktop/NLP/HW/HW1/HW1_solve

~/.codex/venvs/codex311/bin/python scripts/score_outputs_repaired.py \
  --problem-bank data/problem_bank_focus3_main.jsonl \
  --registry-problem-bank data/problem_bank_focus3_calibration.jsonl \
  --registry-scope strict \
  --responses runs/responses_focus3_main_gpt52.jsonl,runs/responses_focus3_main_gemini.jsonl,runs/responses_focus3_main_deepseek.jsonl,runs/responses_focus3_main_glm46.jsonl,runs/responses_focus3_main_qwen235b.jsonl \
  --repair-mode field_aware \
  --scores runs/scores_focus3_main_5models_sccp_strict.jsonl \
  --hard-cases runs/hard_cases_focus3_main_5models_sccp_strict.jsonl \
  --repair-actions runs/repair_actions_sccp_strict.jsonl \
  --focus-task extraction

~/.codex/venvs/codex311/bin/python scripts/compare_repair_effects.py \
  --problem-bank data/problem_bank_focus3_main.jsonl \
  --task-type extraction \
  --score-set none=runs/scores_focus3_main_5models.jsonl \
  --score-set script_numeric=runs/scores_focus3_main_5models_script_numeric.jsonl \
  --score-set sccp_strict=runs/scores_focus3_main_5models_sccp_strict.jsonl \
  --score-set sccp_oracle=runs/scores_focus3_main_5models_sccp_oracle.jsonl \
  --cell-output runs/sccp_summary_cells.csv \
  --c-output runs/sccp_c_summary.csv \
  --acceptance-output runs/sccp_acceptance.csv

~/.codex/venvs/codex311/bin/python scripts/summarize_registry_coverage.py \
  --problem-bank data/problem_bank_focus3_main.jsonl \
  --registry-problem-bank data/problem_bank_focus3_calibration.jsonl \
  --score-set baseline=runs/scores_focus3_main_5models.jsonl \
  --score-set sccp_strict=runs/scores_focus3_main_5models_sccp_strict.jsonl \
  --summary-output runs/registry_coverage_summary.csv \
  --manifest-output runs/registry_manifest.csv
```

## 2. 当前主结果

主文采用 strict registry，即实体规范表只来自 calibration split。

| condition | simp_trad | ocr_confusable | full_half_width |
| --- | ---: | ---: | ---: |
| Raw LLM | 55.2264 | 65.2603 | 1.4583 |
| Char/Num | 1.9746 | 45.6388 | 1.4583 |
| Strict SCCP | 0.0000 | 14.3583 | 0.8333 |

覆盖边界：

| score_set | subtype | all | seen | unseen |
| --- | --- | ---: | ---: | ---: |
| Strict SCCP | simp_trad | 0.0000 | 0.0000 | 0.0000 |
| Strict SCCP | ocr_confusable | 14.3583 | 3.4375 | 35.8929 |
| Strict SCCP | full_half_width | 0.8333 | 0.0000 | 2.5000 |

registry manifest：

- Calibration registry：12 个实体。
- Main seen：12 个实体。
- Main unseen：6 个实体。

## 3. Oracle 上界

Oracle 需要显式 `--registry-scope oracle`，会使用测试集 gold 实体构建 registry，只能作为覆盖完整时的上界。

```bash
~/.codex/venvs/codex311/bin/python scripts/score_outputs_repaired.py \
  --problem-bank data/problem_bank_focus3_main.jsonl \
  --registry-scope oracle \
  --responses runs/responses_focus3_main_gpt52.jsonl,runs/responses_focus3_main_gemini.jsonl,runs/responses_focus3_main_deepseek.jsonl,runs/responses_focus3_main_glm46.jsonl,runs/responses_focus3_main_qwen235b.jsonl \
  --repair-mode field_aware \
  --scores runs/scores_focus3_main_5models_sccp_oracle.jsonl \
  --hard-cases runs/hard_cases_focus3_main_5models_sccp_oracle.jsonl \
  --repair-actions runs/repair_actions_sccp_oracle.jsonl \
  --focus-task extraction
```

Oracle 上界：

| condition | simp_trad | ocr_confusable | full_half_width |
| --- | ---: | ---: | ---: |
| Strict SCCP | 0.0000 | 14.3583 | 0.8333 |
| Oracle SCCP | 0.0000 | 2.9167 | 0.0000 |

## 4. 图表

```bash
~/.codex/venvs/codex311/bin/python scripts/plot_sccp_figures.py \
  --cell-summary runs/sccp_summary_cells.csv \
  --c-summary runs/sccp_c_summary.csv \
  --coverage-summary runs/registry_coverage_summary.csv \
  --output-dir paper/figures
```

输出：

- `paper/figures/sccp_prompt_invariance.pdf`
- `paper/figures/sccp_canonical_gap.pdf`
- `paper/figures/sccp_architecture.pdf`
- `paper/figures/sccp_main_results.pdf`
- `paper/figures/sccp_coverage_boundary.pdf`

## 5. 在线消融

在线消融可读取 `../HW1_begin/api.md` 或环境变量中的私有配置。脚本只读取密钥，不把密钥写入代码、配置、论文或日志。

官方接口依据：

- OpenAI Chat Completions：`POST /v1/chat/completions`。
- OpenAI Responses：Chat Completions 不兼容时作为 GPT fallback，接口路径为 `POST /v1/responses`。
- SiliconFlow Chat Completions：Bearer 认证，`https://api.siliconflow.cn/v1/chat/completions`。

先做 smoke：

```bash
~/.codex/venvs/codex311/bin/python scripts/smoke_api.py \
  --provider gmn \
  --api-doc ../HW1_begin/api.md \
  --allow-responses-fallback

~/.codex/venvs/codex311/bin/python scripts/smoke_api.py \
  --provider siliconflow \
  --api-doc ../HW1_begin/api.md
```

再跑精选消融：

```bash
~/.codex/venvs/codex311/bin/python scripts/run_eval.py \
  --stage main \
  --prompt-bank configs/prompt_bank_repair.yaml \
  --problem-bank data/intervention/problem_bank_base.jsonl \
  --model-ids gpt-5.2,GLM-4.6 \
  --prompt-ids P1,P4,NORM_P1,HDR_P4 \
  --output runs/responses_intervention_base.jsonl \
  --resume \
  --sleep-ms 300 \
  --api-doc ../HW1_begin/api.md \
  --allow-responses-fallback
```

当前 smoke 状态：

- GMN/GPT：`/v1/models` 返回 `INVALID_API_KEY`，暂不可用于在线消融。
- SiliconFlow：`/v1/models` 可访问，但当前模型列表未发现 `zai-org/GLM-4.6`；默认 GLM-4.6 smoke 返回模型/端点不可用。
- SiliconFlow 可用替代模型：`Pro/zai-org/GLM-4.7` smoke 成功；已完成 4 条样本 × 2 个提示的极小切片，普通条件 4/8，预处理条件 8/8，完整 SCCP 条件 8/8。

若目标模型 smoke 不通过，不得把对应在线结果写入论文正文；GLM-4.7 切片仅作为可行性证据，不进入主结论。
