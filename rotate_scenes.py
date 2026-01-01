#!/usr/bin/env python3
import os
import sys
from pathlib import Path
from phue import Bridge
from dotenv import load_dotenv

REPO_DIR = Path(__file__).resolve().parent

# Prefer a repo-local .env (or .envfile) if present; fall back to default dotenv behavior.
dotenv_path = REPO_DIR / ".env"
dotenv_alt_path = REPO_DIR / ".envfile"
load_dotenv(
    dotenv_path=dotenv_path if dotenv_path.exists() else (dotenv_alt_path if dotenv_alt_path.exists() else None)
)

# Replace with your actual bridge IP address
BRIDGE_IP = os.getenv("BRIDGE_IP")
GROUP_NAME = os.getenv("GROUP_NAME")


# List of scenes in the rotation
SCENE_NAMES = [
    "Trick or treat",
    "Recording",
    "Sunday morning",
    "Energize",
    "Honolulu",
    "Nighttime",
    "Arise",
    "Nighttime"   # if you have a second "Nighttime", rename it "Nighttime 2" as needed
]

# File that stores the current scene index
INDEX_FILE = REPO_DIR / "scene_index.txt"

def main():
    if not BRIDGE_IP:
        print('Missing required env var: BRIDGE_IP (set it in your shell or in ".env").')
        sys.exit(2)
    if not GROUP_NAME:
        print('Missing required env var: GROUP_NAME (set it in your shell or in ".env").')
        sys.exit(2)

    bridge = Bridge(BRIDGE_IP)
    try:
        bridge.connect()
    except Exception as e:
        print("Could not connect to Hue Bridge.")
        print(e)
        sys.exit(1)

    # 1. Read the last-used index from a file
    try:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            current_index = int(f.read().strip())
    except FileNotFoundError:
        # If file doesn't exist, start from the first scene
        current_index = 0
    except ValueError:
        # If file is corrupted, reset to 0
        current_index = 0

    # 2. Activate the scene at current_index
    scene_to_activate = SCENE_NAMES[current_index]
    bridge.run_scene(GROUP_NAME, scene_to_activate)
    print(f"Activated scene: {scene_to_activate}")

    # 3. Increment the index for next time (wrap around with modulo)
    new_index = (current_index + 1) % len(SCENE_NAMES)

    # 4. Save the new index back to the file
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(str(new_index))

if __name__ == "__main__":
    main()
