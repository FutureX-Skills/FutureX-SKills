# skill-creator

Anthropic 官方 Skill 构建工具，用于从零创建新技能、对现有技能进行迭代优化，以及通过量化评估测量技能表现。

---

## 🎯 技能介绍

**skill-creator** 是 Anthropic 官方出品的 AI 技能开发框架，帮你完成以下工作：

- **从零构建技能**：将工作流或想法转化为可复用的 Claude Code Skill
- **优化现有技能**：改进技能的触发准确性和执行效果
- **量化评估**：运行基准测试，对比不同版本的技能表现
- **描述优化**：自动优化技能触发词，提升命中精度

### 核心流程

1. **Capture Intent** — 理解需求，提取对话中的工作流
2. **Write Draft** — 编写技能初稿
3. **Build Evals** — 构建测试用例和量化评估集
4. **Run & Iterate** — 运行测试，根据反馈迭代优化
5. **Expand Scale** — 扩大测试集，验证泛化能力

---

## ⚡ 一键安装

在 Claude Code 会话中运行：

```bash
npx skills.sh install https://github.com/FutureX-Skills/FutureX-SKills/tree/main/外部精选Skills/skill-creator
```

安装完成后，在 Claude Code 中说「创建一个skill」或「帮我写一个技能」，skill-creator 会自动激活。

---

## 📁 目录结构

```
skill-creator/
├── SKILL.md          # 技能核心定义文件
├── agents/           # Agent 提示词模板
├── eval-viewer/      # 评估结果可视化脚本
├── references/        # 参考文档
├── scripts/          # 辅助脚本
└── assets/           # 静态资源
```

---

## 📖 详细文档

- 完整使用指南 → 查看 [SKILL.md](./SKILL.md)
- 评估系统 → 查看 [eval-viewer/README.md](./eval-viewer/README.md)
- Anthropic 官方技能库 → [github.com/anthropics/skills](https://github.com/anthropics/skills)
