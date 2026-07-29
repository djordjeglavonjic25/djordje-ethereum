import urllib.request
import json
import pandas as pd
import numpy as np

url = "https://iss.moex.com/iss/engines/stock/markets/shares/boards/TQBR/securities.json"
print("Preuzimanje podataka sa Moskovske berze (MOEX)...")

try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
        columns = data['securities']['columns']
        rows = data['securities']['data']
        
        df = pd.DataFrame(rows, columns=columns)
        print(df[['SECID', 'SHORTNAME', 'PREVPRICE']].head())
        
        df.head(20).to_json("rusija_podaci.json", orient="records", indent=4)
        print("Podaci uspešno sačuvani u rusija_podaci.json")
except Exception as e:
    print(f"Greška pri preuzimanju podataka: {e}")
