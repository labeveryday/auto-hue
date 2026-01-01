#!/usr/bin/env python3
import os
import sys
from phue import Bridge
from dotenv import load_dotenv

load_dotenv()

BRIDGE_IP = os.getenv("BRIDGE_IP")
GROUP_NAME = os.getenv("GROUP_NAME")

def main():
    bridge = Bridge(BRIDGE_IP)
    try:
        bridge.connect()
        bridge.run_scene(GROUP_NAME, "Energize")
        print("✓ Energize scene activated")
        sys.exit(0)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()