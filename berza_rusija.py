import json
import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Definisanje ključnih dostupnih ruskih berzanskih simbola (ticker-a) 
# za najveće banke i energetske gigante koji nose ruski finansijski sektor 
# (Sberbank, VTB, Gazprombank, TCS Holding/T-Bank).
# Napomena: Za servise poput MIR-a, SBP-a i YooMoney nema direktnih berzanskih kvota, 
# pa se prate akcije njihovih matičnih kompanija/banaka.
russia_tickers = {
    "Sberbank": "SBER.ME",
    "VTB_Bank": "VTBR.ME",
    "Gazprombank_Sector": "GAZP.ME",
    "TCS_Holding_T_Bank": "TCSG.ME",
}

data_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "market": "Russia (Banks & Infrastructure)",
    "data": {},
}

print("Preuzimanje podataka za rusko tržište...")

for name, ticker in russia_tickers.items():
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
file_name = "berza_rusija.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(data_output, f, indent=4, ensure_ascii=False)

print(f"Podaci uspešno sačuvani u {file_name}")
