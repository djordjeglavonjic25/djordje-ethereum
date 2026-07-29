#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open-Source China Energy Stock Market Fetcher
Author: djordjeglavonjic25
License: MIT
Repository: djordje-ethereum
Branch: japantokio
"""

import json
import math
from datetime import datetime
import yfinance as yf

# Kineska "Velika trojka" energetskih giganata (Hong Kong Stock Exchange)
COMPANIES = {
    "PetroChina": "0857.HK",
    "Sinopec": "0386.HK",
    "CNOOC": "0883.HK"
}

def clean_number(val):
    """Bezbedno pretvara i zaokružuje broj, rukujući sa None i NaN vrednostima."""
    if val is None or (isinstance(val, float) and math.isnan(val)):
        return None
    return round(float(val), 2)

def fetch_market_data():
    market_data = {}
    print("--- Preuzimanje podataka za kineske naftne gigante ---")

    for name, symbol in COMPANIES.items():
        try:
            stock = yf.Ticker(symbol)
            info = stock.fast_info
            
            price = getattr(info, 'last_price', None)
            prev_close = getattr(info, 'previous_close', None)
            currency = getattr(info, 'currency', 'HKD')
            
            # Fallback mehanizam ako je fast_info prazan ili vrati NaN
            if price is None or (isinstance(price, float) and math.isnan(price)):
                hist = stock.history(period="2d")
                if not hist.empty:
                    price = hist['Close'].iloc[-1]
                    if len(hist) > 1:
                        prev_close = hist['Close'].iloc[-2]

            clean_p = clean_number(price)
            clean_pc = clean_number(prev_close)

            market_data[name] = {
                "symbol": symbol,
                "price": clean_p,
                "previous_close": clean_pc,
                "currency": currency,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"[OK] {name} ({symbol}): {clean_p} {currency}")

        except Exception as e:
            print(f"[GRESKA] {name} ({symbol}): {e}")
            market_data[name] = {
                "symbol": symbol,
                "error": str(e),
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    # Cuvanje u JSON format
    with open("berze_kina_nafta.json", "w", encoding="utf-8") as f:
        json.dump(market_data, f, ensure_ascii=False, indent=4)

    print("\n[USPEH] Podaci su sacuvani u 'berze_kina_nafta.json'")

if __name__ == "__main__":
    fetch_market_data()
