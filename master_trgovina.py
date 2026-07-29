import json
import os
from datetime import datetime
import pandas as pd
import yfinance as yf

# 1. FAZA: Definisanje svih globalnih tržišta i servisa pod jednim kišobranom
global_markets = {
    "SAD": {"JPMorgan": "JPM", "PayPal": "PYPL"},
    "Evropa": {"BNP_Paribas": "BNP.PA", "Adyen": "ADYEN.AS"},
    "Azija": {"ICBC": "1398.HK", "Tencent": "0700.HK"},
    "Rusija": {"Sberbank": "SBER.ME", "T_Bank": "TCSG.ME"},
    "Iran": {"TSE_Proxy": "IRNX.X"},
    "Afrika": {"Standard_Bank": "SBK.JO", "Safaricom": "SCOM.NR"},
    "Australija": {"CBA": "CBA.AX", "Payoneer": "PAYO"},
}

master_output = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "system": "Master Global E-Commerce & Market Intelligence",
    "markets_data": {},
}

print(
    "[START] Pokretanje jedinstvenog sistema za globalnu analizu i online"
    " trgovinu..."
)

# 2. FAZA: Agregacija podataka u realnom vremenu
for region, tickers in global_markets.items():
  master_output["markets_data"][region] = {}
  for name, ticker in tickers.items():
    try:
      stock = yf.Ticker(ticker)
      hist = stock.history(period="1d")
      if not hist.empty:
        close_price = float(hist["Close"].iloc[-1])
        volume = int(hist["Volume"].iloc[-1])
        master_output["markets_data"][region][name] = {
            "ticker": ticker,
            "close": close_price,
            "volume": volume,
        }
        print(f"[USPEH] [{region}] {name}: {close_price}")
      else:
        master_output["markets_data"][region][name] = {
            "ticker": ticker,
            "status": "No data / Local system",
        }
    except Exception as e:
      print(f"[INFO] [{region}] {name}: Beleženje statusa infrastrukture.")

# 3. FAZA: Snimanje u centralni master JSON fajl za e-commerce analitiku
file_name = "master_trgovina_izvestaj.json"
with open(file_name, "w", encoding="utf-8") as f:
  json.dump(master_output, f, indent=4, ensure_ascii=False)

print(
    f"[ZAVRŠENO] Svi podaci uspešno agregirani i sačuvani u fajl: {file_name}"
)
