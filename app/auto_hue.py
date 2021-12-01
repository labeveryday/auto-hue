from phue import Bridge


class AutoHue:

    def __init__(self, bridgeIpAddress):
        """Initialize connection to HUE"""
        self.bridge_ip = bridgeIpAddress
        self._connect()

    def _connect(self):
        """
        Connect to Hue bridge
        """
        self.connect = Bridge(self.bridge_ip)
        self.connect.connect()
        
    def get_light_names(self):
        """
        Get all lights name
        """  
        light_names = self.connect.get_light_objects("name")
        return light_names

    def get_light_groups(self):
        """
        Get light group id and name
        """
        return self.connect.get_group()
        
    
    def Off_light_group(self, group_id):
        """
        Turn off group of lights
        """
        self.connect.set_group(int(group_id), "on", False)
    
    def on_light_group(self, group_id):
        """
        Turn on group of lights
        """
        self.connect.set_group(int(group_id), "on", True)
    
    def set_office_youtube_lights(self):
        """
        Set Hue Light Settings for YouTube
        """
        lights = self.get_light_names()
        for light in lights:
            if light == "Hue lightstrip plus 1":
                lights[light].on = True
                lights[light].hue = 49033
                lights[light].saturation = 252
                lights[light].brightness = 254
            elif light == "Hue color downlight 1":
                lights[light].on = True
                lights[light].hue = 42851
                lights[light].saturation = 254
                lights[light].brightness = 254
            elif light == "Hue color downlight 2":
                lights[light].on = True
                lights[light].hue = 45801
                lights[light].saturation = 254
                lights[light].brightness = 254
            elif light == "Hue color downlight 3":
                lights[light].on = True
                lights[light].hue = 48796
                lights[light].saturation = 242
                lights[light].brightness = 254
    
    def set_office_night_light(self):
        """
        Set Hue Light Settings for Night time
        """
        lights = self.get_light_names()
        for light in lights:
            if light == "Hue lightstrip plus 1":
                lights[light].on = True
                lights[light].hue = 6291
                lights[light].saturation = 251
                lights[light].brightness = 1
            elif light == "Hue color downlight 1":
                lights[light].on = True
                lights[light].hue = 6291
                lights[light].saturation = 251
                lights[light].brightness = 1
            elif light == "Hue color downlight 2":
                lights[light].on = True
                lights[light].hue = 6291
                lights[light].saturation = 251
                lights[light].brightness = 1
            elif light == "Hue color downlight 3":
                lights[light].on = True
                lights[light].hue = 6291
                lights[light].saturation = 251
                lights[light].brightness = 1
    
    def get_all_light_state(self):
        """
        Get all Hue Light configurations
        """
        light_list = []
        lights = self.connect.lights
        for light in lights:
            light_list.append(
                {
                    'light_id': light.light_id,
                    'name': light.name,
                    'saturation': light.saturation,
                    'brightness': light.brightness,
                    'on': light.on,
                    'hue': light.hue,
                    'xy': light.xy
            }
            )
        return light_list


if __name__ == "__main__":
    hue = AutoHue()
    hue.set_office_youtube_lights()
    # hue.set_office_night_light()
