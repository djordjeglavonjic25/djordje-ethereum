import yfinance as yf
import json
import os
from datetime import datetime

# Lista australijskih kompanija (ASX IT & Nafta/Gas)
tickers = {
    "Xero": "XRO.AX",
    "WiseTech Global": "WTC.AX",
    "Computershare": "CPU.AX",
    "Woodside Energy": "WDS.AX",
    "Santos": "STO.AX",
    "Beach Energy": "BPT.AX"
}

data = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "kompanije": {}
}

print("Preuzimanje podataka sa australijske berze (ASX)...")

for name, symbol in tickers.items():
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.fast_info
        
        price = info.last_price
        prev_close = info.previous_close
        change = price - prev_close if price and prev_close else 0
        change_pct = (change / prev_close) * 100 if prev_close else 0
        
        data["kompanije"][name] = {
            "simbol": symbol,
            "cena": round(price, 2) if price else None,
            "valuta": getattr(info, 'currency', 'AUD'),
            "promena": round(change, 2),
            "promena_procenat": f"{round(change_pct, 2)}%"
        }
        print(f"[OK] {name} ({symbol}): {price}")
    except Exception as e:
        print(f"[GREŠKA] Nije moguće preuzeti podatke za {name}: {e}")

# Čuvanje podataka u JSON fajl
output_file = "berze_australija_podaci.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"\nPodaci su uspešno sačuvani u {output_file}")
