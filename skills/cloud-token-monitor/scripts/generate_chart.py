#!/usr/bin/env python3
"""
生成 Token 消耗对比图表
"""
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta

try:
    import matplotlib.pyplot as plt
    import matplotlib
    matplotlib.use('Agg')  # 无头模式
except ImportError:
    plt = None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CHARTS_DIR = DATA_DIR / "charts"
PROCESSED_DIR = DATA_DIR / "processed"

CHARTS_DIR.mkdir(parents=True, exist_ok=True)


def load_stats():
    """加载统计数据"""
    stats_file = PROCESSED_DIR / "daily_stats.json"
    if not stats_file.exists():
        return {}
    with open(stats_file, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_daily_chart(stats: dict, date_str: str):
    """生成单日对比图"""
    if plt is None:
        logger.warning("matplotlib 未安装，跳过图表生成")
        return None
    
    if date_str not in stats:
        logger.warning(f"无 {date_str} 的数据")
        return None
    
    daily_data = stats[date_str]
    
    providers = []
    input_tokens = []
    output_tokens = []
    
    for provider, data in daily_data.items():
        providers.append(provider)
        input_tokens.append(data.get("input_tokens", 0) / 1000000)  # 转换为百万
        output_tokens.append(data.get("output_tokens", 0) / 1000000)
    
    if not providers:
        logger.warning("无有效数据")
        return None
    
    # 创建图表
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = range(len(providers))
    width = 0.35
    
    ax.bar([i - width/2 for i in x], input_tokens, width, label='Input Tokens', color='#4472C4')
    ax.bar([i + width/2 for i in x], output_tokens, width, label='Output Tokens', color='#ED7D31')
    
    ax.set_xlabel('Cloud Provider')
    ax.set_ylabel('Tokens (Millions)')
    ax.set_title(f'Daily Token Usage - {date_str}')
    ax.set_xticks(x)
    ax.set_xticklabels(providers, rotation=45, ha='right')
    ax.legend()
    
    plt.tight_layout()
    
    chart_path = CHARTS_DIR / f"daily_{date_str}.png"
    plt.savefig(chart_path, dpi=150)
    plt.close()
    
    logger.info(f"图表已生成: {chart_path}")
    return chart_path


def generate_trend_chart(stats: dict, days: int = 7):
    """生成趋势图"""
    if plt is None:
        return None
    
    # 获取最近 N 天的数据
    dates = sorted(stats.keys())[-days:]
    
    if len(dates) < 2:
        logger.warning("数据不足，无法生成趋势图")
        return None
    
    # 按厂商聚合数据
    provider_totals = {}
    for date in dates:
        for provider, data in stats[date].items():
            if provider not in provider_totals:
                provider_totals[provider] = []
            provider_totals[provider].append(data.get("total_tokens", 0) / 1000000)
    
    # 创建趋势图
    fig, ax = plt.subplots(figsize=(12, 6))
    
    for provider, totals in provider_totals.items():
        # 补齐数据
        while len(totals) < len(dates):
            totals.insert(0, 0)
        ax.plot(dates, totals, marker='o', label=provider)
    
    ax.set_xlabel('Date')
    ax.set_ylabel('Total Tokens (Millions)')
    ax.set_title(f'Token Usage Trend (Last {days} Days)')
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    chart_path = CHARTS_DIR / f"trend_{days}days.png"
    plt.savefig(chart_path, dpi=150)
    plt.close()
    
    logger.info(f"趋势图已生成: {chart_path}")
    return chart_path


def main():
    """主函数"""
    stats = load_stats()
    
    if not stats:
        logger.error("无统计数据")
        return
    
    # 生成今日图表
    today = datetime.now().strftime("%Y-%m-%d")
    generate_daily_chart(stats, today)
    
    # 生成趋势图
    generate_trend_chart(stats, days=7)


if __name__ == "__main__":
    main()
