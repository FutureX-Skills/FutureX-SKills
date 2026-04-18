---
name: rate-limiter
description: API频率限制工具。使用滑动窗口算法实现线程安全的频率限制，防止API调用触发429限流。支持阻塞和非阻塞模式，内置飞书、OpenAI等常用API的预设配置。在需要进行API调用频率控制时使用此skill。
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/rate-limiter
```

> **前提条件**：Python3，无其他依赖。

---

# Rate Limiter - API频率限制器

## 详细介绍

线程安全的滑动窗口频率限制工具，防止 API 调用触发 429 限流错误。支持阻塞和非阻塞模式，以及多种预设的 API 限制配置。

### 核心能力

- **滑动窗口算法**：精确控制调用频率，自动清理过期记录
- **线程安全**：使用 threading.Lock 保证多线程安全
- **阻塞/非阻塞模式**：阻塞模式自动等待，非阻塞模式立即返回
- **预设配置**：内置飞书、OpenAI 等常用 API 的限制参数

### 适用场景

- 调用有速率限制的 API 时防止触发 429 错误
- 批量处理 API 请求时控制并发
- 管理多个 API 的不同频率限制

### 快速使用

```python
from scripts.rate_limiter import RateLimiter

# 每秒最多 5 次调用
rl = RateLimiter(max_calls=5, period=1.0)

# 阻塞等待模式（推荐）
for item in items:
    rl.acquire(block=True)
    result = api.call(item)

# 非阻塞模式
if rl.acquire(block=False):
    result = api.call(item)
else:
    print('限流中，跳过')
```

### 预设配置

```python
from scripts.rate_limiter import RateLimiter, FeishuLimits, OpenAILimits

# 飞书 API 限制
chat_rl = RateLimiter(*FeishuLimits.CHAT_MESSAGE)      # 50次/秒
file_rl = RateLimiter(*FeishuLimits.FILE_UPLOAD)        # 5次/秒

# OpenAI API 限制
gpt4_rl = RateLimiter(*OpenAILimits.GPT4_PER_MINUTE)   # 60次/分钟
gpt35_rl = RateLimiter(*OpenAILimits.GPT35_PER_MINUTE) # 200次/分钟
```

线程安全的滑动窗口频率限制，防止API调用触发429限流。

## 快速开始

```python
from scripts.rate_limiter import RateLimiter

# 每秒最多5次调用
rl = RateLimiter(max_calls=5, period=1.0)

# 方式1: 阻塞等待（推荐）
for item in items:
    rl.acquire(block=True)
    result = api.call(item)

# 方式2: 非阻塞（立即返回是否成功）
if rl.acquire(block=False):
    result = api.call(item)
else:
    print('限流中，跳过')

# 方式3: 使用上下文管理器
with RateLimiter(10, 1):
    result = api.call()
```

## 预设配置

### 飞书API限制
```python
from scripts.rate_limiter import RateLimiter, FeishuLimits

chat_rl = RateLimiter(*FeishuLimits.CHAT_MESSAGE)      # 50次/秒
file_rl = RateLimiter(*FeishuLimits.FILE_UPLOAD)       # 5次/秒
contact_rl = RateLimiter(*FeishuLimits.CONTACT)        # 20次/秒
```

### OpenAI API限制
```python
from scripts.rate_limiter import RateLimiter, OpenAILimits

gpt4_rl = RateLimiter(*OpenAILimits.GPT4_PER_MINUTE)      # 60次/分钟
gpt35_rl = RateLimiter(*OpenAILimits.GPT35_PER_MINUTE)    # 200次/分钟
```

## 参数说明

| 参数 | 类型 | 说明 |
|------|------|------|
| max_calls | int | 时间窗口内最大调用次数 |
| period | float | 时间窗口（秒） |
| block | bool | 是否阻塞等待 |
| timeout | float | 阻塞模式下的最大等待时间（秒） |

## 实现细节

- **滑动窗口算法**: 自动清理过期调用记录，精确控制频率
- **线程安全**: 使用threading.Lock保证多线程安全
- **精度**: 默认0.05秒轮询间隔，可手动调整
