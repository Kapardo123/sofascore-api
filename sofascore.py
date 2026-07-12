from curl_cffi import requests as cffi_requests

SOFASCORE_BASE = "https://api.sofascore.com/api/v1"

IMPERSONATES = ["chrome131", "chrome124", "chrome120", "chrome110", "safari17_0", "edge101"]

def fetch(url, params=None):
    last_error = None
    for imp in IMPERSONATES:
        try:
            resp = cffi_requests.get(
                f"{SOFASCORE_BASE}{url}",
                params=params,
                timeout=20,
                impersonate=imp,
                headers={
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Origin': 'https://www.sofascore.com',
                    'Referer': 'https://www.sofascore.com/',
                }
            )
            if resp.status_code == 200:
                return resp.json()
            last_error = f"HTTP {resp.status_code}"
        except Exception as e:
            last_error = str(e)
    raise Exception(f"Sofascore API error: {last_error}")
