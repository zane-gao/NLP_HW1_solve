# NLP HW1 Solve: SCCP 中文规范不变性研究

本仓库包含一项关于中文真实噪声下大语言模型结构化抽取鲁棒性的完整研究产物。研究核心观点是：**语义不变性不等于表示不变性**。当输入中的简繁变体、全半角混排和 OCR 易混字符不改变事实含义时，模型仍可能在结构化字段层面输出不同表面表示，从而产生可观的不变性差距。

本文提出 **Schema-Conditioned Canonical Projection, SCCP**，即模式条件规范投影：根据字段模式把模型输出投影到字符、数值和实体规范空间，并用格式约束、源文本一致性和实体注册表进行保守选择。

## 主要产物

- 正式论文 PDF：[paper/final_report.pdf](paper/final_report.pdf)
- 论文 LaTeX 源码：[paper/final_report.tex](paper/final_report.tex)
- 参考文献：[paper/references.bib](paper/references.bib)
- 实验与项目交接：[docs/handoff.md](docs/handoff.md)
- 实验计划与口径：[docs/experiment_plan.md](docs/experiment_plan.md)

## 仓库结构

```text
configs/    模型、提示词、扰动类型和实验配置
data/       CanoInvar-ZH 主集、校准集和在线消融子集
docs/       方法设计、实验计划和交接文档
paper/      正式论文、图表、参考文献和最终 PDF
runs/       离线响应、评分、修复动作、汇总表和案例结果
scripts/    数据构造、模型调用、评分、规范投影、统计与绘图脚本
tests/      核心数据流、评分和规范修复逻辑的回归测试
```

## 关键实验口径

主文采用严格无泄漏设置：实体规范注册表仅由独立校准集构建，不从主测试集 gold 中读取待预测实体。

主要报告结果包括：

- baseline 下，简繁变体和 OCR 易混字符造成显著不变性差距；
- strict SCCP 显著缩小简繁与 OCR 差距；
- oracle registry 结果仅作为附录上界；
- seen/unseen 分析用于揭示实体覆盖率带来的开放世界边界。

## 复现命令

运行单元测试：

```bash
python -m pytest tests
```

重新生成 SCCP 图表：

```bash
python scripts/plot_sccp_figures.py
```

重新编译论文：

```bash
cd paper
latexmk -xelatex -interaction=nonstopmode -halt-on-error final_report.tex
```

## API 与密钥

仓库不包含任何私有 API key。在线实验脚本只在运行时从环境变量或本地私有说明文件读取密钥；请勿把真实密钥提交到仓库。

## 当前版本

当前提交包含最终论文、实验脚本、评测结果、图表和交接文档，可直接用于课程提交、复查和后续扩展。
