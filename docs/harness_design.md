# SCCP 设计说明

本文档保留工程实现视角；论文正文应使用“模式条件规范投影”“组合式推断策略”“类型化规范算子”等学术表述，避免直接写工程文件名和命令。

## 1. 设计目标

- 严格无泄漏：主结果的实体 registry 只能来自 calibration split。
- 可追踪：每次字段修改记录 field/before/after/reason。
- 可消融：同一批 responses 可比较 Raw、Char/Num、Strict SCCP、Oracle SCCP。
- 可复算：评分记录保留 `(qid, model_id, prompt_id, repair_mode, registry_scope)`。
- 可扩展：后续可以把轻量规则替换为外部实体库、候选召回器或训练增强模型。

## 2. 方法抽象

论文中的 SCCP 对应工程中的 `field_aware` 修复，但口径更严格：

1. 字段路由：识别 company/date/amount。
2. 字符算子：简繁、全半角规范化。
3. 数字算子：date/amount 槽位的 OCR 数字恢复。
4. 实体投影：company 槽位使用 registry 做闭集规范化。
5. 一致性验证：只有等价签名或源文本锚定支持时才接受候选。
6. 决策追踪：记录 repair actions 供 case audit 与回归测试使用。

## 3. Registry 口径

`score_outputs_repaired.py` 默认：

- `--registry-scope strict`
- `--registry-problem-bank data/problem_bank_focus3_calibration.jsonl`

这会构建 12 个实体的独立校准 registry。若需要 oracle 上界，必须显式传：

```bash
--registry-scope oracle
```

任何新增脚本都不得默认从 main/test gold 构建 company registry。

## 4. 在线消融接口

在线消融只作为补充，不进入当前主结论。入口：

- `scripts/api_credentials.py`：解析环境变量或 `../HW1_begin/api.md`。
- `scripts/smoke_api.py`：provider smoke test。
- `scripts/run_eval.py --api-doc ../HW1_begin/api.md --allow-responses-fallback`：正式调用。

安全要求：

- 只读取密钥，不写入 `HW1_solve`。
- 输出中只写 `local_private`，不写真实 key。
- GPT 系列优先走 GMN；GLM 走 SiliconFlow。
- SiliconFlow 使用 OpenAI-compatible Chat Completions；当前 `Pro/zai-org/GLM-4.7` smoke 成功，`zai-org/GLM-4.6` 不可用。
- GPT 代理若不兼容 Chat Completions，可 fallback Responses API。

当前在线结果只保留为补充可行性证据：GLM-4.7 在 4 条样本、2 个提示上的普通条件为 4/8，预处理与完整 SCCP 为 8/8。该切片规模不足以支撑主文结论。

## 5. 论文图表

正式论文使用：

- `sccp_canonical_gap.*`
- `sccp_architecture.*`
- `sccp_prompt_invariance.*`
- `sccp_main_results.*`
- `sccp_coverage_boundary.*`

旧 `delta_heatmap`、`field_delta`、`repair_delta_by_mode` 可作为历史结果，不建议继续放进正式论文。
