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


# Sample helper (place outside the class, e.g. in a script using the client)
def print_groups_and_members(hue_client: HueClientUser) -> None:
    """
    Print each group and the lights that belong to it (id + name).
    Uses HueClientUser.list_groups() and HueClientUser.list_lights().
    """
    groups = hue_client.get_groups_and_members() or []
    light_map = {l["id"]: l.get("name") for l in hue_client.list_lights()}

    if not groups:
        print("No groups found")
        return

    for g in groups:
        gid = g.get("id")
        gname = g.get("name") or "(no name)"
        print(f"\n=== Group {gid} : {gname} ===")
        members = g.get("lights", [])
        if not members:
            print("  (no lights in group)")
            continue
        for lid in members:
            print(f"  - {lid} : {light_map.get(lid, '(unknown)')}")

def run_animation_1(hue_client: HueClientUser, lights):

    ligt_id = lights[5]["id"]
    print(f"\nTurning {ligt_id} ON...")
    sleep(1)
    hue_client.set_light_on(ligt_id, True)

    print("brightness to 50%...")
    sleep(1)
    hue_client.set_brightness(ligt_id, 50)

    print("Setting color (xy) to warm-ish values.")
    sleep(1)
    hue_client.set_color_xy(ligt_id, 0.4573, 0.41)
    print("wait 3s\n")
    time.sleep(3)


    print("Wylaczona")
    time.sleep(0.5)
    hue_client.set_light_on(ligt_id, False)
    print("wait 3s\n")
    time.sleep(3)


    print("Wlaczona")
    time.sleep(0.5)
    hue_client.set_light_on(ligt_id, True)
    print("wait 3s\n")
    time.sleep(3)

    print("brightness to 100%...")
    time.sleep(0.5)
    hue_client.set_brightness(ligt_id, 100)
    print("wait 3s\n")
    time.sleep(3)

    return

def run_animation_2(hue_client: HueClientUser, lights):
    id = lights[5]["id"]

    return

def print_lights_details(lights):
    for l in lights:
        lid = l.get("id")
        name = l.get("nazwa") or l.get("name", "")
        print(f"\n=== Light {lid} ({name}) ===")
        hue_client.print_light_json(lid)


if __name__ == "__main__":
    hue_client = initConenction(HUE_BRIDGE_IP)
    lights = hue_client.get_lights() or []


    if not lights:
        print("No lights found, exiting.")
        exit(0)

    #print_lights_details(lights)

    hue_client.print_lights()
    print_groups_and_members(hue_client)

    run_animation_1(hue_client, lights)
    run_animation_2(hue_client, lights)



