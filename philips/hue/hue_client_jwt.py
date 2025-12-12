import requests
import urllib3
from typing import Any, Dict, List, Optional

# disable warnings for self-signed certs on local bridges (remove verify=False in production)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class HueClientBearer:
    def __init__(self, bridge_ip: str, token: str, verify: bool = False, timeout: int = 5) -> None:
        self.bridge_ip = bridge_ip
        self.token = token
        self.verify = verify
        self.timeout = timeout
        self.base = f"https://{self.bridge_ip}/clip/v2/resource"
        self.headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}

    def _request(self, method: str, resource: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base}/{resource}"
        resp = requests.request(method, url, headers=self.headers, json=json, verify=self.verify, timeout=self.timeout)
        resp.raise_for_status()
        return resp.json()

    def list_lights(self) -> List[Dict[str, Any]]:
        data = self._request("GET", "light")
        items = data.get("data", []) if isinstance(data, dict) else []
        result: List[Dict[str, Any]] = []
        for it in items:
            result.append(
                {
                    "id": it.get("id"),
                    "name": it.get("metadata", {}).get("name"),
                    "on": it.get("on", {}).get("on"),
                    "brightness": it.get("dimming", {}).get("brightness"),
                }
            )
        return result

    def set_light_on(self, light_id: str, on: bool) -> Dict[str, Any]:
        payload = {"on": {"on": bool(on)}}
        return self._request("PATCH", f"light/{light_id}", json=payload)

    def set_brightness(self, light_id: str, brightness_percent: int) -> Dict[str, Any]:
        b = max(0, min(100, int(brightness_percent)))
        payload = {"dimming": {"brightness": b}}
        return self._request("PATCH", f"light/{light_id}", json=payload)

    def set_color_xy(self, light_id: str, x: float, y: float) -> Dict[str, Any]:
        payload = {"color": {"xy": {"x": float(x), "y": float(y)}}}
        return self._request("PATCH", f"light/{light_id}", json=payload)
