# File: `hue/hello_hue_world_user.py`
import os
import time
from time import sleep

from hue.hue_client_user import HueClientUser


HUE_BRIDGE_IP = "192.168.7.5"
hue_client = None

def initConenction(bridge_ip: str | None = None):
    # use provided bridge_ip or fall back to environment (or default)
    BRIDGE_IP = bridge_ip or os.getenv("HUE_BRIDGE_IP", "192.168.1.23")

    # read user from environment
    USER = os.getenv("HUE_USER")
    if not USER:
        raise RuntimeError("Environment variable `HUE_USER` not set")

    return HueClientUser(bridge_ip=BRIDGE_IP, user=USER, timeout=5)



if __name__ == "__main__":
    hue_client = initConenction(HUE_BRIDGE_IP)
    hue_client.print_lights()
    lights = hue_client.get_lights() or []
    #lights = _print_lights()
    if not lights:
        print("No lights found, exiting.")
        exit(0)


    first_id = lights[0]["id"]
    print(f"\nTurning {first_id} ON...")
    sleep(1)
    hue_client.set_light_on(first_id, True)

    print("brightness to 50%...")
    sleep(1)
    hue_client.set_brightness(first_id, 50)

    print("Setting color (xy) to warm-ish values.")
    sleep(1)
    hue_client.set_color_xy(first_id, 0.4573, 0.41)
    print("wait 3s\n")
    time.sleep(3)


    print("Wylaczona")
    time.sleep(0.5)
    hue_client.set_light_on(first_id, False)
    print("wait 3s\n")
    time.sleep(3)


    print("Wlaczona")
    time.sleep(0.5)
    hue_client.set_light_on(first_id, True)
    print("wait 3s\n")
    time.sleep(3)

    print("brightness to 100%...")
    time.sleep(0.5)
    hue_client.set_brightness(first_id, 100)
    print("wait 3s\n")
    time.sleep(3)


    print("czerwony")
    time.sleep(0.5)
    hue_client.set_color_rgb(first_id, 255, 0, 0)  # czerwony
    print("wait 3s\n")
    time.sleep(3)

    print("zielony")
    time.sleep(0.5)
    hue_client.set_color_rgb(first_id, 0, 255, 0)     # zielony
    print("wait 3s\n")
    time.sleep(3)

    print("niebieski")
    time.sleep(0.5)
    hue_client.set_color_rgb(first_id, 0, 0, 255)     # niebieski
    print("wait 3s\n")
    time.sleep(3)

    print("żółty")
    time.sleep(0.5)
    hue_client.set_color_rgb(first_id, 255, 255, 0)   # żółty
    print("wait 3s\n")
    time.sleep(3)

    print("bilay")
    time.sleep(1)
    hue_client.set_color_rgb(first_id, 255, 255, 255)   # bilay
    print("wait 3s\n")
    time.sleep(3)

    for l in lights:
        lid = l.get("id")
        name = l.get("nazwa") or l.get("name", "")
        print(f"\n=== Light {lid} ({name}) ===")
        #hue_client.print_light_json(lid)
