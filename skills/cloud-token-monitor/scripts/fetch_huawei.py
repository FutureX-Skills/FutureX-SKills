#!/usr/bin/env python3
"""
华为云 Token 数据获取
"""
import os
import logging

logger = logging.getLogger(__name__)


def fetch(date_str: str) -> dict:
    """获取华为云 ModelArts Token 用量"""
    access_key = os.getenv("HUAWEI_ACCESS_KEY")
    secret_key = os.getenv("HUAWEI_SECRET_KEY")
    
    if not access_key or not secret_key:
        logger.warning("未配置 HUAWEI_ACCESS_KEY 或 HUAWEI_SECRET_KEY")
        return {
            "provider": "huawei",
            "date": date_str,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0,
            "cost_cny": 0,
            "note": "凭证未配置"
        }
    
    return {
        "provider": "huawei",
        "date": date_str,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0,
        "cost_cny": 0,
        "note": "待实现 - 需要接入华为云 CES API"
    }
