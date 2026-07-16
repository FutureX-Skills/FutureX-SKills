# FutureX 创意排版（fx-wechat-formatter）

将 Markdown 转为可直接粘贴到微信公众号编辑器的 `.docx`。这套「电表」设计系统提供琥珀、青金、炭橙、雾青四套配色，以及眉头、章节编号、仪表读数、金句引块和 CTA 等组件。

适用于希望获得更杂志化、机构化视觉风格的公众号文章。只说「排版」而未指定风格时，建议使用默认的 `公众号排版助手`；明确要求创意、电表或杂志化排版时使用本 Skill。

## 使用方法

将文章标记为本 Skill 的 Markdown 方言后执行：

```bash
node scripts/build_docx.js input.md amber output.docx
```

其中配色可选 `amber`、`sage`、`ember` 或 `frost`。生成后请在 Word 中全选复制，粘贴进微信公众号编辑器，并预览确认移动端效果。

## 一键安装

```bash
curl -fsSL "https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/天际团队SKills库/fx-wechat-formatter/install.sh" | bash
```
