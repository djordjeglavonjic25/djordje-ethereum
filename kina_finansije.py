import akshare as ak
import pandas as pd
import numpy as np

print("Preuzimanje podataka sa kineskih berzi putem AKShare...")
try:
    df = ak.stock_zh_a_spot_em()
    print(df[['代码', '名称', '最新价', '涨跌幅']].head())
    
    df.head(20).to_json("kina_podaci.json", orient="records", force_ascii=False, indent=4)
    print("Podaci uspešno sačuvani u kina_podaci.json")
except Exception as e:
    print(f"Greška pri preuzimanju podataka: {e}")
