import requests
import random
import time
from config.settings import SETTINGS

def fetch_url(url):
    headers = SETTINGS["HEADERS"].copy()
    headers["User-Agent"] = random.choice(SETTINGS["USER_AGENTS"])

    for attempt in range(SETTINGS["RETRY_COUNT"]):
        try:
            response = requests.get(url, headers=headers, timeout=SETTINGS["REQUEST_TIMEOUT"])
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Tentativa {attempt + 1} falhou: {e}")
            time.sleep(SETTINGS["RETRY_DELAY"])
    return None
