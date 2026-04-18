---
name: anti-crawl
description: 反爬网页访问工具。针对有反爬机制的网站（微信公众号、Twitter、Reddit等），提供三种自动降级的访问策略：distil代理→curl模拟UA→Playwright无头浏览器。在web_fetch失败或需要抓取反爬网站时使用此skill。
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/anti-crawl
```

> **前提条件**：Python3 + pip。可选 Playwright 用于 JS 渲染页面。

---

# Anti-Crawl - 反爬网页访问

## 详细介绍

针对有反爬机制的网站（如微信公众号、Twitter、Reddit、知乎等）设计的访问工具，提供三种自动降级策略，确保能够成功获取目标内容。

### 核心能力

- **三级自动降级**：distil.net 代理 → curl 模拟 UA → Playwright 无头浏览器
- **支持主流反爬网站**：微信公众号、Twitter/X、Reddit、知乎、小红书等
- **无需 API Key**：完全免费使用
- **Python API**：可集成到其他 Python 项目中

### 三种方法对比

| 方法 | 策略 | 速度 | 依赖 |
|------|------|------|------|
| 1 | distil.net 代理 | 最快 | curl |
| 2 | curl 模拟浏览器 UA | 快 | curl |
| 3 | Playwright 无头浏览器 | 较慢 | playwright |

### 适用场景

- 微信公众号文章无法直接抓取时
- Twitter/X 页面内容获取失败时
- Reddit 内容无法访问时
- 任何 `web_fetch` 失败的页面

### 快速使用

```bash
# 基础用法（自动降级）
python3 scripts/fetch.py "https://mp.weixin.qq.com/s/xxxxx"

# 保存到文件
python3 scripts/fetch.py "https://target.com" -o output.html

# 启用 Playwright（处理 JS 渲染）
python3 scripts/fetch.py "https://target.com" --playwright
```

针对有反爬机制的网站，自动降级的三种访问策略。

## 快速开始

```bash
# 基础用法（自动降级）
python3 scripts/fetch.py "https://mp.weixin.qq.com/s/xxxxx"

# 保存到文件
python3 scripts/fetch.py "https://target.com" -o output.html

# 启用Playwright（处理JS渲染）
python3 scripts/fetch.py "https://target.com" --playwright
```

## 三种方法

| 方法 | 策略 | 速度 | 依赖 |
|------|------|------|------|
| 1 | distil.net代理 | 最快 | curl |
| 2 | curl模拟浏览器UA | 快 | curl |
| 3 | Playwright无头浏览器 | 较慢 | playwright |

## 支持网站

- ✅ 微信公众号（mp.weixin.qq.com）
- ✅ Twitter/X
- ✅ Reddit
- ✅ 知乎、小红书
- ✅ 任何 web_fetch 失败的页面

## Python 调用

```python
import sys
sys.path.insert(0, 'scripts')
from fetch import fetch

# 基础调用（方法1+2）
html = fetch("https://target-url.com")

# 启用Playwright
html = fetch("https://target-url.com", use_playwright=True)
```

## 安装 Playwright（可选）

如需处理JS渲染页面：

```bash
pip install playwright
playwright install chromium
```

## 注意事项

- 遵守目标网站 robots.txt
- 高频请求间隔1-2秒避免封IP
- 完全免费，无需API Key
