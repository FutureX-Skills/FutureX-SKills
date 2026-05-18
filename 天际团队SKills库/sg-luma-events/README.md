# Singapore Luma Events Tracker

> 自动追踪新加坡 Luma 平台（lu.ma）上 Family Office、募资、AI、科技、VC/PE 及科技大厂相关活动，生成结构化周报。

**创建人：Angela**

---

## 适用场景

- 出差新加坡前快速锁定本地高价值活动
- 每周自动汇总新加坡 AI / 募资 / 家办活动，提前报名
- 跟踪 Google、字节、阿里、腾讯、OpenAI、Mistral、Manus 等大厂/明星公司在新加坡的活动出席动态
- 为 LP、被投企业、合作方提供新加坡活动情报

---

## 核心能力

### 1. 主题筛选

覆盖 Family Office、Fundraising、AI、Technology、VC、PE 六大主题，按关键词自动匹配。

### 2. 机构追踪

内置目标公司清单（Google / ByteDance / Alibaba / Tencent / Mistral / OpenAI / Manus / Genspark / Microsoft / Meta / Apple / Amazon / NVIDIA 等），自动识别相关主办或参与方。

### 3. 周报生成

按"概览 → 重点推荐 → 主题分类"结构输出 Markdown 报告，含时间、地点、主办方、链接、匹配关键词。

### 4. 自动化推送

可配置 cron 每周日自动抓取并通过飞书机器人推送。

---

## 触发关键词

- 新加坡 Luma 活动
- 抓取 Luma
- 新加坡活动周报
- Luma events
- 新加坡 AI 活动 / 新加坡家办活动 / 新加坡募资活动

---

## 一键安装

```bash
cd ~/.openclaw/workspace/FutureX-SKills
git pull origin main
cp -r 天际团队SKills库/sg-luma-events ~/.openclaw/workspace/skills/

# 或一步到位
cd ~/.openclaw/workspace/FutureX-SKills && git pull && cp -r 天际团队SKills库/sg-luma-events ~/.openclaw/workspace/skills/
```

---

## 使用方式

直接对话触发，例如：

- "帮我看看本周新加坡有什么 AI 活动"
- "生成新加坡 Luma 活动周报"
- "抓一下 lu.ma 上和家办相关的活动"
