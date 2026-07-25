import urllib.request
import json
import pandas as pd
import numpy as np

url = "https://api.jse.co.za/v1/market/equity/prices"
print("Preuzimanje podataka sa JSE (Južna Afrika)...")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        df = pd.DataFrame(data)
        print(df.head())
        df.head(20).to_json("afrika_podaci.json", orient="records", indent=4)
        print("Podaci uspešno sačuvani u afrika_podaci.json")
except Exception as e:
    print(f"Greška pri preuzimanju podataka sa berze, kreiranje test strukture: {e}")
    dummy_data = [{'Market': 'JSE', 'Status': 'Active', 'Region': 'Africa'}]
    df = pd.DataFrame(dummy_data)
    df.to_json("afrika_podaci.json", orient="records", indent=4)
    print("Osnovni podaci sačuvani u afrika_podaci.json")
