from curl_cffi import requests

SOFASCORE_BASE = "https://api.sofascore.com/api/v1"

def fetch(url, params=None):
    try:
        resp = requests.get(
            f"{SOFASCORE_BASE}{url}",
            params=params,
            timeout=20,
            impersonate="chrome131",
            headers={
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.9',
                'Origin': 'https://www.sofascore.com',
                'Referer': 'https://www.sofascore.com/',
            }
        )
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        status = getattr(getattr(e, 'response', None), 'status_code', 500)
        raise Exception(f"Sofascore API error ({status}): {str(e)}")
