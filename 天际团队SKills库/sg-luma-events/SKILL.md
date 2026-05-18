---
name: sg-luma-events
description: >
  追踪新加坡 Luma 平台（lu.ma）上与 Family Office、募资、AI、科技、VC/PE
  及科技大厂相关的活动。当用户提到"新加坡 Luma 活动"、"抓取 Luma"、
  "新加坡活动周报"、"Luma events"、"新加坡 AI 活动"、"新加坡家办活动"、
  "新加坡募资活动"等关键词时触发。支持按主题与机构关键词筛选，输出结构化
  周报，可选择自动通过飞书推送。
---

# Singapore Luma Events Tracker

追踪新加坡 Luma 平台上与 Family Office、募资、AI、科技、大厂相关的活动。

## 触发条件

当用户提到以下关键词时触发：

- "新加坡 Luma 活动"
- "抓取 Luma"
- "新加坡活动周报"
- "Luma events"
- "新加坡 AI 活动" / "新加坡家办活动" / "新加坡募资活动"

## 追踪范围

### 主题

- Family Office / 家族办公室
- Fundraising / 募资
- AI / Artificial Intelligence
- Technology / 科技
- Venture Capital / VC
- Private Equity / PE

### 目标公司 / 机构

- Google
- ByteDance / 字节跳动
- Alibaba / 阿里巴巴
- Tencent / 腾讯
- Mistral AI
- OpenAI
- Manus
- Genspark
- Microsoft, Meta, Apple, Amazon, NVIDIA 等科技大厂

## 执行流程

1. 访问 https://lu.ma 新加坡地区活动
2. 搜索相关关键词
3. 筛选匹配的活动
4. 提取活动详情
5. 生成周报

## 输出示例

```markdown
# 🇸🇬 新加坡 Luma 活动周报 (2024-XX-XX)

## 📊 本周概览

- 发现活动总数: 15
- 高相关度活动: 5

## 🔥 重点推荐

### 🤖 AI & 科技

**AI Summit Singapore 2024**
- 📅 时间: 2024-XX-XX 18:00
- 📍 地点: Singapore
- 🏢 主办方: Tech Community
- 🔗 链接: [查看详情](https://lu.ma/xxx)
- 📝 描述: 聚焦 AI 前沿技术和应用
- 🎯 匹配关键词: AI, Technology

### 💰 募资 & 投资

**Family Office Investment Forum**
- 📅 时间: 2024-XX-XX 14:00
- 📍 地点: Marina Bay
- 🏢 主办方: Private Wealth Group
- 🔗 链接: [查看详情](https://lu.ma/xxx)
- 📝 描述: 家族办公室投资策略分享
- 🎯 匹配关键词: Family Office, Investment
```

## 自动化

设置 cron 每周日自动执行：

```cron
0 10 * * 0 /root/.openclaw/workspace/skills/sg-luma-events/scrape.sh
```

生成报告后通过 Feishu 发送给用户。
