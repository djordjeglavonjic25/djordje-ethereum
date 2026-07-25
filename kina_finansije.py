import pandas as pd
import numpy as np
import urllib.request
import json

print("Preuzimanje kineskih finansijskih podataka direktno...")
try:
    # Korišćenje alternativnog stabilnog API-ja za spot cene
    url = "https://push2.eastmoney.com/api/qt/clist/get?pn=1&pz=20&po=1&np=1&fltt=2&invt=2&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23&fields=f2,f3,f12,f14"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        
    rows = []
    for item in data.get('data', {}).get('diff', []):
        rows.append({
            'kod': item.get('f12'),
            'naziv': item.get('f14'),
            'cena': item.get('f2'),
            'promena_procenat': item.get('f3')
        })
        
    df = pd.DataFrame(rows)
    print(df.head())
    df.to_json("kina_podaci.json", orient="records", force_ascii=False, indent=4)
    print("Podaci uspešno sačuvani u kina_podaci.json")
except Exception as e:
    print(f"Greška: {e}")
