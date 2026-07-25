import yfinance as yf
import pandas as pd
import numpy as np

tickers = ["BHP.AX", "RIO.AX", "CBA.AX"]
print("Preuzimanje podataka za australijske kompanije (ASX)...")
data = yf.download(tickers, period="5d", interval="1d", progress=False)

if not data.empty:
    print(data.head())
    data.to_json("australija_podaci.json", orient="index", indent=4)
    print("Podaci uspešno sačuvani u australija_podaci.json")
else:
    print("Nema podataka.")
