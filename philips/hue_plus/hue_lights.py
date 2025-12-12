# python
class HueLights:
    def __init__(self, lights):
        self.lights = lights

    def turn_on(self, light_name, brightness=254, color=None):
        light = self.lights.get(light_name)
        if light:
            light.on = True
            light.brightness = brightness
            if color:
                light.xy = color

    def turn_off(self, light_name):
        light = self.lights.get(light_name)
        if light:
            light.on = False

    def set_brightness(self, light_name, brightness):
        light = self.lights.get(light_name)
        if light:
            light.brightness = brightness

    def set_color(self, light_name, color):
        light = self.lights.get(light_name)
        if light:
            light.xy = color
