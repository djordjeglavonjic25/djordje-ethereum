import yfinance as yf
import pandas as pd
import numpy as np

tickers = ["AAPL", "MSFT", "GOOGL"]
print("Preuzimanje podataka za američke kompanije...")
data = yf.download(tickers, period="5d", interval="1d", progress=False)

if not data.empty:
    print(data.head())
    data.to_json("amerika_podaci.json", orient="index", indent=4)
    print("Podaci uspešno sačuvani u amerika_podaci.json")
else:
    print("Nema podataka.")
