#!/usr/bin/env python3
"""
Patch Feishu media.ts to auto-convert audio files (mp3, wav, etc.) to opus
for voice bubble delivery. Without this patch, TTS audio arrives as file
attachments instead of native Feishu voice bubbles.

Usage: python3 patch_media.py [--openclaw-root <path>]

Idempotent — safe to run multiple times. Re-run after `npm update openclaw`.
"""
import argparse
import os
import re
import subprocess
import sys

# --- Patch content ---

IMPORTS_PATCH = '''\
import { execFile } from "child_process";
import { promisify } from "util";
'''

CONVERSION_FUNCTION = '''\

const execFileAsync = promisify(execFile);

/** Audio extensions that should be converted to opus for voice bubble delivery */
const CONVERTIBLE_AUDIO_EXTS = new Set([".mp3", ".m4a", ".wav", ".webm", ".aac", ".flac"]);

/**
 * Convert an audio buffer to opus format via ffmpeg for Feishu voice bubbles.
 * Returns the opus buffer, or null if conversion fails.
 */
async function convertToOpusBuffer(inputBuffer: Buffer, inputExt: string): Promise<Buffer | null> {
  const tmpDir = (await import("os")).tmpdir();
  const id = `feishu-voice-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`;
  const inputPath = path.join(tmpDir, `${id}${inputExt}`);
  const outputPath = path.join(tmpDir, `${id}.opus`);

  try {
    fs.writeFileSync(inputPath, inputBuffer);
    await execFileAsync("ffmpeg", [
      "-y", "-i", inputPath,
      "-vn", "-sn", "-dn",
      "-c:a", "libopus",
      "-b:a", "64k",
      outputPath,
    ], { timeout: 30_000 });
    const opusBuffer = fs.readFileSync(outputPath);
    return opusBuffer.length > 0 ? opusBuffer : null;
  } catch (err) {
    console.error("[feishu] ffmpeg opus conversion failed:", err);
    return null;
  } finally {
    try { fs.unlinkSync(inputPath); } catch {}
    try { fs.unlinkSync(outputPath); } catch {}
  }
}
'''

# The code that replaces the original sendMediaFeishu else-branch
SEND_MEDIA_PATCH_OLD = '''\
  } else {
    const fileType = detectFileType(name);
    const { fileKey } = await uploadFileFeishu({'''

SEND_MEDIA_PATCH_NEW = '''\
  } else {
    let fileType = detectFileType(name);

    // Auto-convert audio files (mp3, wav, etc.) to opus for voice bubble delivery
    if (fileType !== "opus" && CONVERTIBLE_AUDIO_EXTS.has(ext)) {
      const opusBuf = await convertToOpusBuffer(buffer, ext);
      if (opusBuf) {
        buffer = opusBuf;
        name = name.replace(/\\.[^.]+$/, ".opus");
        fileType = "opus";
      }
    }

    const { fileKey } = await uploadFileFeishu({'''

SENTINEL = "CONVERTIBLE_AUDIO_EXTS"


def find_openclaw_root():
    """Find the global npm openclaw package root."""
    try:
        result = subprocess.run(
            ["npm", "root", "-g"],
            capture_output=True, text=True, check=True
        )
        npm_root = result.stdout.strip()
        return os.path.join(npm_root, "openclaw")
    except (subprocess.CalledProcessError, FileNotFoundError):
        # Fallback: common macOS path
        fallback = "/usr/local/lib/node_modules/openclaw"
        if os.path.isdir(fallback):
            return fallback
        return None


def patch_media(openclaw_root: str) -> bool:
    media_path = os.path.join(
        openclaw_root, "extensions", "feishu", "src", "media.ts"
    )

    if not os.path.isfile(media_path):
        print(f"ERROR: media.ts not found at {media_path}", file=sys.stderr)
        print("Is the Feishu plugin installed?", file=sys.stderr)
        return False

    with open(media_path, "r") as f:
        content = f.read()

    # Check if already patched
    if SENTINEL in content:
        print(f"Already patched: {media_path}")
        return True

    # --- Step 1: Add imports at top ---
    # Insert before the first 'import' line
    if 'import { execFile }' not in content:
        content = IMPORTS_PATCH + content

    # --- Step 2: Add conversion function after imports ---
    # Find the line with 'import { resolveFeishuAccount }' and insert before it
    marker = 'import { resolveFeishuAccount }'
    if marker in content:
        content = content.replace(
            marker,
            CONVERSION_FUNCTION + marker
        )
    else:
        # Fallback: insert after all import lines
        lines = content.split('\n')
        last_import_idx = 0
        for i, line in enumerate(lines):
            if line.startswith('import '):
                last_import_idx = i
        lines.insert(last_import_idx + 1, CONVERSION_FUNCTION)
        content = '\n'.join(lines)

    # --- Step 3: Patch sendMediaFeishu to use conversion ---
    if SEND_MEDIA_PATCH_OLD in content:
        content = content.replace(SEND_MEDIA_PATCH_OLD, SEND_MEDIA_PATCH_NEW)
    else:
        print("WARNING: Could not find sendMediaFeishu patch target.", file=sys.stderr)
        print("The function signature may have changed in this version.", file=sys.stderr)
        print("Manual patching may be required.", file=sys.stderr)
        return False

    # --- Write patched file ---
    with open(media_path, "w") as f:
        f.write(content)

    print(f"Patched: {media_path}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Patch Feishu media.ts for voice bubble support"
    )
    parser.add_argument(
        "--openclaw-root",
        help="Path to openclaw package root (auto-detected if omitted)"
    )
    args = parser.parse_args()

    root = args.openclaw_root or find_openclaw_root()
    if not root or not os.path.isdir(root):
        print("ERROR: Could not find openclaw installation.", file=sys.stderr)
        print("Specify with: --openclaw-root /path/to/openclaw", file=sys.stderr)
        sys.exit(1)

    print(f"OpenClaw root: {root}")
    success = patch_media(root)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
