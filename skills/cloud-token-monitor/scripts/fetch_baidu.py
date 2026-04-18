#!/usr/bin/env python3
"""
百度云 Token 数据获取
"""
import os
import logging

logger = logging.getLogger(__name__)


def fetch(date_str: str) -> dict:
    """获取百度云千帆 Token 用量"""
    api_key = os.getenv("BAIDU_API_KEY")
    secret_key = os.getenv("BAIDU_SECRET_KEY")
    
    if not api_key or not secret_key:
        logger.warning("未配置 BAIDU_API_KEY 或 BAIDU_SECRET_KEY")
        return {
            "provider": "baidu",
            "date": date_str,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0,
            "cost_cny": 0,
            "note": "凭证未配置"
        }
    
    return {
        "provider": "baidu",
        "date": date_str,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0,
        "cost_cny": 0,
        "note": "待实现 - 需要接入千帆 API"
    }
