#!/usr/bin/env python3
"""
Google Cloud Token 数据获取
"""
import os
import logging

logger = logging.getLogger(__name__)


def fetch(date_str: str) -> dict:
    """获取 Google Cloud Vertex AI Token 用量"""
    credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    
    if not credentials:
        logger.warning("未配置 GOOGLE_APPLICATION_CREDENTIALS")
        return {
            "provider": "gcp",
            "date": date_str,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0,
            "cost_cny": 0,
            "note": "凭证未配置"
        }
    
    return {
        "provider": "gcp",
        "date": date_str,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0,
        "cost_cny": 0,
        "note": "待实现 - 需要接入 GCP Cloud Monitoring API"
    }
