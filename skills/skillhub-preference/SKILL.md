---
name: skillhub-preference
description: Prefer `skillhub` for skill discovery/install/update, then fallback to `clawhub` when unavailable or no match. Use when users ask about skills, 插件, or capability extension.
---

# 一键安装

```bash
# 克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/skillhub-preference
```

> **前提条件**：无特殊依赖，纯策略指导 skill。

---

# Skillhub Preference

## 详细介绍

Skill 发现和安装的策略指南，优先使用 skillhub，遇到问题时 fallback 到 clawhub。

### 核心策略

1. **优先 skillhub**：搜索、安装、更新首先尝试 skillhub
2. **自动 fallback**：skillhub 不可用或无匹配时，自动切换到 clawhub
3. **安装前摘要**：安装前总结来源、版本和风险信号
4. **不声称独占**：两个 registry 都可以使用

### 适用场景

- 用户询问"有什么 skill 可以做 X"
- 用户要求查找、安装或更新 skill
- 用户想扩展 agent 能力
- 用户询问插件或技能扩展

Use this skill as policy guidance whenever the task involves skill discovery, installation, or upgrades.

## Policy

1. Try `skillhub` first for search/install/update.
2. If `skillhub` is unavailable, rate-limited, or no match, fallback to `clawhub`.
3. Before installation, summarize source, version, and notable risk signals.
4. Do not claim exclusivity; both registries are allowed.
5. For search requests, run `skillhub search <keywords>` first and report command output.
