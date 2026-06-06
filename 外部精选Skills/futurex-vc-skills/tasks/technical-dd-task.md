# Task: Technical DD

## 使用 Skill

请先读取 `skills/technical-dd.md`，并严格按照其中的步骤和输出格式执行。

## 输入材料

- 技术文档：`data/[project]/[tech_docs]`
- 代码库路径：`[local_repo_path_or_NA]`
- 架构图、API 文档、benchmark 或演示材料：`data/[project]/[files]`
- CTO/技术团队访谈：`data/[project]/[notes]`

## 执行要求

1. 提取所有技术 Claim，并标记来源类型和证据状态。
2. 如有代码库，先阅读 README、目录结构、依赖、测试和核心模块。
3. 区分技术新颖性、工程成熟度和商业壁垒。
4. 对无法复现的性能、模型、成本、安全和扩展性指标标记「待验证」。
5. 输出下一步技术尽调清单。

## 输出路径

请保存到：

```text
outputs/[project]/technical-dd.md
```

## 保密检查

- 不泄露代码、密钥、漏洞、客户数据或未公开架构细节。
- 不把公司演示或 benchmark 当作已验证事实。
- 不编造技术指标或审计结论。
