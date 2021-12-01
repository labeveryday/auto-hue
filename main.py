from app.auto_hue import AutoHue
from dotenv import load_dotenv
import os


load_dotenv()

bridgeIpAddress = os.getenv("BRIDGE_IP")

def main():
    """
    Every time script is run lights will change from
    YouTube to Night settings.
    """
    hue = AutoHue(bridgeIpAddress)
    state = hue.get_all_light_state()
    if state[0]['hue'] == 6291:
        hue.set_office_youtube_lights()
    else:
        hue.set_office_night_light()


if __name__ == "__main__":
    main()
