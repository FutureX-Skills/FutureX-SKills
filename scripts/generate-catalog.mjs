#!/usr/bin/env node

import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const catalog = JSON.parse(readFileSync(resolve(root, 'skills.json'), 'utf8'));
const skills = catalog.skills;
const sourceLabel = source => source === 'builtin' ? '天际自建' : '外部精选';
const markdown = value => String(value || '').replaceAll('|', '\\|');

const readmeBlock = [
  '<!-- CATALOG:START -->',
  '## 📚 Skill 清单（由 `skills.json` 生成）',
  '',
  `当前目录共 **${skills.length}** 个 Skills：天际自建 ${skills.filter(skill => skill.source === 'builtin').length} 个，外部精选 ${skills.filter(skill => skill.source === 'curated').length} 个。`,
  '',
  '| Skill | 分类 | 来源 | 仓库路径 |',
  '|------|------|------|----------|',
  ...skills.map(skill => `| [${markdown(skill.name)}](${encodeURI(skill.url)}) | ${markdown(skill.category)} | ${sourceLabel(skill.source)} | \`${markdown(skill.repoPath)}\` |`),
  '',
  '> 这部分由 `node scripts/generate-catalog.mjs` 生成，请修改 `skills.json` 后再运行生成脚本。',
  '<!-- CATALOG:END -->'
].join('\n');

const installBlock = [
  '# CATALOG:START',
  'echo "📦 安装 FutureX Skills（${ONLY_SKILL:-全部}）..."',
  ...skills.map(skill => `install_from_path ${JSON.stringify(skill.repoPath)} ${JSON.stringify(skill.id)}`),
  '# CATALOG:END'
].join('\n');

const readmePath = resolve(root, 'README.md');
const readme = readFileSync(readmePath, 'utf8');
const readmePattern = /<!-- CATALOG:START -->[\s\S]*?<!-- CATALOG:END -->/;
if (!readmePattern.test(readme)) throw new Error('README.md is missing CATALOG markers');
writeFileSync(readmePath, readme.replace(readmePattern, readmeBlock) + (readme.endsWith('\n') ? '' : '\n'));

const installer = `#!/bin/bash
# FutureX Skills 一键安装脚本
# Usage: curl -fsSL https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main/install.sh | bash
# Install one Skill: curl -fsSL .../install.sh | bash -s -- <skill-id>

set -u
AGENTS_DIR="\${AGENTS_DIR:-\$HOME/.agents/skills}"
ONLY_SKILL="\${1:-}"
RAW_BASE="https://raw.githubusercontent.com/FutureX-Skills/FutureX-SKills/main"

install_from_path() {
    local REPO_PATH="$1"
    local SKILL_NAME="$2"
    if [ -n "$ONLY_SKILL" ] && [ "$ONLY_SKILL" != "$SKILL_NAME" ]; then return 0; fi
    local TARGET="$AGENTS_DIR/$SKILL_NAME"
    local SKILL_SOURCE="$REPO_PATH/SKILL.md"
    if [[ "$REPO_PATH" == *.md ]]; then SKILL_SOURCE="$REPO_PATH"; fi

    if [ -f "$TARGET/SKILL.md" ]; then
        echo "⏭  $SKILL_NAME 已安装，跳过"
        return 0
    fi

    mkdir -p "$TARGET"
    if ! curl -fsSL "$RAW_BASE/$SKILL_SOURCE" -o "$TARGET/SKILL.md"; then
        echo "❌ $SKILL_NAME 安装失败"
        rm -rf "$TARGET"
        return 1
    fi
    if [[ "$REPO_PATH" != *.md ]]; then
        curl -fsSL "$RAW_BASE/$REPO_PATH/README.md" -o "$TARGET/README.md" 2>/dev/null || true
    fi
    echo "✅ $SKILL_NAME 安装完成"
}

${installBlock}

if [ -z "$ONLY_SKILL" ] || [ "$ONLY_SKILL" = "fx-wechat-formatter" ]; then
    FX_FORMATTER_DIR="$AGENTS_DIR/fx-wechat-formatter"
    if [ -f "$FX_FORMATTER_DIR/SKILL.md" ]; then
        mkdir -p "$FX_FORMATTER_DIR/scripts"
        curl -fsSL "$RAW_BASE/天际团队SKills库/fx-wechat-formatter/scripts/build_docx.js" -o "$FX_FORMATTER_DIR/scripts/build_docx.js" || true
    fi
fi

echo "🎉 安装流程完成！"
`;
writeFileSync(resolve(root, 'install.sh'), installer);
