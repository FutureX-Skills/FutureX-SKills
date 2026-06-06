# Task: Claims Verification

## 使用 Skill

请先读取 `skills/claims-verification.md`，并严格按照其中的步骤和输出格式执行。

## 输入材料

- 待核验材料：`data/[project]/[source_files]`
- 重点核验范围：`[市场规模 / 客户 / 收入 / 融资 / 技术 / 团队 / 其他]`
- 已有外部来源：`[link_or_file_path]`

## 执行要求

1. 将材料中的断言拆成单条可验证 Claim。
2. 标记来源类型：已验证事实、公司自述、第三方报道、推测/判断或待验证。
3. 对每条 Claim 判断证据强度：强 / 中 / 弱 / 冲突 / 无证据。
4. 对高影响 Claim 给出下一步核验动作。
5. 输出 P0/P1/P2 核验优先级。
6. 不要补写材料中没有的数据。

## 输出路径

请保存到：

```text
outputs/[project]/claims-verification.md
```

## 保密检查

- 不提交真实底稿、访谈纪要或客户资料。
- 不把公司自述当作已验证事实。
- 所有无法确认的信息保留「待验证」标记。
