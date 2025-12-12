# python
from hue_bridge import HueBridge
from hue_lights import HueLights

# Połączenie z mostkiem Hue
bridge_ip = "192.168.7.5"  # Zmień na adres IP swojego mostka
bridge = HueBridge(bridge_ip)

# Pobranie lamp
lights = bridge.get_lights()
hue_lights = HueLights(lights)

# Przykładowe procedury
def turn_on_all_lights():
    for light_name in lights:
        hue_lights.turn_on(light_name)

def turn_off_all_lights():
    for light_name in lights:
        hue_lights.turn_off(light_name)

def set_desk_lamp_color(color):
    hue_lights.set_color("Lampka nocna", color)

# Ernest może tutaj pisać swoje procedury
if __name__ == "__main__":
    turn_on_all_lights()
    set_desk_lamp_color([0.675, 0.322])  # Ustaw kolor na czerwony
