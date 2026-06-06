# FutureX VC Skills

这是 FutureX 内部 VC Agent Skills 仓库，用于沉淀可复用的投研 Agent 工作流。仓库中的 Skill 是 Markdown 指令资产，服务于项目初筛、Claim 核验、赛道研究、技术尽调、风险 memo、投委会材料和投后研究等场景。

本仓库默认中文输出，并坚持证据导向：不编造公司数据，不把公司自述当成事实，所有未经验证的信息必须标记为「待验证」。

## 目录结构

- `AGENTS.md`：仓库级总控规则，定义 FutureX VC 投研 Agent 的角色、证据分级、保密规则和输出原则。
- `skills/`：可复用 Skill 指令，每个文件对应一个投研工作流。
- `tasks/`：可直接复制给 Codex 执行的任务模板，适合处理具体项目或具体材料。
- `data/`：本地输入材料目录。真实 BP、访谈纪要、财务底稿、客户名单等敏感资料不应提交。
- `outputs/`：本地输出目录。真实项目分析结果、内部判断和未公开信息不应提交。
- `references/`：内部参考材料，用于生成和维护本仓库的 Skill。

## 如何调用一个 Skill

在 Codex 中说明要使用的 Skill、输入材料路径和输出目标即可。建议格式：

```text
请按照 skills/[skill_name].md 的流程，分析 data/[input_file]，
并将结果输出到 outputs/[project_name]/[artifact_name].md。
```

如果材料来自多个来源，请同时说明来源类型，例如「BP」「官网摘录」「访谈纪要」「第三方报道」「内部会议记录」。Codex 输出时必须区分「已验证事实」「公司自述」「第三方报道」「推测/判断」和「待验证」。

## Pitch Deck Screening 示例

把待分析 BP 放在本地 `data/` 目录，例如：

```text
data/[company_deck].pdf
```

然后让 Codex 执行：

```text
请按照 skills/pitch-deck-screening.md 的流程，分析 data/[company_deck].pdf。
请输出中文初筛结论，并保存到 outputs/company-one-pager/[company_name].md。
所有收入、客户数量、融资金额、估值、市场规模和技术指标，如未在材料中被可靠证据支持，必须标记为「待验证」。
```

推荐先用脱敏或样例材料测试，不要把真实敏感文件提交到仓库。

## 第一批高优先级 Skills

- `pitch-deck-screening.md`：BP 初筛，输出一页纸结论、风险与追问。
- `claims-verification.md`：抽取并核验公司关键 Claim。
- `risk-memo.md`：系统化识别项目风险和缓释动作。
- `market-map.md`：构建赛道图谱、价值链和竞品分层。
- `startup-onepager.md`：生成投资团队可快速阅读的公司 One-Pager。
- `technical-dd.md`：面向技术型项目的技术尽调。
- `memo-to-ic.md`：将研究材料组织为投委会 memo。
- `product-feedback-analysis.md`：从用户反馈中提取 PMF 信号。
- `paper-analysis.md`：拆解论文或技术白皮书的投资含义。
- `patent-analysis.md`：分析专利保护范围、壁垒和风险。

## 安全与保密规则

- 不提交真实敏感材料到 `data/`、`outputs/` 或其他仓库目录。
- 不提交真实 BP、PDF、PPTX、DOCX、XLSX、客户名单、财务底稿、合同、访谈纪要或内部 memo。
- 输出示例使用虚构公司、脱敏字段或占位符。
- 不编造经营数据、融资金额、估值、市场规模、客户数量、收入、技术指标或创始人履历。
- 对 BP、官网、访谈和销售材料中的信息，默认标记为「公司自述」，除非有可靠证据支持。
- 所有未经验证的信息必须标记为「待验证」，并给出下一步核验动作。

## 维护方式

每次用 Skill 处理真实项目后，可以把新的检查项、风险模式、输出格式优化沉淀回对应 `skills/*.md`。更新时只保留通用方法论、脱敏示例和内部格式，不写入真实项目敏感信息。
