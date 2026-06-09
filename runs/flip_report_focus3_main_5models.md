# Focus3 翻转分析表

## 表 1：跨模型触发概览
| subtype_id | model_id | prompt_id | total_pairs | flip_pairs | delta_pp | representative_pair_id |
| --- | --- | --- | --- | --- | --- | --- |
| full_half_width | DeepSeek-V3.2 | P1 | 30 | 1 | 3.3333 | pair_main_ext_full_half_width_077 |
| full_half_width | DeepSeek-V3.2 | P2 | 30 | 1 | 3.3333 | pair_main_ext_full_half_width_077 |
| full_half_width | DeepSeek-V3.2 | P3 | 30 | 1 | 3.3333 | pair_main_ext_full_half_width_066 |
| full_half_width | DeepSeek-V3.2 | P4 | 30 | 2 | 0.0000 | pair_main_ext_full_half_width_072 |
| full_half_width | GLM-4.6 | P1 | 30 | 1 | 3.3333 | pair_main_ext_full_half_width_082 |
| full_half_width | GLM-4.6 | P2 | 30 | 0 | -3.3333 |  |
| full_half_width | GLM-4.6 | P3 | 30 | 3 | 10.0000 | pair_main_ext_full_half_width_067 |
| full_half_width | GLM-4.6 | P4 | 30 | 2 | 6.6667 | pair_main_ext_full_half_width_061 |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P1 | 30 | 1 | 3.3333 | pair_main_ext_full_half_width_084 |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P2 | 30 | 0 | 0.0000 |  |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P3 | 30 | 1 | 0.0000 | pair_main_ext_full_half_width_076 |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P4 | 30 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P1 | 22 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P2 | 29 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P3 | 30 | 0 | 0.0000 |  |
| full_half_width | gemini-3-flash | P4 | 29 | 0 | 0.0000 |  |
| full_half_width | gpt-5.2 | P1 | 30 | 0 | -3.3333 |  |
| full_half_width | gpt-5.2 | P2 | 30 | 0 | -3.3333 |  |
| full_half_width | gpt-5.2 | P3 | 30 | 0 | 0.0000 |  |
| full_half_width | gpt-5.2 | P4 | 30 | 0 | -6.6667 |  |
| ocr_confusable | DeepSeek-V3.2 | P1 | 30 | 14 | 46.6667 | pair_main_ext_ocr_confusable_092 |
| ocr_confusable | DeepSeek-V3.2 | P2 | 30 | 18 | 60.0000 | pair_main_ext_ocr_confusable_092 |
| ocr_confusable | DeepSeek-V3.2 | P3 | 30 | 13 | 43.3333 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | DeepSeek-V3.2 | P4 | 30 | 15 | 50.0000 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | GLM-4.6 | P1 | 30 | 16 | 53.3333 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | GLM-4.6 | P2 | 30 | 16 | 53.3333 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | GLM-4.6 | P3 | 30 | 13 | 43.3333 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | GLM-4.6 | P4 | 30 | 15 | 46.6667 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | 30 | 19 | 63.3333 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | 30 | 19 | 63.3333 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | 30 | 16 | 53.3333 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | 30 | 18 | 60.0000 | pair_main_ext_ocr_confusable_091 |
| ocr_confusable | gemini-3-flash | P1 | 25 | 15 | 60.0000 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | gemini-3-flash | P2 | 29 | 13 | 44.8276 | pair_main_ext_ocr_confusable_094 |
| ocr_confusable | gemini-3-flash | P3 | 30 | 15 | 50.0000 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | gemini-3-flash | P4 | 30 | 15 | 46.6667 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | gpt-5.2 | P1 | 30 | 18 | 56.6667 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | gpt-5.2 | P2 | 30 | 19 | 63.3333 | pair_main_ext_ocr_confusable_092 |
| ocr_confusable | gpt-5.2 | P3 | 30 | 16 | 53.3333 | pair_main_ext_ocr_confusable_093 |
| ocr_confusable | gpt-5.2 | P4 | 30 | 16 | 50.0000 | pair_main_ext_ocr_confusable_093 |
| simp_trad | DeepSeek-V3.2 | P1 | 60 | 23 | 36.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | DeepSeek-V3.2 | P2 | 60 | 25 | 41.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | DeepSeek-V3.2 | P3 | 60 | 27 | 43.3333 | pair_main_ext_simp_trad_001 |
| simp_trad | DeepSeek-V3.2 | P4 | 60 | 24 | 40.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | GLM-4.6 | P1 | 60 | 29 | 43.3333 | pair_main_ext_simp_trad_001 |
| simp_trad | GLM-4.6 | P2 | 60 | 28 | 46.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | GLM-4.6 | P3 | 60 | 27 | 45.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | GLM-4.6 | P4 | 60 | 29 | 48.3333 | pair_main_ext_simp_trad_001 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | 60 | 28 | 46.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | 60 | 28 | 46.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | 60 | 26 | 43.3333 | pair_main_ext_simp_trad_001 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | 60 | 28 | 46.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | gemini-3-flash | P1 | 58 | 27 | 46.5517 | pair_main_ext_simp_trad_001 |
| simp_trad | gemini-3-flash | P2 | 60 | 27 | 45.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | gemini-3-flash | P3 | 60 | 27 | 45.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | gemini-3-flash | P4 | 60 | 28 | 45.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | gpt-5.2 | P1 | 60 | 28 | 45.0000 | pair_main_ext_simp_trad_001 |
| simp_trad | gpt-5.2 | P2 | 60 | 26 | 43.3333 | pair_main_ext_simp_trad_001 |
| simp_trad | gpt-5.2 | P3 | 60 | 26 | 41.6667 | pair_main_ext_simp_trad_001 |
| simp_trad | gpt-5.2 | P4 | 60 | 25 | 40.0000 | pair_main_ext_simp_trad_001 |

## 表 2：代表性错误个案
| subtype_id | model_id | prompt_id | pair_id | task_type | trigger_shape | perturbed_error_type | trigger_explanation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| full_half_width | DeepSeek-V3.2 | P1 | pair_main_ext_full_half_width_077 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | DeepSeek-V3.2 | P2 | pair_main_ext_full_half_width_077 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | DeepSeek-V3.2 | P3 | pair_main_ext_full_half_width_066 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | DeepSeek-V3.2 | P4 | pair_main_ext_full_half_width_072 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | DeepSeek-V3.2 | P4 | pair_main_ext_full_half_width_077 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P1 | pair_main_ext_full_half_width_082 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P3 | pair_main_ext_full_half_width_067 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P3 | pair_main_ext_full_half_width_072 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P3 | pair_main_ext_full_half_width_082 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P4 | pair_main_ext_full_half_width_061 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | GLM-4.6 | P4 | pair_main_ext_full_half_width_072 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_full_half_width_084 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| full_half_width | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_full_half_width_076 | extraction | mixed_width_numeric_field | mismatch_company | 数值或编号字段中的全半角混排破坏了事实匹配，导致答案翻转。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_company_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P1 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_097 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_099 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_company_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_107 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_company_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_company_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_117 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P2 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_cla_ocr_confusable_110 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_company_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P3 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_company_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_107 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | DeepSeek-V3.2 | P4 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_cla_ocr_confusable_120 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_117 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P1 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_cla_ocr_confusable_120 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_117 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P2 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_097 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_company_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P3 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_117 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | GLM-4.6 | P4 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_112 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_112 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_091 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_112 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_cla_ocr_confusable_110 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P1 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P2 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P3 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gemini-3-flash | P4 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_cla_ocr_confusable_110 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_097 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_099 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_107 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P1 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_092 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_097 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_099 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_102 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P2 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_cla_ocr_confusable_110 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_106 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_108 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P3 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_cla_ocr_confusable_120 | classification | ocr_confusion_near_key_slot | label_mismatch | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_093 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_094 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_096 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_097 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_098 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_099 | extraction | ocr_confusion_near_key_slot | mismatch_date | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_101 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_103 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_104 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_109 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_111 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_113 | extraction | ocr_confusion_near_key_slot | mismatch_amount | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_116 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_118 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| ocr_confusable | gpt-5.2 | P4 | pair_main_ext_ocr_confusable_119 | extraction | ocr_confusion_near_key_slot | mismatch_company | OCR 易混字符落在关键槽位附近，模型未完成必要的字符归一化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_016 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P1 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_012 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_047 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P2 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_012 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_014 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_016 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_032 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_036 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_053 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P3 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_012 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | DeepSeek-V3.2 | P4 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_007 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_012 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_036 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P1 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_007 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_028 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_032 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P2 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_013 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_055 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P3 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_012 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_025 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_028 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | GLM-4.6 | P4 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_044 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P1 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_044 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P2 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P3 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_034 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_044 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | Qwen3-235B-A22B-Instruct-2507 | P4 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P1 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P2 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_013 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P3 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_016 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gemini-3-flash | P4 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_013 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_032 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P1 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_013 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_026 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P2 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_013 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_042 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_046 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P3 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_001 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_002 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_003 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_004 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_006 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_007 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_008 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_013 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_022 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_023 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_024 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_025 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_027 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_028 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_033 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_037 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_041 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_043 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_045 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_051 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_053 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_055 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_056 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_057 | extraction | manual_review_needed | mismatch_company | 无法由当前规则稳定归因 |
| simp_trad | gpt-5.2 | P4 | pair_main_ext_simp_trad_058 | extraction | script_variant_preserved | mismatch_company | 模型保留了简繁字形变体而未做规范化，导致字段级精确匹配失败。 |
