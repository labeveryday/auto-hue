#!/usr/bin/env python3

import os
import sys
from phue import Bridge
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual bridge IP address
BRIDGE_IP = os.getenv("BRIDGE_IP")  # You can find this by pressing the button on your Hue bridge and running `nmap -p 1900


def main():
    b = Bridge(BRIDGE_IP)
    try:
        b.connect()
    except Exception as e:
        print("Could not connect to the Hue Bridge.")
        print(e)
        sys.exit(1)

    # Get a dictionary of lights keyed by their numeric ID
    lights_by_id = b.get_light_objects('id')

    # Check if ANY lights are currently on
    any_on = any(light.on for light in lights_by_id.values())

    if any_on:
        # If any lights are on, turn them ALL off
        for light in lights_by_id.values():
            light.on = False
        print("All lights turned OFF.")
    else:
        # If no lights are on, turn them ALL on
        for light in lights_by_id.values():
            light.on = True
        print("All lights turned ON.")

if __name__ == "__main__":
    main()

