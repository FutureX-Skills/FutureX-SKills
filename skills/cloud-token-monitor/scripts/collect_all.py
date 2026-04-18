#!/usr/bin/env python3
"""
收集所有云厂商的 Token 消耗数据
"""
import os
import sys
import json
import logging
from datetime import datetime
from pathlib import Path

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 基础路径
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# 确保目录存在
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# 支持的厂商列表
PROVIDERS = [
    "aliyun",
    "tencent",
    "huawei",
    "baidu",
    "volcengine",
    "aws",
    "azure",
    "gcp",
    "google_ai",
    "openai",
    "anthropic"
]


def collect_provider(provider_name: str, date_str: str) -> dict:
    """收集单个厂商的数据"""
    try:
        # 动态导入对应的 fetch 模块
        fetch_module = __import__(f"fetch_{provider_name}", fromlist=["fetch"])
        data = fetch_module.fetch(date_str)
        logger.info(f"✓ {provider_name}: 收集成功")
        return data
    except Exception as e:
        logger.error(f"✗ {provider_name}: 收集失败 - {e}")
        return {"error": str(e), "provider": provider_name}


def save_raw_data(provider: str, date_str: str, data: dict):
    """保存原始数据"""
    provider_dir = RAW_DIR / date_str
    provider_dir.mkdir(parents=True, exist_ok=True)
    
    file_path = provider_dir / f"{provider}.json"
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    logger.info(f"  原始数据已保存: {file_path}")


def update_daily_stats(date_str: str, all_data: dict):
    """更新每日统计文件"""
    stats_file = PROCESSED_DIR / "daily_stats.json"
    
    # 读取现有数据
    if stats_file.exists():
        with open(stats_file, "r", encoding="utf-8") as f:
            stats = json.load(f)
    else:
        stats = {}
    
    # 提取关键指标
    daily_summary = {}
    for provider, data in all_data.items():
        if "error" not in data:
            daily_summary[provider] = {
                "input_tokens": data.get("input_tokens", 0),
                "output_tokens": data.get("output_tokens", 0),
                "total_tokens": data.get("total_tokens", 0),
                "cost_usd": data.get("cost_usd", 0),
                "cost_cny": data.get("cost_cny", 0)
            }
    
    stats[date_str] = daily_summary
    
    # 保存更新后的统计
    with open(stats_file, "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)
    logger.info(f"  每日统计已更新: {stats_file}")


def main():
    """主函数"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    logger.info(f"开始收集 {date_str} 的云厂商 Token 数据...")
    
    all_data = {}
    
    for provider in PROVIDERS:
        data = collect_provider(provider, date_str)
        all_data[provider] = data
        save_raw_data(provider, date_str, data)
    
    # 更新每日统计
    update_daily_stats(date_str, all_data)
    
    logger.info(f"数据收集完成！共 {len(all_data)} 个厂商")
    
    # 输出汇总
    success_count = sum(1 for d in all_data.values() if "error" not in d)
    logger.info(f"成功: {success_count}, 失败: {len(all_data) - success_count}")


if __name__ == "__main__":
    main()
