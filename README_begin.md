# Focus3 中文噪声鲁棒性调研工程

本仓库用于完成一项中文大模型鲁棒性调研：研究真实噪声文本中的规范化缺失，是否会在事实不变的前提下诱发结构化抽取与事实分类输出翻转。

当前正式报告成品位于 [paper/focus3_report.pdf](/d:/NLP/HW/HW1/paper/focus3_report.pdf)，对应的 LaTeX 源文件位于 [paper/focus3_report.tex](/d:/NLP/HW/HW1/paper/focus3_report.tex)。

## 项目内容

本仓库包含以下几部分：

- `data/`：Focus3 主集、校准集及相关问题库。
- `runs/`：模型响应、评分、汇总表、分层分析表和 flip case 分析结果。
- `scripts/`：数据构造、评测、评分、汇总和绘图脚本。
- `paper/`：正式论文源码、图表和最终 PDF。
- `docs/`：早期草稿、实验说明和中间文档。

## 当前结论

正式报告当前冻结口径如下：

- `simp_trad`：正式成立。
- `ocr_confusable`：正式成立。
- `full_half_width`：弱对照，不正式成立。
- `classification`：仅作补充分析，不进入正式 C。

## 关键产物路径

- 正式报告 PDF：

  - [paper/focus3_report.pdf](/d:/NLP/HW/HW1/paper/focus3_report.pdf)
- 正式报告源码：

  - [paper/focus3_report.tex](/d:/NLP/HW/HW1/paper/focus3_report.tex)
- 数据图脚本：

  - [scripts/plot_focus3_figures.py](/d:/NLP/HW/HW1/scripts/plot_focus3_figures.py)
- API 模板文件：

  - [api.example.md](/d:/NLP/HW/HW1/api.example.md)

## 常用命令

重新生成数据图：

```powershell
python scripts/plot_focus3_figures.py
```

重新编译正式报告：

```powershell
cd paper
latexmk -xelatex -interaction=nonstopmode focus3_report.tex
```

## 备注

- PowerShell 当前环境会夹带 conda 的 GBK 编码噪声，这通常不是主命令失败依据。
- 当前正式 PDF 仍然可直接交付。
- 若准备公开仓库，请只提交源码、配置、文档和论文 TeX；本地密钥请参考 [api.example.md](/d:/NLP/HW/HW1/api.example.md) 自行配置。
