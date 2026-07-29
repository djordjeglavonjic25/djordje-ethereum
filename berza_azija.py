import json
import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# Definisanje ključnih azijskih banaka i ekvivalenata za platne platforme/tehnologije 
# (ICBC, MUFG, DBS, SBI, Tencent, Alibaba/Ant Group ekvivalent, itd.)
asia_tickers = {
    "ICBC_China": "1398.HK",
    "MUFG_Japan": "8306.T",
    "DBS_Singapore": "D05.SI",
    "State_Bank_India": "SBIN.NS",
    "Tencent_WeChat_Parent": "0700.HK",
    "Alibaba_Ant_Parent": "9988.HK",
}

data_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "market": "Asia (Banks & Tech Platforms)",
    "data": {},
}

print("Preuzimanje podataka za azijsko tržište...")

for name, ticker in asia_tickers.items():
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
file_name = "berza_azija.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(data_output, f, indent=4, ensure_ascii=False)

print(f"Podaci uspešno sačuvani u {file_name}")
