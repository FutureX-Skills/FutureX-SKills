# 公众号排版助手（wechat-formatter）

把文章排版成微信公众号可直接使用的 **.docx 成品**：在 Word 里全选 → 复制 → 粘贴进公众号编辑器即可，样式完整保留。

**为什么是 DOCX 而不是 HTML？** 微信编辑器粘贴时会过滤掉所有 `<style>` 标签和 `class` 属性，HTML 排版会完全失效；Word 富文本粘贴进微信能完整保留，这是目前唯一可靠的方案。

## v2.0 特性

- **8 套预设配色**：Wood（默认）/ Ink / Ocean / Vermilion / Mist / Forest / Violet / Amber
- **封面图自动配色**：上传封面图自动匹配最贴近的方案，或提取主色生成定制配色
- **完整组件库**：Hero 块 · 导读块 · 编号章节标题 · 金句块 · 重点段落 · 关键词高亮 · 关键数字下划线 · 三栏概念表 · 两列要点表 · 来源注释 · Footer
- **排版分析流程**：自动划分章节、提炼金句、标注关键词与关键数字、估算阅读时长
- **踩坑清单 + 质量核查表**：表格列宽、shading、中文引号转义等约束一次说清

## 使用方法

1. 把文章发给 Claude，触发词："排版 / 做成公众号 / 转换成公众号格式"等
2. 选择配色方案（或上传封面图自动匹配）
3. Claude 用 `docx` 库生成 `.docx`
4. 在 Word 中全选复制，粘贴进公众号后台

> 依赖：`npm install docx`

## 一键安装

```bash
curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/futurex-skills/main/公众号排版助手/install.sh | bash
```
