#!/usr/bin/env python3
"""
发送报告到飞书
"""
import json
import logging
from pathlib import Path
from datetime import datetime
import urllib.request
import urllib.parse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
CHARTS_DIR = DATA_DIR / "charts"
PROCESSED_DIR = DATA_DIR / "processed"


def load_config():
    """加载配置"""
    import yaml
    config_file = BASE_DIR / "config.yaml"
    if not config_file.exists():
        return {}
    with open(config_file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_stats():
    """加载统计数据"""
    stats_file = PROCESSED_DIR / "daily_stats.json"
    if not stats_file.exists():
        return {}
    with open(stats_file, "r", encoding="utf-8") as f:
        return json.load(f)


def format_number(num):
    """格式化数字"""
    if num >= 100000000:
        return f"{num/100000000:.2f}亿"
    elif num >= 10000:
        return f"{num/10000:.2f}万"
    return str(num)


def build_message(date_str: str, daily_data: dict) -> dict:
    """构建飞书消息"""
    # 计算总计
    total_input = sum(d.get("input_tokens", 0) for d in daily_data.values())
    total_output = sum(d.get("output_tokens", 0) for d in daily_data.values())
    total_tokens = sum(d.get("total_tokens", 0) for d in daily_data.values())
    total_cost_usd = sum(d.get("cost_usd", 0) for d in daily_data.values())
    total_cost_cny = sum(d.get("cost_cny", 0) for d in daily_data.values())
    
    # 构建内容
    content = f"**📊 云厂商 Token 消耗日报 ({date_str})**\n\n"
    content += f"**总计**\n"
    content += f"• Input: {format_number(total_input)}\n"
    content += f"• Output: {format_number(total_output)}\n"
    content += f"• Total: {format_number(total_tokens)}\n"
    content += f"• 预估成本: ${total_cost_usd:.2f} / ¥{total_cost_cny:.2f}\n\n"
    content += "**各厂商详情**\n"
    
    for provider, data in sorted(daily_data.items(), key=lambda x: x[1].get("total_tokens", 0), reverse=True):
        if "error" not in data:
            content += f"• **{provider}**: {format_number(data.get('total_tokens', 0))} tokens"
            if data.get('cost_usd'):
                content += f" (${data['cost_usd']:.2f})"
            content += "\n"
    
    return {
        "msg_type": "interactive",
        "card": {
            "config": {"wide_screen_mode": True},
            "header": {
                "title": {
                    "tag": "plain_text",
                    "content": f"☁️ Cloud Token Monitor - {date_str}"
                },
                "template": "blue"
            },
            "elements": [
                {
                    "tag": "div",
                    "text": {
                        "tag": "lark_md",
                        "content": content
                    }
                }
            ]
        }
    }


def send_to_feishu(webhook_url: str, message: dict):
    """发送消息到飞书"""
    headers = {
        "Content-Type": "application/json"
    }
    
    data = json.dumps(message).encode("utf-8")
    
    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers=headers,
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
            if result.get("code") == 0:
                logger.info("✓ 消息发送成功")
                return True
            else:
                logger.error(f"✗ 发送失败: {result}")
                return False
    except Exception as e:
        logger.error(f"✗ 发送异常: {e}")
        return False


def main():
    """主函数"""
    config = load_config()
    webhook_url = config.get("feishu", {}).get("webhook_url")
    
    if not webhook_url:
        logger.error("未配置飞书 webhook_url")
        return
    
    stats = load_stats()
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    if date_str not in stats:
        logger.error(f"无 {date_str} 的数据")
        return
    
    message = build_message(date_str, stats[date_str])
    send_to_feishu(webhook_url, message)


if __name__ == "__main__":
    main()
