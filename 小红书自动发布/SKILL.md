---
name: xiaohongshu-publish
description: 小红书自动化发布 skill，基于 xiaohongshu-mcp + MCPorter，支持一键发布图文笔记，包含图片上传、标题填写、正文填写、标签设置的完整流程。适用于需要自动化发布小红书内容的场景。
---

# 小红书自动发布 Skill

## 快速开始

### 前置条件

1. xiaohongshu-mcp 服务已部署并运行
2. 小红书账号已登录（通过 xiaohongshu-login）
3. MCPorter 已安装配置

### 一键发布

```bash
npx mcporter call xiaohongshu-mcp.publish_content \
  --args "$(cat publish_args.json)"
```

**publish_args.json 示例**:
```json
{
  "title": "笔记标题（≤20字）",
  "content": "笔记正文内容",
  "images": ["/path/to/image.jpg"],
  "tags": ["标签1", "标签2", "标签3"],
  "visibility": "公开可见"
}
```

---

## 最佳实践

### 📝 标题
- 字数限制：≤20 个中文字符
- 建议包含关键词，吸引点击

### 🖼️ 图片
- 推荐尺寸：3:4（竖屏）
- 支持格式：JPG、PNG
- 数量：至少 1 张，不超过 9 张
- 建议使用英文路径，避免中文路径问题

### 🏷️ 标签
- **数量建议**：3-4 个最佳，避免过多
- **选择建议**：优先选高频、常见的标签（如："宠物"、"搞笑"、"日常"）
- **稳定性**：避免标签联想下拉框问题导致发布失败

### 👁️ 可见范围
- 建议显式设置：`"公开可见"`
- 可选值：`"公开可见"`、`"仅自己可见"`、`"好友圈可见"`

---

## 成功案例

### 发布参数（成功版本）
```json
{
  "title": "养了4只小龙虾，想选个小三被拒了",
  "content": "养了4只小龙虾，给它们设定角色的时候，想安排其中一只当我梦寐以求的\"小三\"，结果被它无情拒绝了 🦞💔 现在的小龙虾都这么有原则的吗？",
  "images": ["/Users/ben/.openclaw/workspace/crayfish.jpg"],
  "tags": ["小龙虾", "宠物", "搞笑"],
  "visibility": "公开可见"
}
```

### 发布结果
- ✅ 图片上传成功
- ✅ 标题填写成功
- ✅ 正文填写成功
- ✅ 标签点击成功（全部3个标签）
- ✅ 可见范围设置成功
- ✅ 最终发布成功！

---

## 故障排查

### 问题 1：PostID 为空但显示"发布完成"
**原因**：最后一步点击发布按钮可能失败，或者工具返回状态与实际不符

**解决**：
1. 检查小红书 App 确认笔记是否真的发布
2. 尝试减少标签数量（3-4 个）
3. 使用更常见、高频的标签

### 问题 2：标签点击失败
**原因**：标签联想下拉框不稳定，某些标签的联想选项可能不可用

**解决**：
1. 减少标签数量
2. 使用更常见的标签（如："日常"、"宠物"、"搞笑"）
3. 避免过于细分或小众的标签

### 问题 3：图片上传失败
**原因**：中文路径问题、图片格式不支持、图片尺寸过大

**解决**：
1. 使用英文路径（如：`/path/to/image.jpg` 而非 `/路径/图片.jpg`）
2. 检查图片格式（推荐 JPG/PNG）
3. 尝试压缩图片大小

---

## 技术架构

| 组件 | 用途 |
|------|------|
| xiaohongshu-mcp | HTTP MCP 服务，提供 13 个工具（包括 publish_content） |
| MCPorter | MCP 客户端，自动处理会话初始化和协议细节 |
| Chromium | 浏览器自动化，用于登录和发布操作 |

---

## 相关资源

- xiaohongshu-mcp GitHub: https://github.com/xpzouying/xiaohongshu-mcp
- MCPorter GitHub: https://github.com/modelcontextprotocol/mcporter
