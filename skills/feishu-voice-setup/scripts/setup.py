#!/usr/bin/env python3
"""
Feishu Voice I/O Setup — One-command onboarding for voice input/output.

Usage: python3 setup.py [--voice <edge-tts-voice>] [--tts-auto <mode>]

What it does:
  1. Checks prerequisites (OpenClaw >= 2026.3.x, ffmpeg, edge-tts)
  2. Installs edge-tts if missing
  3. Applies config changes to ~/.openclaw/openclaw.json
  4. Patches Feishu media.ts for MP3→Opus auto-conversion
  5. Restarts the gateway
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys

CONFIG_PATH = os.path.expanduser("~/.openclaw/openclaw.json")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── Helpers ───────────────────────────────────────────────────────────

def run(cmd, check=True, capture=True):
    """Run a shell command and return stdout."""
    result = subprocess.run(
        cmd, shell=isinstance(cmd, str),
        capture_output=capture, text=True
    )
    if check and result.returncode != 0:
        stderr = result.stderr.strip() if capture else ""
        raise RuntimeError(f"Command failed: {cmd}\n{stderr}")
    return result.stdout.strip() if capture else ""


def has_bin(name):
    return shutil.which(name) is not None


def print_step(n, text):
    print(f"\n{'='*50}")
    print(f"  Step {n}: {text}")
    print(f"{'='*50}")


def print_ok(msg):
    print(f"  OK  {msg}")


def print_warn(msg):
    print(f"  WARN  {msg}")


def print_fail(msg):
    print(f"  FAIL  {msg}")

# ─── Step 1: Check prerequisites ──────────────────────────────────────

def check_prerequisites():
    print_step(1, "Checking prerequisites")
    ok = True

    # OpenClaw version
    try:
        ver = run("openclaw --version")
        # Extract version like "2026.3.2"
        m = re.search(r'(\d{4})\.(\d+)\.(\d+)', ver)
        if m:
            year, major = int(m.group(1)), int(m.group(2))
            if year >= 2026 and major >= 3:
                print_ok(f"OpenClaw {m.group(0)}")
            else:
                print_fail(f"OpenClaw {m.group(0)} — need >= 2026.3.x")
                print("       Run: npm update -g openclaw")
                ok = False
        else:
            print_warn(f"Could not parse version: {ver}")
    except Exception:
        print_fail("openclaw not found on PATH")
        ok = False

    # ffmpeg
    if has_bin("ffmpeg"):
        try:
            ffver = run("ffmpeg -version")
            first_line = ffver.split('\n')[0] if ffver else "unknown"
            print_ok(f"ffmpeg ({first_line[:60]})")
        except Exception:
            print_ok("ffmpeg found")
    else:
        print_fail("ffmpeg not found")
        print("       Install: brew install ffmpeg (macOS) / apt install ffmpeg (Linux)")
        ok = False

    # edge-tts — check both PATH and python module
    edge_tts_found = has_bin("edge-tts")
    if not edge_tts_found:
        # Check if importable even if CLI not on PATH
        try:
            run(f"{sys.executable} -c 'import edge_tts'", check=True)
            edge_tts_found = True
        except Exception:
            pass

    if edge_tts_found:
        print_ok("edge-tts installed")
    else:
        print_warn("edge-tts not found — will install")
        try:
            run(f"{sys.executable} -m pip install edge-tts", check=True, capture=False)
            print_ok("edge-tts installed successfully")
        except Exception as e:
            print_fail(f"Failed to install edge-tts: {e}")
            print("       Install manually: pip3 install edge-tts")
            ok = False

    return ok

# ─── Step 2: Apply config changes ─────────────────────────────────────

def apply_config(voice: str, tts_auto: str):
    print_step(2, "Applying config changes")

    if not os.path.isfile(CONFIG_PATH):
        print_fail(f"Config not found: {CONFIG_PATH}")
        return False

    with open(CONFIG_PATH, "r") as f:
        cfg = json.load(f)

    changes = []

    # tools.media.audio.enabled
    tools = cfg.setdefault("tools", {})
    media = tools.setdefault("media", {})
    audio = media.setdefault("audio", {})
    if not audio.get("enabled"):
        audio["enabled"] = True
        changes.append("tools.media.audio.enabled = true")

    # messages.tts
    messages = cfg.setdefault("messages", {})
    tts = messages.get("tts", {})
    need_tts_update = (
        tts.get("auto") != tts_auto
        or tts.get("provider") != "edge"
        or tts.get("edge", {}).get("voice") != voice
        or tts.get("edge", {}).get("lang") != "zh-CN"
    )
    if need_tts_update:
        messages["tts"] = {
            **tts,  # preserve any extra keys
            "auto": tts_auto,
            "provider": "edge",
            "edge": {
                **tts.get("edge", {}),  # preserve extra edge keys
                "voice": voice,
                "lang": "zh-CN",
            },
        }
        changes.append(f"messages.tts.auto = \"{tts_auto}\"")
        changes.append(f"messages.tts.edge.voice = \"{voice}\"")

    if changes:
        # Backup
        backup_path = CONFIG_PATH + ".bak"
        shutil.copy2(CONFIG_PATH, backup_path)

        with open(CONFIG_PATH, "w") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
            f.write("\n")

        for c in changes:
            print_ok(c)
        print(f"  Backup saved to {backup_path}")
    else:
        print_ok("Config already up to date")

    return True

# ─── Step 3: Patch media.ts ────────────────────────────────────────────

def patch_media():
    print_step(3, "Patching Feishu media.ts for opus conversion")

    patch_script = os.path.join(SCRIPT_DIR, "patch_media.py")
    result = subprocess.run(
        [sys.executable, patch_script],
        capture_output=True, text=True
    )
    for line in result.stdout.strip().split('\n'):
        if line:
            print(f"  {line}")
    if result.returncode != 0:
        for line in result.stderr.strip().split('\n'):
            if line:
                print(f"  {line}")
        return False
    return True

# ─── Step 4: Restart gateway ──────────────────────────────────────────

def restart_gateway():
    print_step(4, "Restarting gateway")
    try:
        result = subprocess.run(
            ["openclaw", "gateway", "restart"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            print_ok("Gateway restarted")
            return True
        else:
            print_warn("Gateway restart returned non-zero")
            print(f"  {result.stderr.strip()[:200]}")
            return True  # Non-fatal
    except subprocess.TimeoutExpired:
        print_warn("Gateway restart timed out (may still be starting)")
        return True
    except FileNotFoundError:
        print_warn("openclaw command not found — restart manually")
        return True

# ─── Main ──────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Feishu Voice I/O Setup"
    )
    parser.add_argument(
        "--voice", default="zh-CN-YunxiNeural",
        help="Edge TTS voice (default: zh-CN-YunxiNeural)"
    )
    parser.add_argument(
        "--tts-auto", default="inbound",
        choices=["off", "always", "inbound", "tagged"],
        help="TTS auto mode (default: inbound)"
    )
    parser.add_argument(
        "--no-restart", action="store_true",
        help="Skip gateway restart"
    )
    args = parser.parse_args()

    print("Feishu Voice I/O Setup")
    print("=" * 50)

    # Step 1
    prereqs_ok = check_prerequisites()
    if not prereqs_ok:
        print("\nPrerequisite check failed. Fix issues above and re-run.")
        sys.exit(1)

    # Step 2
    config_ok = apply_config(args.voice, args.tts_auto)
    if not config_ok:
        sys.exit(1)

    # Step 3
    patch_ok = patch_media()
    if not patch_ok:
        print("\nMedia patch failed. Voice will be sent as file attachments.")
        print("You can try running patch_media.py manually.")

    # Step 4
    if not args.no_restart:
        restart_gateway()

    # Summary
    print(f"\n{'='*50}")
    print("  Setup Complete!")
    print(f"{'='*50}")
    print()
    print("Voice Output (TTS):")
    print(f"  Voice: {args.voice}")
    print(f"  Auto mode: {args.tts_auto}")
    print(f"  Provider: Edge TTS (free)")
    print()
    print("Voice Input (STT):")
    print("  Auto-transcription enabled")
    print()
    print("Test it:")
    print('  Send "用语音说你好" to your bot on Feishu')
    print()
    if patch_ok:
        print("NOTE: After `npm update openclaw`, re-run:")
        print(f"  python3 {os.path.join(SCRIPT_DIR, 'patch_media.py')}")
        print("  openclaw gateway restart")


if __name__ == "__main__":
    main()
