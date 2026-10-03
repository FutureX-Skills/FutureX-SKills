# FutureX Skills 知识库

> **天际资本（FutureX Capital）** 出品 | 全部开源 | 持续更新

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

网站首页使用根目录的 [`skills.json`](skills.json) 作为 Skill 目录唯一数据源。修改 Skill 清单、链接或安装信息后，请运行 `node scripts/validate-catalog.mjs` 检查目录完整性。

### 快速导航

| 需求场景 | 推荐 Skills |
|---------|------------|
| 生成投研报告、尽调报告 | `研报助手`、`硅谷季度报告`、`立项报告`、`PIB投研搜索` |
| 社交媒体内容创作 | `社媒营销`、`视频标题大师`、`LinkedIn内容助手`、`AI-VC推文助手` |
| 播客/内容生产 | `播客后期助手`、`FutureX公众号长文写作`、`FutureX创意排版`、`公众号排版助手`、`AI内容写作助手` |
| 投资业务提效 | `投资-Memo`、`VC创始人会面准备`、`会议纪要整理助手`、`PE募资追踪器`、`vcpe-fundraising-tracker` |
| 活动与情报追踪 | `sg-luma-events`、`PE募资追踪器`、`vcpe-fundraising-tracker` |
| 运营与合规 | `费用报销合规检查`、`事项提醒`、`云Token监控`、`TODO任务追踪`、`pptx-logo-label-fix` |
| 外部精选工具 | `qiaomu-markdown-proxy`、`李继刚skills/`、`43-Agent-skills/` |

<!-- CATALOG:START -->
## 📚 Skill 清单（由 `skills.json` 生成）

当前目录共 **65** 个 Skills：天际自建 31 个，外部精选 34 个。

| Skill | 分类 | 来源 | 仓库路径 |
|------|------|------|----------|
| [研报助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E7%A0%94%E6%8A%A5%E5%8A%A9%E6%89%8B) | 投研 | 天际自建 | `天际团队SKills库/研报助手` |
| [PIB投研搜索](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/PIB%E6%8A%95%E7%A0%94%E6%90%9C%E7%B4%A2) | 投研 | 天际自建 | `天际团队SKills库/PIB投研搜索` |
| [投资-Memo](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E6%8A%95%E8%B5%84-Memo) | 投研 | 天际自建 | `天际团队SKills库/投资-Memo` |
| [立项报告](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E7%AB%8B%E9%A1%B9%E6%8A%A5%E5%91%8A) | 投研 | 天际自建 | `天际团队SKills库/立项报告` |
| [项目立项投资报告](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E9%A1%B9%E7%9B%AE%E7%AB%8B%E9%A1%B9%E6%8A%95%E8%B5%84%E6%8A%A5%E5%91%8A) | 投研 | 天际自建 | `天际团队SKills库/项目立项投资报告` |
| [硅谷季度报告](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E7%A1%85%E8%B0%B7%E5%AD%A3%E5%BA%A6%E6%8A%A5%E5%91%8A) | 投研 | 天际自建 | `天际团队SKills库/硅谷季度报告` |
| [PE募资追踪器](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/PE%E5%8B%9F%E8%B5%84%E8%BF%BD%E8%B8%AA%E5%99%A8) | 投研 | 天际自建 | `天际团队SKills库/PE募资追踪器` |
| [vcpe-fundraising-tracker](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/vcpe-fundraising-tracker) | 投研 | 天际自建 | `天际团队SKills库/vcpe-fundraising-tracker` |
| [视频标题大师](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E8%A7%86%E9%A2%91%E6%A0%87%E9%A2%98%E5%A4%A7%E5%B8%88) | 内容创作 | 天际自建 | `天际团队SKills库/视频标题大师` |
| [AI内容写作助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/AI%E5%86%85%E5%AE%B9%E5%86%99%E4%BD%9C%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/AI内容写作助手` |
| [FutureX公众号长文写作](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/futurex-writer) | 内容创作 | 天际自建 | `天际团队SKills库/futurex-writer` |
| [微信公众号Markdown排版助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E5%85%AC%E4%BC%97%E5%8F%B7%E6%8E%92%E7%89%88%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/公众号排版助手` |
| [FutureX创意排版](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/fx-wechat-formatter) | 内容创作 | 天际自建 | `天际团队SKills库/fx-wechat-formatter` |
| [AI-VC推文助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/AI-VC%E6%8E%A8%E6%96%87%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/AI-VC推文助手` |
| [LinkedIn内容助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/LinkedIn%E5%86%85%E5%AE%B9%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/LinkedIn内容助手` |
| [播客后期助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E6%92%AD%E5%AE%A2%E5%90%8E%E6%9C%9F%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/播客后期助手` |
| [旅行规划助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E6%97%85%E8%A1%8C%E8%A7%84%E5%88%92%E5%8A%A9%E6%89%8B) | 内容创作 | 天际自建 | `天际团队SKills库/旅行规划助手` |
| [金融网页构建器](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E9%87%91%E8%9E%8D%E7%BD%91%E9%A1%B5%E6%9E%84%E5%BB%BA%E5%99%A8) | 内容创作 | 天际自建 | `天际团队SKills库/金融网页构建器` |
| [社媒营销](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E7%A4%BE%E5%AA%92%E8%90%A5%E9%94%80) | 社媒运营 | 天际自建 | `天际团队SKills库/社媒营销` |
| [社媒内容处理](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E7%A4%BE%E5%AA%92%E5%86%85%E5%AE%B9%E5%A4%84%E7%90%86) | 社媒运营 | 天际自建 | `天际团队SKills库/社媒内容处理` |
| [小红书自动发布](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E5%B0%8F%E7%BA%A2%E4%B9%A6%E8%87%AA%E5%8A%A8%E5%8F%91%E5%B8%83) | 社媒运营 | 天际自建 | `天际团队SKills库/小红书自动发布` |
| [语音合成助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E8%AF%AD%E9%9F%B3%E5%90%88%E6%88%90%E5%8A%A9%E6%89%8B) | 社媒运营 | 天际自建 | `天际团队SKills库/语音合成助手` |
| [多媒体处理助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E5%A4%9A%E5%AA%92%E4%BD%93%E5%A4%84%E7%90%86%E5%8A%A9%E6%89%8B) | 社媒运营 | 天际自建 | `天际团队SKills库/多媒体处理助手` |
| [会议纪要整理助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E4%BC%9A%E8%AE%AE%E7%BA%AA%E8%A6%81%E6%95%B4%E7%90%86%E5%8A%A9%E6%89%8B) | 效率工具 | 天际自建 | `天际团队SKills库/会议纪要整理助手` |
| [VC创始人会面准备](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/VC%E5%88%9B%E5%A7%8B%E4%BA%BA%E4%BC%9A%E9%9D%A2%E5%87%86%E5%A4%87) | 效率工具 | 天际自建 | `天际团队SKills库/VC创始人会面准备` |
| [云Token监控](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E4%BA%91Token%E7%9B%91%E6%8E%A7) | 效率工具 | 天际自建 | `天际团队SKills库/云Token监控` |
| [费用报销合规检查](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E8%B4%B9%E7%94%A8%E6%8A%A5%E9%94%80%E5%90%88%E8%A7%84%E6%A3%80%E6%9F%A5) | 效率工具 | 天际自建 | `天际团队SKills库/费用报销合规检查` |
| [pptx-logo-label-fix](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/pptx-logo-label-fix) | 效率工具 | 天际自建 | `天际团队SKills库/pptx-logo-label-fix` |
| [sg-luma-events](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/sg-luma-events) | 效率工具 | 天际自建 | `天际团队SKills库/sg-luma-events` |
| [ljg-invest](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-invest) | 投研 | 外部精选 | `外部精选Skills/李继刚skills/ljg-invest` |
| [ljg-learn](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-learn) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-learn` |
| [ljg-paper](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-paper) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-paper` |
| [ljg-paper-river](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-paper-river) | 投研 | 外部精选 | `外部精选Skills/李继刚skills/ljg-paper-river` |
| [ljg-plain](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-plain) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-plain` |
| [ljg-rank](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-rank) | 投研 | 外部精选 | `外部精选Skills/李继刚skills/ljg-rank` |
| [ljg-relationship](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-relationship) | 投研 | 外部精选 | `外部精选Skills/李继刚skills/ljg-relationship` |
| [ljg-roundtable](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-roundtable) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-roundtable` |
| [ljg-think](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-think) | 投研 | 外部精选 | `外部精选Skills/李继刚skills/ljg-think` |
| [ljg-travel](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-travel) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-travel` |
| [ljg-word](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-word) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-word` |
| [ljg-writes](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-writes) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-writes` |
| [ljg-card](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/%E6%9D%8E%E7%BB%A7%E5%88%9Askills/ljg-card) | 内容创作 | 外部精选 | `外部精选Skills/李继刚skills/ljg-card` |
| [聊天记录归档](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/chat-archiver) | 效率工具 | 外部精选 | `外部精选Skills/43-Agent-skills/chat-archiver` |
| [飞书助手](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/feishu-assistant) | 效率工具 | 外部精选 | `外部精选Skills/43-Agent-skills/feishu-assistant` |
| [追踪创业者动态](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/follow-builders) | 投研 | 外部精选 | `外部精选Skills/43-Agent-skills/follow-builders` |
| [媒体转录](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/media-transcriber) | 内容创作 | 外部精选 | `外部精选Skills/43-Agent-skills/media-transcriber` |
| [社交媒体情报](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/social-media-scout) | 社媒运营 | 外部精选 | `外部精选Skills/43-Agent-skills/social-media-scout` |
| [视频创作](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/video-creator) | 社媒运营 | 外部精选 | `外部精选Skills/43-Agent-skills/video-creator` |
| [浏览器自动化](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/43-Agent-skills/web-browser) | 效率工具 | 外部精选 | `外部精选Skills/43-Agent-skills/web-browser` |
| [qiaomu-markdown-proxy](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/qiaomu-markdown-proxy) | 效率工具 | 外部精选 | `外部精选Skills/qiaomu-markdown-proxy` |
| [skill-vetter](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/Skill-Vetter/skills/skill-vetter) | 效率工具 | 外部精选 | `外部精选Skills/Skill-Vetter/skills/skill-vetter` |
| [skill-creator](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/skill-creator) | 效率工具 | 外部精选 | `外部精选Skills/skill-creator` |
| [ian-xiaohei-illustrations](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/ian-xiaohei-illustrations) | 内容创作 | 外部精选 | `外部精选Skills/ian-xiaohei-illustrations` |
| [BP初筛](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/pitch-deck-screening.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/pitch-deck-screening.md` |
| [Claim核验](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/claims-verification.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/claims-verification.md` |
| [风险Memo](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/risk-memo.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/risk-memo.md` |
| [赛道图谱](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/market-map.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/market-map.md` |
| [公司One-Pager](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/startup-onepager.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/startup-onepager.md` |
| [技术尽调](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/technical-dd.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/technical-dd.md` |
| [投委会Memo](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/memo-to-ic.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/memo-to-ic.md` |
| [用户反馈分析](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/product-feedback-analysis.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/product-feedback-analysis.md` |
| [论文投资分析](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/paper-analysis.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/paper-analysis.md` |
| [专利分析](https://github.com/FutureX-Skills/FutureX-SKills/blob/main/%E5%A4%96%E9%83%A8%E7%B2%BE%E9%80%89Skills/futurex-vc-skills/skills/patent-analysis.md) | 投研 | 外部精选 | `外部精选Skills/futurex-vc-skills/skills/patent-analysis.md` |
| [TODO任务追踪](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/TODO%E4%BB%BB%E5%8A%A1%E8%BF%BD%E8%B8%AA) | 效率工具 | 天际自建 | `天际团队SKills库/TODO任务追踪` |
| [事项提醒](https://github.com/FutureX-Skills/FutureX-SKills/tree/main/%E5%A4%A9%E9%99%85%E5%9B%A2%E9%98%9FSKills%E5%BA%93/%E4%BA%8B%E9%A1%B9%E6%8F%90%E9%86%92) | 效率工具 | 天际自建 | `天际团队SKills库/事项提醒` |

> 这部分由 `node scripts/generate-catalog.mjs` 生成，请修改 `skills.json` 后再运行生成脚本。
<!-- CATALOG:END -->

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
| **ian-xiaohei-illustrations** | [helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations) | 「小黑」手绘怪诞风中文文章正文配图（16:9 / shot list） |
| **futurex-vc-skills** | 外部VC | 10个 VC 投研 Agent 工作流（BP初筛/Claim核验/赛道图谱/技术尽调/IC memo 等），证据导向 |

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
│   ├── skill-creator           # 来源：[anthropics/skills](https://github.com/anthropics/skills)
│   │   ├── agents/                   # Analyzer / Comparator / Grader
│   │   ├── scripts/                  # validate / package / run_eval 等
│   │   └── eval-viewer/              # 评估可视化工具
│   │
│   ├── ian-xiaohei-illustrations  # 来源：[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)
│   │   ├── SKILL.md                  # 「小黑」手绘怪诞风中文正文配图
│   │   └── references/               # 风格DNA / 小黑IP / 构图 / 提示词模板 / QA
│   │
│   └── futurex-vc-skills        # 来源：外部VC
│       ├── AGENTS.md                 # VC 投研 Agent 总控规则（证据分级/保密）
│       ├── skills/                   # 10个投研工作流（BP初筛/Claim核验/赛道图谱/技术尽调/IC memo…）
│       ├── tasks/                    # 7个可直接执行的任务模板
│       └── codex-skills/futurex-vc/  # 打包好的 Codex Skill（入口 SKILL.md）
│
└── 天际团队SKills库/        # 天际资本团队自建 Skills（31个）
    ├── 研报助手                  # MoE 多智能体调度中心，生成投行级尽调报告
    ├── 视频标题大师              # 短视频封面标题与简介生成
    ├── 硅谷季度报告              # VC 赛道趋势分析报告（90天）
    ├── 社媒营销                  # LinkedIn/TikTok/Meta/YouTube/X 多平台内容
    ├── 社媒内容处理              # 图片水印/文字标注/视频拼接/尺寸适配
    ├── AI内容写作助手            # AI 行业热点深度长文（5000字+Word）
    ├── futurex-writer             # 天际资本官方公众号长文写作（选题判断 + 四层自检）
    ├── 公众号排版助手             # 微信公众号 DOCX 排版（8套配色+封面图自动配色）
    ├── fx-wechat-formatter        # 微信公众号「电表」杂志化创意排版（4套配色）
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
    ├── AI-VC推文助手            # VC 风格 Twitter/X 帖子生成
    ├── pptx-logo-label-fix      # 自动修复 PPTX 中公司 Logo 与文字标签错位
    ├── sg-luma-events           # 新加坡 Luma 活动追踪（Family Office/AI/募资/大厂）
    └── vcpe-fundraising-tracker # 全球 VC/PE 募资动态追踪（多源新闻聚合）
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
