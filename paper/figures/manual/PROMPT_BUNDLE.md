# Focus3 外部图生成资源包

这份资源包用于给正式报告补两类“论文风格”的外部图：概念框架图与数据流程图。仓库不直接调用 API，只提供固定路径、推荐 skill、分辨率建议和 prompt 约束。生成好的图片请放到指定位置，供正式报告使用。

## 必做图

### 1. `problem_framework_ai.png`
- 目标路径: `paper/figures/manual/problem_framework_ai.png`
- 推荐 skill: `scientific-schematics`
- 推荐比例 / 分辨率: `16:9`，建议 `1920x1080`
- 用途: 替换正文图 1，呈现“真实输入源 -> 三类规范化缺失 -> 五模型 -> 两条任务轨 -> 输出翻转”的整体逻辑。
- 正向 prompt:
  ```text
  publication-quality scientific schematic, white background, AI conference paper style, Chinese NLP robustness study, six real input sources including announcement, customer service transcript, social media post, email memo, instant message chat, form OCR, flowing into three normalization-gap mechanisms: simplified-traditional script variation, full-width half-width character mixing, OCR confusable characters, then into five frontier representative language models, then split into structured extraction and factual classification, final panel highlights output flip and field mismatch, emphasize fact unchanged but surface form changed, clean vector layout, high contrast, colorblind-safe palette, minimal text, no decorative clutter, no prompt text
  ```
- Negative prompt:
  ```text
  watermark, photorealistic, 3d, glossy gradients, dense paragraphs, layout instruction text, prompt leakage, low resolution, decorative background, unrelated icons, extra labels
  ```
- 必须出现的元素:
  - `6` 类真实输入源
  - `3` 类规范化缺失机制
  - `5` 个前沿代表模型
  - `2` 条任务轨
  - “事实不变、表面变化、输出翻转”的核心关系
- 禁止出现的元素:
  - 大段解释性文本
  - 品牌 logo
  - 花哨背景、炫光或装饰性纹理

### 2. `data_pipeline_ai.png`
- 目标路径: `paper/figures/manual/data_pipeline_ai.png`
- 推荐 skill: `scientific-schematics`
- 推荐比例 / 分辨率: `16:9`，建议 `1920x1080`
- 用途: 替换正文图 2，呈现 Focus3 的数据构造、校准门和分析流程。
- 正向 prompt:
  ```text
  publication-quality scientific flowchart, white background, horizontal pipeline layout, Chinese NLP robustness dataset construction workflow, source templates and scenario slots, control and perturbed pairing, calibration gate for semantic preservation and parse quality, Focus3 main set, five models times four prompt templates evaluation, scoring summary layer analysis and flip analysis, clean academic schematic, vector style, subtle blue orange accents, high contrast, minimal labels, publication ready, no prompt text
  ```
- Negative prompt:
  ```text
  watermark, photorealistic, 3d, cluttered background, dense paragraphs, layout instruction text, prompt leakage, low resolution, decorative arrows, unrelated charts
  ```
- 必须出现的元素:
  - 源模板 / 场景槽位
  - `control / perturbed` 配对
  - 校准门
  - Focus3 主集
  - 五模型四提示评测
  - scoring / flip / layer analysis
- 禁止出现的元素:
  - 大段说明文字
  - 复杂渐变背景
  - 与论文无关的插画元素

## 可选增强图

### 3. `noise_landscape.png`
- 目标路径: `paper/figures/manual/noise_landscape.png`
- 推荐 skill: `infographics`
- 推荐比例 / 分辨率: `4:3`，建议 `1800x1350`
- 用途: 做附加信息图，展示六类真实场景与三类噪声并置的“噪声景观”。
- 正向 prompt:
  ```text
  publication-quality infographic, real-world Chinese noisy text landscape, six panels for announcement, customer service, social media, email memo, instant message chat, form OCR, each panel shows semantically equivalent but visually perturbed Chinese text examples, highlight simplified-traditional variants, full-width half-width mixing, OCR confusable characters, flat vector poster style, white background, clean grid layout, subtle blue orange accents, colorblind-safe palette, minimal labels
  ```
- Negative prompt:
  ```text
  watermark, photorealistic, 3d, dense paragraphs, decorative icons, prompt leakage, layout instruction text, low resolution, unrelated charts
  ```

### 4. `graphical_abstract.png`
- 目标路径: `paper/figures/manual/graphical_abstract.png`
- 推荐 skill: `generate-image`
- 推荐比例 / 分辨率: `2:1`，建议 `2048x1024`
- 用途: 作为封面式概念图或附录附加图，不阻塞主 PDF。
- 正向 prompt:
  ```text
  clean AI conference style graphical abstract, Chinese NLP robustness study, real noisy text from OCR chat social email form flows into five large language models, outputs structured extraction and factual classification, highlight normalization gap in simplified-traditional characters, full-width half-width numbers, OCR confusable characters, white background, vector-like flat design, high contrast, colorblind-safe palette, minimal labels, publication quality, do not include any text showing the prompt or instructions
  ```
- Negative prompt:
  ```text
  watermark, photorealistic, 3d, cluttered background, dense paragraphs, decorative icons, glossy gradients, extra labels, prompt leakage, layout instruction text, low resolution
  ```

## 接入说明
- `problem_framework_ai.png` 和 `data_pipeline_ai.png` 对应正文前两张方法图。
- 建议优先生成前两张必做图；后两张属于增强项，不是交付阻塞项。
