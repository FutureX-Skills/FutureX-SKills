# FutureX Skills 知识库

> **天际资本（FutureX Capital）** 出品 | 全部开源 | 持续更新

---

## 📊 上线情况一览

| 类别 | 数量 | 说明 |
|------|------|------|
| 🔧 天际团队自建 Skills | 26 个 | 覆盖投研、内容、运营等多场景 |
| 🌐 外部精选 Skills | 28 个 | 李继刚 16 + qiaomu 1 + 43-Agent 10 + skill-creator 1 |
| ⭐ CEO 开源项目 | 1 个 | GPilot-Simon（独立展示） |
| **合计** | **~55 个** | 持续增加中 |

---

## 🎯 这是什么？

**FutureX Capital（天际资本）** 是一家专注于 AI 领域的早期投资机构，重点关注 AI Agent、AI 应用、AI 硬件及下一代智能基础设施。我们不仅提供资金支持，更通过内容传播、资源链接与社区构建，帮助创业者加速成长。

> 🌐 **开源与共享** — 我们坚信：工具开源，知识共享，才能推动整个 VC/PE 行业进入智能化时代。**FutureX Skills** 知识库完全开源，供创业者和行业同行免费使用。

天际团队会**不定期更新**新的 Skills，同时也会主动发掘和评测来自社区的优质 Skills，将其收入 **外部精选Skills** 库中推荐给大家。欢迎 Star 关注，持续跟踪最新工具。

---

## 🚀 如何安装

### 安装单个 Skill

每个 Skill 目录下都有独立的 `README.md`，其中包含该 Skill 的详细介绍和**一键安装命令**。

找到你想安装的 Skill → 进入其目录 → 复制 `README.md` 中的安装指令即可。

### 快速导航

| 需求场景 | 推荐 Skills |
|---------|------------|
| 生成投研报告、尽调报告 | `研报助手`、`硅谷季度报告`、`立项报告`、`PIB投研搜索` |
| 社交媒体内容创作 | `社媒营销`、`视频标题大师`、`LinkedIn内容助手`、`AI-VC推文助手` |
| 播客/内容生产 | `播客后期助手`、`公众号排版助手`、`AI内容写作助手` |
| 投资业务提效 | `投资-Memo`、`VC创始人会面准备`、`会议纪要整理助手`、`PE募资追踪器` |
| 运营与合规 | `费用报销合规检查`、`事项提醒`、`云Token监控`、`TODO任务追踪` |
| 外部精选工具 | `qiaomu-markdown-proxy`、`李继刚skills/`、`43-Agent-skills/` |

---

## ⭐ CEO 开源项目：GPilot-Simon

> **特别推荐** — 天际资本 CEO Simon 的心血之作

**GPilot-Simon** 是 Simon 独立开发的多智能体投资管理系统，也是本知识库的技术底座之一。

它是一个面向 VC/PE 投资人的 AI 原生工作流框架，包含：

- 🤖 **8个专用 Agent** — Deal Sourcer、Deep Researcher、Financial Analyst、Memo Writer …
- 📋 **19个投研命令** — IC Memo、Deal Screen、Research、Board Prep …
- 🗓️ **9个定时任务** — Morning Briefing、Portfolio News、Weekly Pipeline …
- 💼 **募资运营模块** — Fund Accounting、LP Reporting、Capital Call …
- 📊 **Next.js 管理面板** — Portfolio 全景可视化管理

👉 **项目地址：[ruiyang-xu/GPilot](https://github.com/ruiyang-xu/GPilot)**

如果你觉得 GPilot 有用，欢迎给个 Star ⭐

---

## 🌐 外部精选Skills

我们收录来自社区的优质开源 Skills，所有来源均标注原始仓库链接。

| 来源 | 仓库 | 内容 |
|------|------|------|
| **李继刚skills** | — | 16个认知/创作类 Skills（概念解剖、论文阅读、写作引擎等） |
| **43-Agent-skills** | [43COLLEGE/43-Agent-skills](https://github.com/43COLLEGE/43-Agent-skills) | 10个实用 Agent Skills（飞书助手、浏览器自动化、视频创作等） |
| **qiaomu-markdown-proxy** | [joeseesun/qiaomu-markdown-proxy](https://github.com/joeseesun/qiaomu-markdown-proxy) | URL → Markdown 转换（微信公众号/飞书/PDF/YouTube） |
| **skill-creator** | [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方 Skill 构建工具（分析器/比较器/评分器） |

> 收录标准：功能明确、维护活跃、与 AI/VC 业务高度相关。

---

## 📁 仓库结构

```
futurex-skills/
├── 外部精选Skills/          # 天际精选的优质开源 Skills，持续更新
│   ├── 李继刚skills/              # 李继刚老师 Skills 合集（16个）
│   │   ├── ljg-card               # 内容铸造成 PNG 海报/信息图
│   │   ├── ljg-paper              # 论文阅读（给普通人读的论文解析）
│   │   ├── ljg-paper-river        # 论文溯源（问题演化史）
│   │   ├── ljg-invest             # 投资分析报告
│   │   ├── ljg-learn              # 概念解剖（8维度）
│   │   ├── ljg-plain              # 说人话（12岁能懂的解释）
│   │   ├── ljg-rank               # 降秩分析（找不可再少的力）
│   │   ├── ljg-relationship       # 关系分析（结构诊断+精神分析）
│   │   ├── ljg-roundtable         # 圆桌辩论框架
│   │   ├── ljg-think              # 追本之箭（纵向深钻）
│   │   ├── ljg-travel             # 深度旅行研究
│   │   ├── ljg-word               # 英语单词深度掌握
│   │   ├── ljg-writes             # 写作引擎（写中想透）
│   │   └── ...（共16个）
│   │
│   ├── 43-Agent-skills        # 来源：[43COLLEGE/43-Agent-skills](https://github.com/43COLLEGE/43-Agent-skills)
│   │   ├── chat-archiver            # 聊天记录归档
│   │   ├── email-invoice-processor  # 邮件发票处理
│   │   ├── feishu-assistant         # 飞书助手
│   │   ├── find-skills              # 技能发现
│   │   ├── follow-builders          # 追踪创业者动态
│   │   ├── media-transcriber       # 媒体转录
│   │   ├── social-media-scout       # 社交媒体情报
│   │   ├── video-creator            # 视频创作（含完整规则集）
│   │   └── web-browser              # 浏览器自动化
│   │
│   ├── qiaomu-markdown-proxy  # 来源：[joeseesun/qiaomu-markdown-proxy](https://github.com/joeseesun/qiaomu-markdown-proxy)
│   │   └── SKILL.md                 # URL → Markdown（微信公众号/飞书/PDF/YouTube等）
│   │
│   └── skill-creator           # 来源：[anthropics/skills](https://github.com/anthropics/skills)
│       ├── agents/                   # Analyzer / Comparator / Grader
│       ├── scripts/                  # validate / package / run_eval 等
│       └── eval-viewer/              # 评估可视化工具
│
└── 天际团队SKills库/        # 天际资本团队自建 Skills（26个）
    ├── 研报助手                  # MoE 多智能体调度中心，生成投行级尽调报告
    ├── 视频标题大师              # 短视频封面标题与简介生成
    ├── 硅谷季度报告              # VC 赛道趋势分析报告（90天）
    ├── 社媒营销                  # LinkedIn/TikTok/Meta/YouTube/X 多平台内容
    ├── 社媒内容处理              # 图片水印/文字标注/视频拼接/尺寸适配
    ├── AI内容写作助手            # AI 行业热点深度长文（5000字+Word）
    ├── 公众号排版助手             # 微信公众号 HTML 排版
    ├── LinkedIn内容助手          # LinkedIn 短帖子+长文章生成
    ├── 播客后期助手              # 双语播客后期（文字稿→多平台适配内容）
    ├── 投资-Memo                 # VC 投资备忘录/Deal Memo 撰写
    ├── 立项报告                  # 中文 VC 立项报告撰写
    ├── 项目立项投资报告           # 标准立项框架生成完整投资报告
    ├── PE募资追踪器             # 全球 PE/VC 募资动态追踪+LP分析
    ├── PIB投研搜索              # 私募公司 VC 风格投研备忘录
    ├── VC创始人会面准备          # 创始人会面问题清单生成
    ├── 会议纪要整理助手           # 录音转文字→结构化会议纪要
    ├── 事项提醒                  # Excel生日列表→飞书日历年度提醒
    ├── 旅行规划助手              # 保姆级旅行规划（小白友好）
    ├── 语音合成助手              # TTS 多模型语音合成
    ├── 云Token监控              # 多云厂商 Token 消耗监控+推送
    ├── 多媒体处理助手             # 图片处理+PDF处理
    ├── 小红书自动发布            # 小红书自动化发布
    ├── 费用报销合规检查           # 收据与报销单交叉核对
    ├── 金融网页构建器             # Goldman Sachs 风格 Web Artifacts 构建
    ├── TODO任务追踪             # 持久化 TODO.md 任务清单
    └── AI-VC推文助手            # VC 风格 Twitter/X 帖子生成
```

---

## 🤝 如何贡献

天际团队成员如有新 Skill 要入库，欢迎联系技术团队提交。

外部社区用户发现好用的 Skills 也欢迎推荐！

---

## 📮 联系方式

**天际资本（FutureX Capital）**
📧 capper@futurexcapital.com

*Built for FutureX Team · Open for Everyone*
