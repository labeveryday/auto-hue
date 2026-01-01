#!/usr/bin/env python3
import os
import sys
from phue import Bridge
from dotenv import load_dotenv

load_dotenv()

BRIDGE_IP = os.getenv("BRIDGE_IP")  
GROUP_NAME = os.getenv("GROUP_NAME")


def main(scene_name="Recording"):
    b = Bridge(BRIDGE_IP)
    try:
        b.connect()
    except Exception as e:
        print("Could not connect to the Hue Bridge.")
        print(e)
        sys.exit(1)

    # Activate the scene
    b.run_scene(GROUP_NAME, scene_name)
    print(f"Activated scene '{scene_name}' in group '{GROUP_NAME}'.")

if __name__ == "__main__":
    main()