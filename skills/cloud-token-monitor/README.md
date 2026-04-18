# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/cloud-token-monitor

# 安装依赖
pip install matplotlib pyyaml
```

> **前提条件**：Python3 + pip，配置各云厂商凭证

---

# Cloud Token Monitor

## 安装依赖

```bash
pip install matplotlib pyyaml
```

## 配置凭证

1. 复制配置模板
```bash
cp config.yaml.example config.yaml
```

2. 编辑 `config.yaml`，配置各厂商凭证

3. 或使用环境变量（推荐）
```bash
export ALIYUN_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
# ... 其他厂商
```

## 使用方法

### 手动运行

```bash
# 收集数据
python3 scripts/collect_all.py

# 生成图表
python3 scripts/generate_chart.py

# 发送飞书报告
python3 scripts/send_feishu.py

# 一键生成完整报告
python3 scripts/generate_report.py --output feishu
```

### 自动运行

添加到 crontab：
```bash
# 每天 9:00 执行
0 9 * * * cd /path/to/cloud-token-monitor && python3 scripts/generate_report.py --output feishu
```

## 目录结构

```
cloud-token-monitor/
├── SKILL.md                    # 技能文档
├── README.md                   # 使用说明
├── config.yaml                 # 配置文件
├── scripts/                    # 脚本目录
│   ├── collect_all.py         # 主收集脚本
│   ├── generate_chart.py      # 图表生成
│   ├── send_feishu.py         # 飞书推送
│   ├── generate_report.py     # 报告生成
│   └── fetch_*.py             # 各厂商数据获取
├── references/                 # 参考文档
│   ├── api_docs.md            # API 文档汇总
│   └── credentials_setup.md   # 凭证配置指南
└── data/                       # 数据目录
    ├── raw/                   # 原始数据
    ├── processed/             # 处理后数据
    └── charts/                # 生成图表
```

## 开发说明

### 添加新厂商

1. 创建 `scripts/fetch_<provider>.py`
2. 实现 `fetch(date_str: str) -> dict` 函数
3. 返回格式：
```python
{
    "provider": "provider_name",
    "date": "2024-01-01",
    "input_tokens": 1000000,
    "output_tokens": 500000,
    "total_tokens": 1500000,
    "cost_usd": 0.5,
    "cost_cny": 3.5
}
```
4. 在 `collect_all.py` 的 `PROVIDERS` 列表中添加厂商名

## 注意事项

- 各厂商 API 权限和计费方式不同，需要分别申请
- 部分厂商（如 OpenAI）需要组织级 API Key 才能获取用量数据
- 建议先在控制台确认用量数据可查看，再配置 API 访问
