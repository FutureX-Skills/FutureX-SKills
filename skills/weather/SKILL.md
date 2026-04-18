---
name: weather
description: Get current weather and forecasts (no API key required).
homepage: https://wttr.in/:help
metadata: {"clawdbot":{"emoji":"🌤️","requires":{"bins":["curl"]}}}
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/weather

# 方式二：复制 SKILL.md 到 skills 目录
# 将本文件复制到 ~/.openclaw/workspace/skills/weather/SKILL.md
```

> **前提条件**：仅需 `curl`，无需任何 API Key，完全免费。

---

# Weather

## 详细介绍

免费的天气查询工具，集成 wttr.in 和 Open-Meteo 两个服务，无需任何 API Key 即可使用。

### 核心能力

- **即时天气查询**：输入城市名或机场代码，快速获取当前天气
- **多格式输出**：支持纯文本、JSON、PNG 图片等多种格式
- **天气预报**：支持未来几天的天气预报
- **完全免费**：无需注册、无需 API Key、无使用限制

### 适用场景

| 场景 | 命令 |
|------|------|
| 快速查询当前天气 | `curl -s "wttr.in/London?format=3"` → `London: ⛅️ +8°C` |
| 获取完整天气预报 | `curl -s "wttr.in/London?T"` |
| 获取 PNG 天气图 | `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png` |
| 编程式 JSON 查询 | `curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"` |

### 支持的位置格式

- 城市名：`wttr.in/New+York`
- 机场代码：`wttr.in/JFK`
- 地标建筑：`wttr.in/Eiffel+Tower`

### 输出格式代码

| 代码 | 含义 | 示例 |
|------|------|------|
| `%c` | 天气状况 | ⛅️ |
| `%t` | 温度 | +8°C |
| `%h` | 湿度 | 71% |
| `%w` | 风速 | ↙5km/h |
| `%l` | 位置 | London |

Two free services, no API keys needed.

## wttr.in (primary)

Quick one-liner:
```bash
curl -s "wttr.in/London?format=3"
# Output: London: ⛅️ +8°C
```

Compact format:
```bash
curl -s "wttr.in/London?format=%l:+%c+%t+%h+%w"
# Output: London: ⛅️ +8°C 71% ↙5km/h
```

Full forecast:
```bash
curl -s "wttr.in/London?T"
```

Format codes: `%c` condition · `%t` temp · `%h` humidity · `%w` wind · `%l` location · `%m` moon

Tips:
- URL-encode spaces: `wttr.in/New+York`
- Airport codes: `wttr.in/JFK`
- Units: `?m` (metric) `?u` (USCS)
- Today only: `?1` · Current only: `?0`
- PNG: `curl -s "wttr.in/Berlin.png" -o /tmp/weather.png`

## Open-Meteo (fallback, JSON)

Free, no key, good for programmatic use:
```bash
curl -s "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current_weather=true"
```

Find coordinates for a city, then query. Returns JSON with temp, windspeed, weathercode.

Docs: https://open-meteo.com/en/docs
