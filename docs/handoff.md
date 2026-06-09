# HW1_solve 项目交接

## 当前状态

`HW1_solve` 已重构为正式学术论文版本。论文主线为 SCCP（Schema-Conditioned Canonical Projection，模式条件规范投影），核心 insight 是：语义不变性不等于表示不变性，结构化抽取错误主要发生在语义表示到规范字段空间的投影阶段。

当前 PDF/LaTeX：

- `paper/final_report.tex`：正式论文源码。
- `paper/final_report.pdf`：编译产物。
- `paper/references.bib`：参考文献。

## 结果口径

主文只使用 strict registry 结果：

- Raw LLM：`simp_trad=55.2264pp`，`ocr_confusable=65.2603pp`，`full_half_width=1.4583pp`。
- Char/Num：`simp_trad=1.9746pp`，`ocr_confusable=45.6388pp`，`full_half_width=1.4583pp`。
- Strict SCCP：`simp_trad=0.0000pp`，`ocr_confusable=14.3583pp`，`full_half_width=0.8333pp`。

覆盖边界：

- Calibration registry：12 个实体。
- Main set：18 个实体，其中 12 seen / 6 unseen。
- Strict SCCP OCR：all `14.3583pp`，seen `3.4375pp`，unseen `35.8929pp`。

Oracle 上界：

- `simp_trad=0.0000pp`，`ocr_confusable=2.9167pp`，`full_half_width=0.0000pp`。
- 只放附录，不作为主结果。

## 关键脚本

- `scripts/normalization_repair.py`：SCCP 字段规范投影核心。
- `scripts/score_outputs_repaired.py`：修复后重评分；默认 strict registry。
- `scripts/summarize_registry_coverage.py`：seen/unseen 覆盖分析。
- `scripts/plot_sccp_figures.py`：正式论文五张机制图与统计图。
- `scripts/api_credentials.py`：本地私有 API 文件解析，不输出密钥。
- `scripts/smoke_api.py`：在线消融前的安全 smoke test。

## 最小验证

```bash
cd /Users/zane/Desktop/NLP/HW/HW1/HW1_solve

~/.codex/venvs/codex311/bin/python -m pytest \
  tests/test_normalization_repair.py tests/test_run_eval.py tests/test_common.py -q

~/.codex/venvs/codex311/bin/python -m compileall scripts

~/.codex/venvs/codex311/bin/python scripts/plot_sccp_figures.py \
  --cell-summary runs/sccp_summary_cells.csv \
  --c-summary runs/sccp_c_summary.csv \
  --coverage-summary runs/registry_coverage_summary.csv \
  --output-dir paper/figures
```

LaTeX 推荐使用插件编译器或本机 `latexmk`：

```bash
cd paper
latexmk -xelatex -interaction=nonstopmode final_report.tex
```

## 在线消融

真实 API 信息在 `../HW1_begin/api.md`。不要复制密钥到 `HW1_solve`，不要把密钥写入日志、论文或配置。

先 smoke：

```bash
~/.codex/venvs/codex311/bin/python scripts/smoke_api.py --provider gmn --api-doc ../HW1_begin/api.md --allow-responses-fallback
~/.codex/venvs/codex311/bin/python scripts/smoke_api.py --provider siliconflow --api-doc ../HW1_begin/api.md
```

若 smoke 失败，在线消融不进入论文。

当前已验证状态：

- GMN/GPT 返回 `INVALID_API_KEY`，不可用于本轮在线消融。
- SiliconFlow 的模型列表可访问，但当前未提供计划中的 `zai-org/GLM-4.6`。
- SiliconFlow `Pro/zai-org/GLM-4.7` 可用；极小切片结果为普通条件 4/8、预处理条件 8/8、完整 SCCP 条件 8/8。

GLM-4.7 切片只作为在线可行性证据，不作为主文主结果。

## 注意事项

- 不要修改 `HW1_begin/`。
- 不要把 `field_aware` 旧结果误写成主结果；旧文件使用测试集 gold 构建实体表，属于 oracle-like 上界。
- 主文不得出现课程、结项、文件路径、命令、API、密钥等工程痕迹。
- docs 可以保留复现命令和工程说明，论文正文必须用抽象学术概念表达。
- 当前正式 PDF 已编译为 10 页；若继续扩写，优先增加理论推导、相关工作和案例分析，而不是恢复工程命令。
