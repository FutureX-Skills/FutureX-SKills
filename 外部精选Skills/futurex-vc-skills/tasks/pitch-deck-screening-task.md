# Task: Pitch Deck Screening

## 使用 Skill

请先读取 `skills/pitch-deck-screening.md`，并严格按照其中的步骤和输出格式执行。

## 输入材料

- BP 或项目介绍：`data/[company_deck].pdf`
- 补充材料：`data/[project]/[supplemental_files]`
- 已知背景：`[project_source_referrer_meeting_context_key_questions]`

## 执行要求

1. 默认中文输出。
2. 先列出输入材料清单，并标记来源类型。
3. 抽取收入、客户数量、融资金额、估值、市场规模、技术指标等高影响 Claim。
4. 所有未经验证的信息必须标记为「待验证」。
5. 公司 BP、官网、创始人访谈和销售材料中的信息默认标记为「公司自述」。
6. 给出初筛建议、关键风险、下次会议问题和缺失材料。

## 输出路径

请保存到：

```text
outputs/company-one-pager/[company_name].md
```

## 保密检查

- 不要把真实 BP、PDF、PPTX、DOCX、XLSX 或客户名单提交到仓库。
- 输出如包含真实公司敏感信息，只能保存在本地 `outputs/`。
- 提交仓库前必须脱敏或替换为占位符。
