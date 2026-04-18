---
name: github
description: "Interact with GitHub using the `gh` CLI. Use `gh issue`, `gh pr`, `gh run`, and `gh api` for issues, PRs, CI runs, and advanced queries."
---

# 一键安装

```bash
# 方式一：克隆仓库
git clone https://github.com/FutureX-Skills/FutureX-SKills.git ~/.openclaw/workspace/skills/github

# 方式二：复制 SKILL.md 到 skills 目录
# 将本文件复制到 ~/.openclaw/workspace/skills/github/SKILL.md
```

> **前提条件**：已安装 `gh` CLI 工具。详见 https://cli.github.com/

---

# GitHub Skill

## 详细介绍

本 skill 是 GitHub API 和 CLI 的封装工具，专注于一级市场投资研究场景中的 GitHub 数据获取需求。

### 核心能力

- **PR 与 CI 管理**：查看 PR 状态、CI 运行结果、失败日志
- **Issue 追踪**：搜索和管理 GitHub Issues
- **API 高级查询**：通过 `gh api` 访问任意 GitHub API 端点
- **结构化输出**：支持 `--json` 和 `--jq` 过滤，输出机器可读格式

### 适用场景

| 场景 | 命令示例 |
|------|---------|
| 检查某个 PR 的 CI 是否通过 | `gh pr checks 55 --repo owner/repo` |
| 查看最近的 Workflow 运行 | `gh run list --repo owner/repo --limit 10` |
| 获取某个 Run 的失败日志 | `gh run view <run-id> --repo owner/repo --log-failed` |
| 搜索某仓库的 Issue | `gh issue list --repo owner/repo --json number,title` |
| 获取 PR 的详细信息 | `gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'` |

### 使用限制

- 需要提前在 GitHub 完成认证 (`gh auth login`)
- 部分 API 端点有速率限制
- 未指定 `--repo` 时默认使用当前目录所属仓库

Use the `gh` CLI to interact with GitHub. Always specify `--repo owner/repo` when not in a git directory, or use URLs directly.

## Pull Requests

Check CI status on a PR:
```bash
gh pr checks 55 --repo owner/repo
```

List recent workflow runs:
```bash
gh run list --repo owner/repo --limit 10
```

View a run and see which steps failed:
```bash
gh run view <run-id> --repo owner/repo
```

View logs for failed steps only:
```bash
gh run view <run-id> --repo owner/repo --log-failed
```

## API for Advanced Queries

The `gh api` command is useful for accessing data not available through other subcommands.

Get PR with specific fields:
```bash
gh api repos/owner/repo/pulls/55 --jq '.title, .state, .user.login'
```

## JSON Output

Most commands support `--json` for structured output.  You can use `--jq` to filter:

```bash
gh issue list --repo owner/repo --json number,title --jq '.[] | "\(.number): \(.title)"'
```
