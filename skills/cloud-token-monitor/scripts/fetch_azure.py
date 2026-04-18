#!/usr/bin/env python3
"""
Azure Token 数据获取
"""
import os
import logging

logger = logging.getLogger(__name__)


def fetch(date_str: str) -> dict:
    """获取 Azure OpenAI Service Token 用量"""
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    
    if not endpoint or not api_key:
        logger.warning("未配置 AZURE_OPENAI_ENDPOINT 或 AZURE_OPENAI_API_KEY")
        return {
            "provider": "azure",
            "date": date_str,
            "input_tokens": 0,
            "output_tokens": 0,
            "total_tokens": 0,
            "cost_usd": 0,
            "cost_cny": 0,
            "note": "凭证未配置"
        }
    
    return {
        "provider": "azure",
        "date": date_str,
        "input_tokens": 0,
        "output_tokens": 0,
        "total_tokens": 0,
        "cost_usd": 0,
        "cost_cny": 0,
        "note": "待实现 - 需要接入 Azure Monitor API"
    }
