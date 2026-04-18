# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/cloud-token-monitor
```

> **前提条件**：Python3 + pip，配置各云厂商凭证（详见 references/credentials_setup.md）

---

# cloud-token-monitor

name: cloud-token-monitor
description: 自动收集国内外主流云厂商（阿里云、腾讯云、华为云、百度云、火山引擎、AWS、Azure、GCP、Google AI、OpenAI、Anthropic）的每日 Token 消耗数据，生成可视化图表并推送到飞书。用于监控多平台 AI 用量和成本分析。当用户需要查询云厂商 token 消耗、生成用量报告、对比各平台成本或设置每日自动监控时使用此技能。

## Cloud Token Monitor

监控国内外主流云厂商的每日 Token 消耗量，自动生成图表并推送到飞书。

## 支持的云厂商

### 国内厂商

- 阿里云（百炼/灵积）
- 腾讯云（TI-ONE）
- 华为云（ModelArts）
- 百度云（千帆）
- 火山引擎（方舟）

### 国外厂商

- AWS（Bedrock）
- Azure（OpenAI Service）
- Google Cloud（Vertex AI）
- Google AI（Gemini API）
- OpenAI
- Anthropic

## 快速开始

### 1. 配置凭证

各厂商需要不同的认证方式，详见 references/credentials_setup.md

### 2. 运行监控

```bash
# 手动执行一次数据收集
python3 scripts/collect_all.py

# 生成图表并发送到飞书
python3 scripts/generate_report.py --output feishu
```

### 3. 设置每日自动运行

```bash
# 添加到 crontab（每天 9:00 运行）
0 9 * * * cd /root/.openclaw/workspace/skills/cloud-token-monitor && python3 scripts/collect_all.py && python3 scripts/generate_report.py --output feishu
```

## 脚本说明

| 脚本 | 功能 |
|------|------|
| scripts/collect_all.py | 收集所有厂商数据 |
| scripts/fetch_*.py | 各厂商数据获取脚本 |
| scripts/generate_chart.py | 生成对比图表 |
| scripts/send_feishu.py | 飞书消息推送 |
| scripts/generate_report.py | 完整报告生成 |

## 数据结构

收集的数据保存在 data/ 目录：

- data/raw/YYYY-MM-DD/ - 原始 API 响应
- data/processed/daily_stats.json - 清洗后的每日统计
- data/charts/ - 生成的图表文件

## 配置

编辑 config.yaml：

```yaml
feishu:
  webhook_url: "https://open.feishu.cn/open-apis/bot/v2/hook/xxx"
  
providers:
  aliyun:
    enabled: true
    api_key: "${ALIYUN_API_KEY}"
  # ... 其他厂商
```

## 参考文档

- API 文档汇总：references/api_docs.md
- 凭证配置指南：references/credentials_setup.md
