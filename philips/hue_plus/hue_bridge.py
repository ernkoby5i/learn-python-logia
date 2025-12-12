# python
from phue import Bridge

class HueBridge:
    def __init__(self, ip_address):
        self.bridge = Bridge(ip_address)
        self.bridge.connect()

    def get_lights(self):
        return self.bridge.get_light_objects('name')

    def get_groups(self):
        return self.bridge.get_group()
