# FutureX Skills 知识库

> 天际资本（FutureX Capital）内部 Skills 资产沉淀仓库，涵盖投研、内容创作、运营提效等全场景 AI 工具集。

---

## 📁 仓库结构

```
futurex-skills/
├── 外部精选Skills/          # 天际精选的优质开源 Skills，持续更新
│   ├── qiaomu-markdown-proxy/     # URL → Markdown 转换（微信公众号/飞书/PDF/YouTube）
│   └── 李继刚skills/              # 李继刚老师的 Skills 合集（16个）
│       ├── ljg-card               # 内容铸造成 PNG 海报/信息图
│       ├── ljg-paper              # 论文阅读（给普通人读的论文解析）
│       ├── ljg-paper-river        # 论文溯源（问题演化史）
│       ├── ljg-invest             # 投资分析报告
│       ├── ljg-learn              # 概念解剖（8维度）
│       ├── ljg-plain              # 说人话（12岁能懂的解释）
│       ├── ljg-rank               # 降秩分析（找不可再少的力）
│       ├── ljg-relationship       # 关系分析（结构诊断+精神分析）
│       ├── ljg-roundtable         # 圆桌辩论框架
│       ├── ljg-think              # 追本之箭（纵向深钻）
│       ├── ljg-travel             # 深度旅行研究
│       ├── ljg-word               # 英语单词深度掌握
│       ├── ljg-writes             # 写作引擎（写中想透）
│       └── ...（共16个）
│
├── 天际团队SKills库/        # 天际资本团队自建的 Skills（26个）
│   ├── 研报助手                  # MoE 多智能体调度中心，生成投行级尽调报告
│   ├── GPilot-Simon             # Simon's GPilot — 天际内部 AI 助手系统
│   ├── 视频标题大师              # 短视频封面标题与简介生成
│   ├── 硅谷季度报告              # VC 赛道趋势分析报告（90天）
│   ├── 社媒营销                  # LinkedIn/TikTok/Meta/YouTube/X 多平台内容
│   ├── 社媒内容处理              # 图片水印/文字标注/视频拼接/尺寸适配
│   ├── AI内容写作助手            # AI 行业热点深度长文（5000字+Word）
│   ├── 公众号排版助手             # 微信公众号 HTML 排版
│   ├── LinkedIn内容助手          # LinkedIn 短帖子+长文章生成
│   ├── 播客后期助手              # 双语播客后期（文字稿→多平台适配内容）
│   ├── 投资-Memo                 # VC 投资备忘录/Deal Memo 撰写
│   ├── 立项报告                  # 中文 VC 立项报告撰写
│   ├── 项目立项投资报告           # 标准立项框架生成完整投资报告
│   ├── PE募资追踪器             # 全球 PE/VC 募资动态追踪+LP分析
│   ├── PIB投研搜索              # 私募公司 VC 风格投研备忘录
│   ├── VC创始人会面准备          # 创始人会面问题清单生成
│   ├── 会议纪要整理助手           # 录音转文字→结构化会议纪要
│   ├── 事项提醒                  # Excel生日列表→飞书日历年度提醒
│   ├── 旅行规划助手              # 保姆级旅行规划（小白友好）
│   ├── 语音合成助手              # TTS 多模型语音合成
│   ├── 云Token监控              # 多云厂商 Token 消耗监控+推送
│   ├── 多媒体处理助手             # 图片处理+PDF处理
│   ├── 小红书自动发布            # 小红书自动化发布（xiaohongshu-mcp）
│   ├── 费用报销合规检查           # 收据与报销单交叉核对
│   ├── 金融网页构建器             # Goldman Sachs 风格 Web Artifacts 构建
│   ├── TODO任务追踪             # 持久化 TODO.md 任务清单
│   └── AI-VC推文助手            # VC 风格 Twitter/X 帖子生成
│
└── GPilot-Simon/            # CEO Simon 开源项目（独立展示）
    ├── agents/                     # 8个专用 Agent
    ├── commands/                    # 19个投研命令
    ├── skills/                     # 6个核心技能
    ├── scheduled/                   # 9个定时任务
    ├── modules/                    # 募资运营/LP Reporting 等
    ├── dashboard/                  # Next.js 管理面板
    └── scripts/                    # 快速启动脚本
```

---

## 🚀 一键安装

### 安装全部 Skills

```bash
curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/futurex-skills/main/install-all.sh | bash
```

### 安装单个 Skill

以 `研报助手` 为例：

```bash
curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/futurex-skills/main/天际团队SKills库/研报助手/install.sh | bash
```

> 每个 Skill 目录下均有对应的 `install.sh` 脚本

---

## 📖 快速导航

| 需求场景 | 推荐 Skills |
|---------|------------|
| 生成投研报告、尽调报告 | `研报助手`、`硅谷季度报告`、`立项报告`、`PIB投研搜索` |
| 社交媒体内容创作 | `社媒营销`、`视频标题大师`、`LinkedIn内容助手`、`AI-VC推文助手` |
| 播客/内容生产 | `播客后期助手`、`公众号排版助手`、`AI内容写作助手` |
| 投资业务提效 | `投资-Memo`、`VC创始人会面准备`、`会议纪要整理助手`、`PE募资追踪器` |
| 运营与合规 | `费用报销合规检查`、`事项提醒`、`云Token监控`、`TODO任务追踪` |
| 外部精选工具 | `qiaomu-markdown-proxy`、`李继刚skills/` |

---

## 🤝 如何贡献

天际团队成员如有新 Skill 要入库：

1. 将 Skill 文件整理为 `[Skill名称]/SKILL.md` 结构
2. 联系管理员上传，或提交 PR
3. 外部精选 Skills 持续接收推荐，欢迎分享

---

## 📮 联系方式

如有问题或建议，欢迎联系天际资本技术团队。

---

*Maintained by FutureX Capital · Built for FutureX Team*
