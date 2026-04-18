#!/usr/bin/env python3
"""
反爬网页访问工具 - 自动降级策略
使用方法: python fetch.py <url> [--output file.html]
"""

import sys
import subprocess
import argparse
import shutil

def method1_distil(url):
    """distil.net代理（最快）

    注意：distil.net 的开放代理端点在某些环境/时期可能不可用（可能返回 404）。
    这种情况应直接降级到 method2/method3。
    """
    try:
        # 先探测 HTTP 状态，404 直接视为不可用
        probe = subprocess.run(
            ['curl', '-sS', '-I', '-L', '--max-time', '20', f'https://distil.net/url/{url}'],
            capture_output=True,
            text=True,
            timeout=25
        )
        if ' 404' in (probe.stdout or ''):
            return None

        result = subprocess.run(
            ['curl', '-sS', '-L', '--max-time', '30', f'https://distil.net/url/{url}'],
            capture_output=True,
            text=True,
            timeout=35
        )
        if result.returncode == 0 and len(result.stdout) > 100:
            return result.stdout
    except Exception:
        pass
    return None

def method2_curl(url):
    """curl模拟浏览器"""
    try:
        result = subprocess.run([
            'curl', '-sL', '--max-time', '30',
            '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            '-H', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            '-H', 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8',
            '-H', 'Accept-Encoding: gzip, deflate, br',
            '-H', 'DNT: 1',
            '-H', 'Connection: keep-alive',
            '--compressed',
            url
        ], capture_output=True, text=True, timeout=35)
        if result.returncode == 0 and len(result.stdout) > 100:
            return result.stdout
    except Exception:
        pass
    return None

def method3_playwright(url):
    """Playwright无头浏览器（最强）"""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            )
            page.goto(url, wait_until='networkidle', timeout=30000)
            content = page.content()
            browser.close()
            return content
    except ImportError:
        print("Playwright未安装，跳过方法3", file=sys.stderr)
    except Exception as e:
        print(f"Playwright失败: {e}", file=sys.stderr)
    return None

def fetch(url, use_playwright=False):
    """主获取函数，自动降级"""
    # 方法1: distil代理
    print("尝试方法1: distil代理...", file=sys.stderr)
    result = method1_distil(url)
    if result:
        return result
    
    # 方法2: curl模拟UA
    print("方法1失败，尝试方法2: curl模拟浏览器...", file=sys.stderr)
    result = method2_curl(url)
    if result:
        return result
    
    # 方法3: Playwright（如果启用）
    if use_playwright:
        print("方法2失败，尝试方法3: Playwright...", file=sys.stderr)
        result = method3_playwright(url)
        if result:
            return result
    
    raise Exception("所有方法均失败")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='反爬网页访问工具')
    parser.add_argument('url', help='目标URL')
    parser.add_argument('-o', '--output', help='输出文件（默认stdout）')
    parser.add_argument('--playwright', action='store_true', help='启用Playwright（需安装）')
    
    args = parser.parse_args()
    
    try:
        content = fetch(args.url, use_playwright=args.playwright)
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"已保存到: {args.output}")
        else:
            print(content)
    except Exception as e:
        print(f"错误: {e}", file=sys.stderr)
        sys.exit(1)
