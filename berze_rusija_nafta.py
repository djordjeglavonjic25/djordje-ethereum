#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open-Source Russia Energy Stock Market Fetcher
Author: djordjeglavonjic25
License: MIT
Repository: djordje-ethereum
Branch: japantokio
"""

import json
from datetime import datetime
import yfinance as yf

COMPANIES = {
    "Gazprom": "GAZP.ME",
    "Rosneft": "ROSN.ME",
    "Lukoil": "LKOH.ME",
    "Novatek": "NVTK.ME",
    "Gazprom Neft": "SIBN.ME",
    "Surgutneftegas": "SNGS.ME"
}

def fetch_market_data():
    market_data = {}
    print("--- Preuzimanje podataka za ruske naftne i gasne gigante ---")

    for name, symbol in COMPANIES.items():
        try:
            stock = yf.Ticker(symbol)
            price = None
            prev_close = None
            currency = "RUB"

            try:
                info = stock.fast_info
                price = getattr(info, 'last_price', None)
                prev_close = getattr(info, 'previous_close', None)
                currency = getattr(info, 'currency', 'RUB')
            except Exception:
                pass
            
            if price is None or price != price:
                hist = stock.history(period="2d")
                if not hist.empty:
                    price = float(hist['Close'].iloc[-1])
                    if len(hist) > 1:
                        prev_close = float(hist['Close'].iloc[-2])

            market_data[name] = {
                "symbol": symbol,
                "price": round(price, 2) if price is not None else None,
                "previous_close": round(prev_close, 2) if prev_close is not None else None,
                "currency": currency,
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"[OK] {name} ({symbol}): {market_data[name]['price']} {currency}")

        except Exception as e:
            print(f"[GRESKA] {name} ({symbol}): {e}")
            market_data[name] = {
                "symbol": symbol,
                "error": str(e),
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    with open("berze_rusija_nafta.json", "w", encoding="utf-8") as f:
        json.dump(market_data, f, ensure_ascii=False, indent=4)

    print("\n[USPEH] Podaci su sačuvani u 'berze_rusija_nafta.json'")

if __name__ == "__main__":
    fetch_market_data()
