#!/usr/bin/env python3
import os
import sys
from phue import Bridge
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual bridge IP address
BRIDGE_IP = os.getenv("BRIDGE_IP")  # You can find this by pressing the button on your Hue bridge and running `nmap -p 1900


def list_scenes(bridge):
    scenes = bridge.scenes  # Returns a dict of scene_id => scene_data

    print("Available scenes on this bridge:")
    for scene_id, scene_data in scenes.items():
        scene_name = scene_data['name']
        owner = scene_data['owner']
        lights = scene_data['lights']  # list of light IDs
        print(f"  ID: {scene_id}, Name: {scene_name}, Lights: {lights}, Owner: {owner}")

def main():
    b = Bridge(BRIDGE_IP)
    b.connect()  # Press link button if first time

    scenes = b.scenes  # If this is a list
    print(f"Found {len(scenes)} scenes.")

    for i, scene in enumerate(scenes):
        # scene might look like: {'id': 'xyz123', 'name': 'My Scene', 'lights': [...], ...}
        scene_id = scene.scene_id
        scene_name = scene.name
        lights_in_scene = scene.lights

        print(f"Scene ID: {scene_id}, Name: {scene_name}, Lights: {lights_in_scene}")

if __name__ == "__main__":
    main()
