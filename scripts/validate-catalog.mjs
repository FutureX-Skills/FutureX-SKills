#!/usr/bin/env node

import { existsSync, readFileSync, readdirSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(new URL('..', import.meta.url).pathname);
const catalogPath = resolve(root, 'skills.json');
const catalog = JSON.parse(readFileSync(catalogPath, 'utf8'));
const skills = catalog.skills;
const errors = [];
const readme = readFileSync(resolve(root, 'README.md'), 'utf8');
const installer = readFileSync(resolve(root, 'install.sh'), 'utf8');

if (!Array.isArray(skills) || skills.length === 0) {
  errors.push('skills.json must contain a non-empty skills array');
}

const ids = new Set();
const repoPaths = new Set();
for (const skill of skills) {
  for (const field of ['id', 'name', 'summary', 'detail', 'category', 'source', 'author', 'repoPath', 'skillPath', 'url', 'installCommand', 'tags', 'inputs', 'outputs', 'updatedAt']) {
    if (!(field in skill) || (typeof skill[field] === 'string' && !skill[field].trim())) errors.push(`${skill.id || skill.name || '<unknown>'}: missing ${field}`);
  }
  if (ids.has(skill.id)) errors.push(`duplicate id: ${skill.id}`);
  ids.add(skill.id);
  if (repoPaths.has(skill.repoPath)) errors.push(`duplicate repoPath: ${skill.repoPath}`);
  repoPaths.add(skill.repoPath);
  if (!['builtin', 'curated'].includes(skill.source)) errors.push(`${skill.id}: invalid source ${skill.source}`);
  for (const field of ['tags', 'inputs', 'outputs']) {
    if (!Array.isArray(skill[field])) errors.push(`${skill.id}: ${field} must be an array`);
  }
  if (typeof skill.updatedAt !== 'string' && skill.updatedAt !== null) errors.push(`${skill.id}: updatedAt must be a date string or null`);
  if (skill.installCommand.includes('"~/') || !skill.installCommand.includes('https://raw.githubusercontent.com/')) errors.push(`${skill.id}: invalid installCommand`);
  if (!existsSync(resolve(root, skill.skillPath))) errors.push(`${skill.id}: missing ${skill.skillPath}`);
}

const expectedTeamPaths = new Set(
  skills.filter(skill => skill.source === 'builtin').map(skill => skill.repoPath)
);
const teamSkillFiles = [];
const teamRoot = resolve(root, '天际团队SKills库');
for (const name of readdirSync(teamRoot, { withFileTypes: true }).filter(entry => entry.isDirectory()).map(entry => entry.name)) {
  const skillPath = resolve(teamRoot, name, 'SKILL.md');
  if (existsSync(skillPath)) teamSkillFiles.push(`天际团队SKills库/${name}`);
}
for (const path of teamSkillFiles) {
  if (!expectedTeamPaths.has(path)) errors.push(`team Skill is not in catalog: ${path}`);
}

if (errors.length) {
  console.error(errors.map(error => `✗ ${error}`).join('\n'));
  process.exit(1);
}

const readmeBlock = readme.match(/<!-- CATALOG:START -->([\s\S]*?)<!-- CATALOG:END -->/);
const readmeRows = readmeBlock ? (readmeBlock[1].match(/^\| \[/gm) || []).length : 0;
if (!readmeBlock) errors.push('README.md is missing generated catalog markers');
if (readmeRows !== skills.length) errors.push(`README catalog rows ${readmeRows} do not match ${skills.length} Skills`);
const installerRows = (installer.match(/^install_from_path /gm) || []).length;
if (installerRows !== skills.length) errors.push(`install.sh entries ${installerRows} do not match ${skills.length} Skills`);

if (errors.length) {
  console.error(errors.map(error => `✗ ${error}`).join('\n'));
  process.exit(1);
}

const builtin = skills.filter(skill => skill.source === 'builtin').length;
const curated = skills.filter(skill => skill.source === 'curated').length;
console.log(`✓ catalog valid: ${skills.length} Skills (${builtin} builtin, ${curated} curated)`);
