---
name: podcast-post-production
description: "Bilingual (Chinese/English) podcast post-production pipeline. 播客后期全套工具，将原始文字稿转换为多平台适配内容。触发词：文字稿、播客后期、切片、图文、show notes等。适用于公众号、小红书、B站、YouTube、TikTok、Instagram等平台。"
---

# Podcast Post-Production Pipeline

双语播客后期技能，将原始文字稿转换为各平台适配的可发布内容，支持中文平台（公众号、小红书、B站、视频号）和国际平台（YouTube、Spotify、TikTok、Instagram）。

## 触发场景

- 用户上传或粘贴播客文字稿（来自飞书妙记、Whisper、Descript 等 ASR 工具）
- 提到"处理文字稿"、"后期流程"、"生成 show notes"、"做切片"、"各平台文案"
- 要求清理、翻译或重新利用播客内容
- 提及任何集数（如"EP01"、"第二期"）

## 完整流程（6个阶段）

用户可请求单个阶段或完整流程，开始前先确认需要哪些阶段。

### Stage 1: Transcript Cleanup — 文字稿清理

**输入**：原始 ASR 文字稿（.docx 或 .txt，来自飞书妙记/Whisper）
**输出**：清洁的带时间码 Markdown 文字稿

**步骤：**
1. 用 pandoc 提取文本（.docx → markdown）
2. 建立错字纠正表（ASR 常见错误模式）
3. 自动化清理脚本（Python）
4. 人工复核（首尾 50 行、章节过渡、人名/产品名）

### Stage 2: Analysis & Extraction — 分析与提取

**输入**：清理后的文字稿
**输出**：分析工作文档，含 5 个部分

- **Topic Segment Map**：每章节时间范围、摘要、发言者
- **Quote Extraction**：15-20 个金句（洞察/故事/框架/梗）
- **Clip Suggestions**：10-15 个切片建议（含标题、时间码、推荐平台、传播潜力）

### Stage 3: English Translation — 英文翻译

**输入**：清洁的中文文字稿
**输出**：自然口语化英文版本（非正式书面语）

### Stage 4: Subtitle Generation — 字幕生成

**输入**：时间码
**输出**：中英双语 SRT 字幕文件

### Stage 5: Platform Copy Package — 多平台文案包

**输出**：每个平台的标题、描述、标签、话题标签

| 平台 | 内容类型 |
|------|---------|
| 微信公众号 | 长文版文章 |
| 小红书 | 图文帖子 |
| B站/视频号 | 视频描述 |
| YouTube | 标题、描述、标签、章节 |
| TikTok | 短视频文案 |
| Instagram | 配文+话题标签 |

### Stage 6: Long-form Content — 长内容生成

**输出**：Show notes、公众号文章、博客帖子

## 输出格式

### 清理后文字稿格式
```markdown
# [Show Name] [Episode] — 清理版文字稿

> **节目：**[Show name]
> **集数：**[Episode number]
> **嘉宾：**[Guest name and title]
> **主持：**[Host names]
> **录制时间：**[Date]
> **总时长：**[Duration after cuts]

---

## Part 1: [Topic title]
[Speaker] [HH:MM:SS]
[Cleaned text...]

## Part 2: [Topic title]
...
```

### 切片建议格式
每个切片包含：
- **标题/钩子**（中英双语）
- **时间码**（起止）
- **推荐平台**（抖音/TikTok、YouTube Shorts、小红书、B站、IG Reels）
- **传播潜力分析**（争议性/情感/实用性/幽默）
- **预估时长**
- **分类**：高传播性 / 实用性/教育性 / 垂直/生活方式
