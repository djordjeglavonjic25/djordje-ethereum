import json
import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Definisanje ključnih australijskih banaka ("Big Four") i platnih servisa (Payoneer, Block/Afterpay)
australia_tickers = {
    "Commonwealth_Bank_CBA": "CBA.AX",
    "Westpac_Banking": "WBC.AX",
    "National_Australia_Bank_NAB": "NAB.AX",
    "ANZ_Group": "ANZ.AX",
    "Payoneer": "PAYO",
    "Block_Afterpay_Parent": "SQ",
}

data_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "market": "Australia (Big Four Banks & Services)",
    "data": {},
}

print("Preuzimanje podataka za australijske banke i servise...")

for name, ticker in australia_tickers.items():
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
file_name = "berza_australija_bigfour.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(data_output, f, indent=4, ensure_ascii=False)

print(f"Podaci uspešno sačuvani u {file_name}")
