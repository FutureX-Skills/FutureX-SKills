# Security & License Review

## 审计日期

2026-06-04

## 审计范围

本次只审计以下文件类型和目录：

- `AGENTS.md`
- `README.md`
- `.gitignore`
- `skills/*.md`
- `tasks/*.md`
- `references/*.md`（当前不存在）

未读取、未审计、不得提交：

- `data/`
- `outputs/`
- `references/*.docx`
- 任何 PDF、PPTX、DOCX、XLSX、CSV、JSON、`.env`、secrets 或 credentials 文件

## 可安全提交的文件

在本次审计范围内，以下文件经修复后可提交到公司 GitHub 私有仓库：

- `AGENTS.md`
- `README.md`
- `.gitignore`
- `docs/security-review.md`
- `skills/claims-verification.md`
- `skills/market-map.md`
- `skills/memo-to-ic.md`
- `skills/paper-analysis.md`
- `skills/patent-analysis.md`
- `skills/pitch-deck-screening.md`
- `skills/product-feedback-analysis.md`
- `skills/risk-memo.md`
- `skills/startup-onepager.md`
- `skills/technical-dd.md`
- `tasks/claims-verification-task.md`
- `tasks/market-map-task.md`
- `tasks/memo-to-ic-task.md`
- `tasks/pitch-deck-screening-task.md`
- `tasks/risk-memo-task.md`
- `tasks/startup-onepager-task.md`
- `tasks/technical-dd-task.md`

## 需要排除的文件

以下文件或目录不应提交：

- `data/*`
- `outputs/*`
- `references/*.docx`
- `*.pdf`
- `*.pptx`
- `*.docx`
- `*.xlsx`
- `*.csv`
- `*.json`
- `.env`
- `*.env`
- `secrets.*`
- `*_secret*`
- `*_credentials*`
- `desktop.ini`

允许保留：

- `data/.gitkeep`
- `outputs/.gitkeep`

## 敏感信息风险清单

| 风险项 | 审计结果 | 处理 |
|---|---|---|
| 真实公司 BP 内容 | 审计范围内未发现真实 BP 内容。 | 无需修改。 |
| 真实客户名称 | 审计范围内未发现真实客户名称。 | 无需修改。 |
| 创始人私人信息 | 未发现邮箱、手机号、私人身份信息。 | 无需修改。 |
| 投资金额、cap table、交易条款 | 未发现真实项目条款；模板中仅保留通用风险描述。 | 无需修改。 |
| 会议纪要、内部评价、未公开交易信息 | 未发现真实内容。 | 无需修改。 |
| README 示例路径 | 原示例使用了具体样例文件名。 | 已改为 `data/[company_deck].pdf` 和 `outputs/company-one-pager/[company_name].md`。 |
| tasks 模板路径 | 原模板使用 `<project>` 等通用占位符，未见真实项目；为统一格式已改为方括号占位符。 | 已改为 `[project]`、`[company_deck]`、`[company_name]` 等。 |

## 外部 Prompt / Skill 版权与许可风险

| 检查项 | 审计结果 | 处理 |
|---|---|---|
| 是否直接复制外部 Prompt 原文 | 未发现整段外部 prompt、system prompt 或 user prompt 原文。 | 无需删除。 |
| 是否标注灵感来源 | 原 Skill 未统一标注来源灵感。 | 已为每个 `skills/*.md` 增加 `Source inspiration`。 |
| 是否本地化改写 | Skill 内容为 FutureX VC 投研语境，采用中文、Claim 核验、保密和投研输出格式。 | 已保留。 |
| 是否可能存在许可证合规问题 | 当前仅保留方法启发，不保留外部原文句式；仍建议法务按公司政策确认外部项目引用方式。 | 需人工确认。 |

## Prompt Injection / 越权指令检查

已在审计范围内搜索以下风险词：

- `ignore previous instructions`
- `bypass`
- `reveal system prompt`
- `exfiltrate`
- `upload`
- `send to external`
- `delete`
- `rm -rf`
- `curl`
- `wget`
- `token`
- `API key`
- `password`
- `secret`

结果：未发现要求 Agent 忽略规则、泄露系统提示、上传数据、删除文件、调用外部服务或读取无关目录的英文越权指令。

已修复/补强：

- 每个 Skill 都明确要求遵守 `AGENTS.md`。
- 每个 Skill 都明确禁止上传、外发或复制原始文件内容到外部服务。
- 每个 Skill 都明确要求信息不足时标记「信息不足 / 待验证」。

## `.gitignore` 检查

已确认并补齐以下忽略规则：

- `data/*`
- `outputs/*`
- `*.pdf`
- `*.pptx`
- `*.docx`
- `*.xlsx`
- `*.csv`
- `*.json`
- `.env`
- `*.env`
- `secrets.*`
- `*_secret*`
- `*_credentials*`

并保留：

- `!data/.gitkeep`
- `!outputs/.gitkeep`

额外补充：

- `desktop.ini`

## 已修复的问题

- 将 README 中的具体样例路径改为通用占位符。
- 将 `tasks/*.md` 中路径和上下文字段统一改为占位符格式。
- 补齐 `.gitignore` 中缺失的敏感文件类型。
- 每个 Skill 增加安全限制：不得编造数据、不得把公司自述当事实、不得泄露敏感材料、不得上传/外发原始内容、信息不足必须标记。
- 每个 Skill 增加 `Source inspiration`，说明仅为灵感来源，已为 FutureX VC 投研流程改写，未复制外部 Prompt 原文。

## 仍需人工确认的问题

- 外部灵感来源涉及 Fabric、GitHub Awesome Copilot 等公开项目；当前仓库未复制原文，但建议法务或仓库 owner 确认公司内部对“Inspired by”标注的合规偏好。
- `references/VC_Top30_Agent_Skills_Codex_clean.docx` 不在本次审计范围内，且应被 `.gitignore` 排除；如需要提交参考材料，应先转成脱敏、可授权的 Markdown 摘要。
- 本次未读取 `data/` 和 `outputs/`，因此不能对其中真实材料作安全结论；这些目录必须继续排除。
- `desktop.ini` 当前已被 Git 跟踪；`.gitignore` 已补规则，但仍需要人工运行 `git rm --cached desktop.ini` 才能从后续提交中排除。

## 最终建议

Needs manual review

前提：

- 只提交本报告列出的可安全提交文件。
- 不提交 `data/`、`outputs/`、`references/*.docx` 或任何被 `.gitignore` 排除的敏感文件。
- 先人工确认并处理已跟踪的 `desktop.ini`。
- 如公司要求严格许可证审查，请先让法务确认 `Source inspiration` 标注方式。
