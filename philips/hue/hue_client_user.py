# python
import os
import requests
from typing import Any, Dict, List, Optional
import json


class HueClientUser:
    def __init__(self, bridge_ip: str = "192.168.1.23", user: Optional[str] = None, timeout: int = 5) -> None:
        self.bridge_ip = bridge_ip
        self.user = user or os.getenv("HUE_USER")
        if not self.user:
            raise RuntimeError("Environment variable `HUE_USER` not set and no user provided")
        self.timeout = timeout
        self.base = f"http://{self.bridge_ip}/api/{self.user}"

    def _url(self, path: str) -> str:
        return f"{self.base}/{path.lstrip('/')}"

    def _rgb_to_xy(self, r: int, g: int, b: int) -> tuple[float, float]:
        # Normalize 0-255 to 0-1
        r_n = max(0, min(255, int(r))) / 255.0
        g_n = max(0, min(255, int(g))) / 255.0
        b_n = max(0, min(255, int(b))) / 255.0

        # Apply inverse gamma correction (sRGB)
        def lin(c: float) -> float:
            if c > 0.04045:
                return ((c + 0.055) / 1.055) ** 2.4
            return c / 12.92

        r_l = lin(r_n)
        g_l = lin(g_n)
        b_l = lin(b_n)

        # Convert to XYZ using sRGB D65 matrix
        X = r_l * 0.4124 + g_l * 0.3576 + b_l * 0.1805
        Y = r_l * 0.2126 + g_l * 0.7152 + b_l * 0.0722
        Z = r_l * 0.0193 + g_l * 0.1192 + b_l * 0.9505

        denom = X + Y + Z
        if denom == 0:
            return 0.0, 0.0

        x = X / denom
        y = Y / denom

        # Clamp to [0,1]
        x = max(0.0, min(1.0, x))
        y = max(0.0, min(1.0, y))
        return x, y

    def _get(self, path: str) -> Any:
        resp = requests.get(self._url(path), timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def _put(self, path: str, body: Dict[str, Any]) -> Any:
        resp = requests.put(self._url(path), json=body, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def list_lights(self) -> List[Dict[str, Any]]:
        data = self._get("lights")
        result: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            for light_id, info in data.items():
                state = info.get("state", {})
                result.append(
                    {
                        "id": light_id,
                        "name": info.get("name"),
                        "on": state.get("on"),
                        "brightness": state.get("bri"),  # 1-254 (v1)
                    }
                )
        return result

    def set_light_on(self, light_id: str, on: bool) -> Any:
        body = {"on": bool(on)}
        return self._put(f"lights/{light_id}/state", body)

    def set_brightness(self, light_id: str, brightness_percent: int) -> Any:
        b_pct = max(0, min(100, int(brightness_percent)))
        if b_pct == 0:
            body = {"on": False}
        else:
            bri = max(1, min(254, int(b_pct * 254 / 100)))
            body = {"on": True, "bri": bri}
        return self._put(f"lights/{light_id}/state", body)

    def get_lights(self) -> list[dict]:
        """
        Return a list of lights as dictionaries with keys:
          - id
          - nazwa (name)
        """
        raw = self.list_lights() or []
        return [{"id": l.get("id"), "nazwa": l.get("name")} for l in raw]

    def print_lights(self) -> list[dict]:
        """
        Print list of lights (id and name) and return the simplified list.
        """
        lights = self.get_lights()
        print("Found lights:")
        for l in lights:
            print(f"- {l['id']} : {l['nazwa']}")
        return lights

    def set_color_xy(self, light_id: str, x: float, y: float) -> Any:
        body = {"on": True, "xy": [float(x), float(y)]}
        return self._put(f"lights/{light_id}/state", body)

    def set_color_rgb(self, light_id: str, r: int, g: int, b: int) -> Any:
        """
        Set light color using 8-bit RGB values (0-255).
        Converts RGB -> CIE 1931 xy and calls existing set_color_xy.
        """
        x, y = self._rgb_to_xy(r, g, b)
        return self.set_color_xy(light_id, x, y)

    def get_light_by_id(self, light_id: str) -> Optional[Dict[str, Any]]:
        """
        Return the light resource for `light_id` or None if not found.
        """
        try:
            data = self._get(f"lights/{light_id}")
            if isinstance(data, dict):
                return data
            return None
        except requests.RequestException:
            return None

    def print_light_json(self, light_id: str) -> Optional[Dict[str, Any]]:
        """
        Fetch the light by id, pretty-print JSON and return the dict or None.
        """
        light = self.get_light_by_id(light_id)
        if not light:
            print(f"Light {light_id} not found")
            return None
        print(json.dumps(light, indent=2, ensure_ascii=False))
        return light
