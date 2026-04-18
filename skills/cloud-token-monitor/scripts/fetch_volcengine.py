#!/usr/bin/env python3
"""
火山引擎 Token 数据获取
"""
import os
import logging

logger = logging.getLogger(__name__)


def fetch(date_str: str) -> dict:
    """获取火山引擎方舟 Token 用量"""
    api_key = os.getenv("VOLCENGINE_API_KEY")
    
    if not api_key:
        logger.warning("未配置 VOLCENGINE_API_KEY")
        return {
            "provider": "volcengine",
            "date": date_str,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0,
            "cost_cny": 0,
            "note": "API Key 未配置"
        }
    
    return {
        "provider": "volcengine",
        "date": date_str,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0,
        "cost_cny": 0,
        "note": "待实现 - 需要接入方舟 API"
    }
