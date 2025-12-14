# =============================================================
# packages
# =============================================================

import urllib.request
import ssl
import certifi
import time
import pandas as pd
from bs4 import BeautifulSoup

# =============================================================
# CONFIG
# =============================================================

EVENT_DB = "products_export_1.csv"
VENUE_DB = ""
INTEREST_DB = ""

# =============================================================
# html loader function
# =============================================================

def get_html(root: str, path: str, title: str = "test") -> str:
    # extracts and decodes bulk html from target url

    context = ssl.create_default_context(cafile=certifi.where())
    url = root+path

    print("Sleeping for 1 second to avoid request block...")
    time.sleep(1)
    print(f"Requesting HTML for {title} with:\n{url}...")

    try:
        with urllib.request.urlopen(url, context=context) as fp:
            print("HTLM recieved!")
            data = fp.read()
            return data.decode("utf-8")
    
    except:
        print(f"WARN: URL path \"{path}\"does not exist!\nSkipping...")
