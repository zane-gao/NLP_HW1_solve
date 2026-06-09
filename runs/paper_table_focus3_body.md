### 3.4 Focus3 跨模型初筛结果

| subtype_id | model_id | prompt_id | total_pairs | flip_pairs | delta_pp | representative_pair_id |
| --- | --- | --- | --- | --- | --- | --- |
| full_half_width | DeepSeek-V3.2 | P1 | 4 | 0 | 0.0000 |  |
| full_half_width | DeepSeek-V3.2 | P2 | 4 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P1 | 3 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P2 | 4 | 0 | 0.0000 |  |
| full_half_width | gpt-5.2 | P1 | 4 | 1 | 25.0000 | pair_cls_full_half_width_001 |
| full_half_width | gpt-5.2 | P2 | 4 | 1 | 25.0000 | pair_cls_full_half_width_001 |
| minor_typo | DeepSeek-V3.2 | P1 | 4 | 0 | 0.0000 |  |
| minor_typo | DeepSeek-V3.2 | P2 | 4 | 0 | 0.0000 |  |
| minor_typo | gemini-3-flash | P1 | 3 | 0 | 0.0000 |  |
| minor_typo | gemini-3-flash | P2 | 4 | 0 | 0.0000 |  |
| minor_typo | gpt-5.2 | P1 | 4 | 1 | 25.0000 | pair_ex_minor_typo_002 |
| minor_typo | gpt-5.2 | P2 | 4 | 1 | 25.0000 | pair_ex_minor_typo_002 |
| simp_trad | DeepSeek-V3.2 | P1 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |
| simp_trad | DeepSeek-V3.2 | P2 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |
| simp_trad | gemini-3-flash | P1 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |
| simp_trad | gemini-3-flash | P2 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |
| simp_trad | gpt-5.2 | P1 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |
| simp_trad | gpt-5.2 | P2 | 4 | 1 | 25.0000 | pair_ex_simp_trad_003 |

- 在当前 `GPT-5.2`、`gemini-3-flash`、`DeepSeek-V3.2` 三模型对照下，`simp_trad` 继续稳定复现，说明简繁混排导致的字段规范化缺失具有跨模型一致性。
- `minor_typo` 与 `full_half_width` 目前仍停留在 `gpt-5.2` 单模型现象，还不足以作为稳定跨模型机制下结论。

### 4.1 代表性翻转样例

| subtype_id | pair_id | 控制句 | 扰动句 | 模型输出 | 机制解释 |
| --- | --- | --- | --- | --- | --- |
| full_half_width | pair_cls_full_half_width_001 | 社媒原文：社媒转发：有人贴出截图称长风教育在2026年09月09日拿到800万元融资（AX1296），评论区提到资金用于算法研发。<br>复述断言：长风教育在2026-09-09完成了800万元融资。<br>请判断：支持/不支持。 | 社媒原文：社媒转发：有人贴出截图称长风教育在２02６年０９月0９日拿到８０0万元融资（ＡＸ1２96），评论区提到资金用于算法研发。<br>复述断言：长风教育在２０２６-０９-0９完成了８００万元融资。<br>请判断：支持/不支持。 | {"label":"不支持"} | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| minor_typo | pair_ex_minor_typo_002 | 客服会话节选：关于澄明支付融资，坐席确认“在2026年02月05日完成1800万元，追踪号AX4145，用途合规投入”。 | 客服会话节选：关于澄明支付融姿，坐席确认“在2026年02月05日完成1800万元，追踪号AX4145，用途合规投入”。 | {"company":"澄明支付融姿","date":"2026-02-05","amount":"1800万元"} | 轻微错别字触发了实体边界扩张，业务词被模型并入 company 字段。 |
| simp_trad | pair_ex_simp_trad_003 | 社媒转发：有人贴出截图称蓝海数据在2026年03月09日拿到2000万元融资（AX3294），评论区提到资金用于市场投放。 | 社媒轉发：有人贴出截图称蓝海数據在2026年03月09日拿到2000万元融资（AX3294），评论区提到資金用於市场投放。 | {"company":"蓝海数據","date":"2026-03-09","amount":"2000万元"} | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |

- 固定 8 条案例完整表放入附录。
