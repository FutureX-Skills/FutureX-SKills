# VCPE Fundraising Tracker

> 全球 VC/PE 募资动态追踪工具，多数据源聚合（PitchBook、Crunchbase、TechCrunch、VentureBeat、PE Hub、投中网、36 氪等），支持最新新闻、周报生成、特定机构追踪、地区/行业筛选。

**创建人：Angela**

> 💡 与 [PE募资追踪器](../PE募资追踪器/)（重点关注中国和美国市场 + 自动 LP 情报报告）形成互补：本 Skill 侧重**全球范围**的多源新闻聚合与按需查询，PE募资追踪器 侧重中美深度 LP 分析与定时推送。

---

## 适用场景

- 了解全球本周/本月 VC、PE 募资全景
- 追踪某只大型基金（红杉、KKR、Blackstone 等）的最新募资进度
- 按地区（北美 / 欧洲 / 亚太）或行业（AI / 医疗 / 消费）筛选募资动态
- 生成投决会、LP 沟通会前的"全球募资周报"

---

## 核心能力

### 1. 最新募资新闻

实时聚合 TechCrunch、VentureBeat、PE Hub、投中网、36 氪等多源新闻，按时间线汇总。

### 2. 募资周报生成

按"概览 → 地区分布 → 重点事件 → 趋势观察"结构生成标准化周报，可直接用于内部分享。

### 3. 特定基金追踪

输入机构名（如"红杉资本"、"KKR"），返回该机构最新募资进度、目标规模、当前进展。

### 4. 多维筛选

支持按地区（北美 / 欧洲 / 亚太 / 其他）、行业（科技 / 医疗 / 消费 等）、金额、币种快速筛选。

---

## 触发关键词

- VC 募资 / PE 募资 / 风险投资募资 / 私募股权募资
- fundraising tracker / latest VC funding
- 全球募资情况 / 募资周报

---

## 一键安装

```bash
cd ~/.openclaw/workspace/FutureX-SKills
git pull origin main
cp -r 天际团队SKills库/vcpe-fundraising-tracker ~/.openclaw/workspace/skills/

# 或一步到位
cd ~/.openclaw/workspace/FutureX-SKills && git pull && cp -r 天际团队SKills库/vcpe-fundraising-tracker ~/.openclaw/workspace/skills/
```

---

## 使用方式

直接对话触发，例如：

- "最近有什么 VC 募资新闻？"
- "生成本周 VC 募资周报"
- "追踪红杉资本的募资情况"
- "中国 PE 市场最近募资情况"

---

## 注意事项

- 募资数据可能有延迟，输出会标注数据来源和时间
- 区分"首次募集完成"和"最终募集完成"
- 注意币种单位（USD / CNY / EUR）
- 大额募资事件会优先展示
