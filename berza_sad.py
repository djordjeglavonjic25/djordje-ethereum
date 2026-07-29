import json
import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Definisanje ključnih američkih banaka i platnih servisa (uključujući PayPal)
us_tickers = {
    "JPMorgan_Chase": "JPM",
    "Bank_of_America": "BAC",
    "Citigroup": "C",
    "Wells_Fargo": "WFC",
    "PayPal": "PYPL",
    "Stripe_Proxy_Sector": "SQ",  # Blok/Square kao ekvivalent/alternativa u fintek sektoru
}

data_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "market": "USA (Banks & Payments)",
    "data": {},
}

print("Preuzimanje podataka za američko tržište (SAD)...")

for name, ticker in us_tickers.items():
  try:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    if not hist.empty:
      close_price = float(hist["Close"].iloc[-1])
      volume = int(hist["Volume"].iloc[-1])
      data_output["data"][name] = {
          "ticker": ticker,
          "close": round(close_price, 2),
          "volume": volume,
      }
      print(f"[USPEH] {name} ({ticker}): {close_price}")
    else:
      print(f"[UPOZORENjE] Nema podataka za {name}")
  except Exception as e:
    print(f"[GREŠKA] Greška pri preuzimanju za {name}: {e}")

# Snimanje u JSON fajl
file_name = "berza_sad.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(data_output, f, indent=4, ensure_ascii=False)

print(f"Podaci uspešno sačuvani u {file_name}")
