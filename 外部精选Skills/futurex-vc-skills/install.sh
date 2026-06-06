#!/usr/bin/env bash
set -euo pipefail

REPO="${FUTUREX_VC_REPO:-CharlesWu17/futurex-vc-skills}"
REF="${FUTUREX_VC_REF:-main}"
SKILL_PATH="${FUTUREX_VC_SKILL_PATH:-codex-skills/futurex-vc}"
SKILL_NAME="${FUTUREX_VC_SKILL_NAME:-futurex-vc}"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
DEST_ROOT="$CODEX_HOME/skills"
DEST="$DEST_ROOT/$SKILL_NAME"
INSTALLER="$CODEX_HOME/skills/.system/skill-installer/scripts/install-skill-from-github.py"

say() {
  printf "%s\n" "$*"
}

die() {
  printf "Error: %s\n" "$*" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"
}

find_python() {
  if [ -n "${PYTHON:-}" ] && command -v "$PYTHON" >/dev/null 2>&1; then
    printf "%s\n" "$PYTHON"
    return 0
  fi

  for candidate in python3 python py; do
    if command -v "$candidate" >/dev/null 2>&1; then
      printf "%s\n" "$candidate"
      return 0
    fi
  done

  return 1
}

if [ -d "$DEST" ]; then
  if [ "${FORCE:-0}" != "1" ]; then
    say "FutureX VC skill is already installed at $DEST"
    say "Restart Codex if you just installed it."
    say "To reinstall or update, run:"
    say "curl -fsSL https://raw.githubusercontent.com/${REPO}/main/install.sh | FORCE=1 bash"
    exit 0
  fi

  BACKUP="${DEST}.backup.$(date +%Y%m%d%H%M%S)"
  say "Existing installation found. Moving it to $BACKUP"
  mv "$DEST" "$BACKUP"
fi

mkdir -p "$DEST_ROOT"

if [ -f "$INSTALLER" ] && PYTHON_BIN="$(find_python)"; then
  say "Installing FutureX VC with Codex skill installer..."
  "$PYTHON_BIN" "$INSTALLER" \
    --repo "$REPO" \
    --ref "$REF" \
    --path "$SKILL_PATH"
else
  say "Codex skill installer not found; installing directly from GitHub archive..."
  need_cmd curl
  need_cmd tar
  need_cmd find
  need_cmd cp

  TMP_DIR="$(mktemp -d)"
  trap 'rm -rf "$TMP_DIR"' EXIT

  ARCHIVE="$TMP_DIR/repo.tar.gz"
  curl -fsSL "https://codeload.github.com/${REPO}/tar.gz/${REF}" -o "$ARCHIVE"
  tar -xzf "$ARCHIVE" -C "$TMP_DIR"

  REPO_DIR="$(find "$TMP_DIR" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
  [ -n "$REPO_DIR" ] || die "Downloaded archive layout was not recognized."

  SRC="$REPO_DIR/$SKILL_PATH"
  [ -f "$SRC/SKILL.md" ] || die "SKILL.md not found in $SKILL_PATH."

  cp -R "$SRC" "$DEST"
fi

[ -f "$DEST/SKILL.md" ] || die "Install failed: $DEST/SKILL.md was not created."

say "Installed $SKILL_NAME to $DEST"
say "Restart Codex to pick up the skill."
