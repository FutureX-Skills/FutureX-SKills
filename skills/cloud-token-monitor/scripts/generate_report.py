#!/usr/bin/env python3
"""
生成完整报告
"""
import argparse
import logging
from pathlib import Path
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent


def run_collection():
    """运行数据收集"""
    import subprocess
    result = subprocess.run(
        ["python3", str(BASE_DIR / "scripts/collect_all.py")],
        capture_output=True,
        text=True
    )
    logger.info(result.stdout)
    if result.returncode != 0:
        logger.error(result.stderr)
    return result.returncode == 0


def generate_charts():
    """生成图表"""
    import subprocess
    result = subprocess.run(
        ["python3", str(BASE_DIR / "scripts/generate_chart.py")],
        capture_output=True,
        text=True
    )
    logger.info(result.stdout)
    return result.returncode == 0


def send_feishu():
    """发送到飞书"""
    import subprocess
    result = subprocess.run(
        ["python3", str(BASE_DIR / "scripts/send_feishu.py")],
        capture_output=True,
        text=True
    )
    logger.info(result.stdout)
    return result.returncode == 0


def main():
    parser = argparse.ArgumentParser(description="生成云厂商 Token 消耗报告")
    parser.add_argument(
        "--output",
        choices=["feishu", "console", "all"],
        default="console",
        help="输出方式"
    )
    parser.add_argument(
        "--skip-collection",
        action="store_true",
        help="跳过数据收集"
    )
    
    args = parser.parse_args()
    
    logger.info(f"开始生成报告 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # 数据收集
    if not args.skip_collection:
        logger.info("=" * 40)
        logger.info("步骤 1/3: 收集数据...")
        if not run_collection():
            logger.error("数据收集失败")
            return
    
    # 生成图表
    logger.info("=" * 40)
    logger.info("步骤 2/3: 生成图表...")
    generate_charts()
    
    # 发送报告
    logger.info("=" * 40)
    logger.info("步骤 3/3: 发送报告...")
    if args.output in ("feishu", "all"):
        send_feishu()
    
    logger.info("=" * 40)
    logger.info("报告生成完成！")


if __name__ == "__main__":
    main()
