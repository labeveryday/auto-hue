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

    # Connect to the Bridge
    try:
        b.connect()
    except Exception as e:
        print("Could not connect to the Hue Bridge.")
        print(e)
        sys.exit(1)

    # b.groups is a list of Group objects
    groups_list = b.groups

    print(f"Found {len(groups_list)} groups.")
    for group in groups_list:
        # Each 'group' is a phue.Group object
        print(f"Group ID: {group.group_id}")
        print(f"  Name: {group.name}")
        print(f"  Lights: {group.lights}\n")

if __name__ == "__main__":
    main()