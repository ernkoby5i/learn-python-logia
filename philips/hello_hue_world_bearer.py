# python
import os
import requests
import urllib3

# disable warnings for self-signed certs on local bridges (remove verify=False in production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BRIDGE_IP = "192.168.7.5"
TOKEN = os.getenv("HUE_TOKEN")
if not TOKEN:
    raise RuntimeError("Environment variable `HUE_TOKEN` not set")

BASE_URL = f"https://{BRIDGE_IP}/clip/v2/resource"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}


def api_get(resource: str):
    url = f"{BASE_URL}/{resource}"
    resp = requests.get(url, headers=HEADERS, verify=False, timeout=5)
    resp.raise_for_status()
    return resp.json()


def api_patch(resource: str, body: dict):
    url = f"{BASE_URL}/{resource}"
    resp = requests.patch(url, headers=HEADERS, json=body, verify=False, timeout=5)
    resp.raise_for_status()
    return resp.json()


def list_lights():
    data = api_get("light")
    lights = []
    for item in data.get("data", []):
        lights.append(
            {
                "id": item.get("id"),
                "name": item.get("metadata", {}).get("name"),
                "on": item.get("on", {}).get("on"),
                "brightness": item.get("dimming", {}).get("brightness"),
            }
        )
    return lights


def set_light_on(light_id: str, on: bool):
    body = {"on": {"on": bool(on)}}
    return api_patch(f"light/{light_id}", body)


def set_brightness(light_id: str, brightness_percent: int):
    # brightness_percent: 0-100
    brightness = max(0, min(100, int(brightness_percent)))
    body = {"dimming": {"brightness": brightness}}
    return api_patch(f"light/{light_id}", body)


def set_color_xy(light_id: str, x: float, y: float):
    body = {"color": {"xy": {"x": float(x), "y": float(y)}}}
    return api_patch(f"light/{light_id}", body)


if __name__ == "__main__":
    # Example usage
    lights = list_lights()
    print("Found lights:")
    for l in lights:
        print(f"- {l['id']} : {l['name']} (on={l['on']}, brightness={l['brightness']})")

    if not lights:
        print("No lights found")
    else:
        first = lights[0]["id"]
        print(f"\nTurning {first} ON...")
        set_light_on(first, True)

        print("Set brightness to 70%...")
        set_brightness(first, 70)

        # warm-ish color XY example (adjust for your bulb)
        print("Set color (xy)...")
        set_color_xy(first, 0.4573, 0.41)

        print("Turning off in 3 seconds...")
        import time

        time.sleep(3)
        set_light_on(first, False)
    print("Done.")