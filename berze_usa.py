import json
import os
from datetime import datetime
import yfinance as yf
import pandas as pd

# Vodeće tehnološke kompanije sa NASDAQ berze
TICKERS = {
    "AAPL": "Apple Inc.",
    "MSFT": "Microsoft Corporation",
    "NVDA": "NVIDIA Corporation",
    "GOOGL": "Alphabet Inc.",
    "META": "Meta Platforms, Inc."
}

def fetch_stock_data():
    results = []
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for symbol, name in TICKERS.items():
        try:
            ticker = yf.Ticker(symbol)
            fast_info = ticker.fast_info

            price = fast_info.get("lastPrice")
            prev_close = fast_info.get("previousClose")
            market_cap = fast_info.get("marketCap")
            currency = fast_info.get("currency", "USD")

            change = round(price - prev_close, 4) if price and prev_close else None
            change_percent = round(((price - prev_close) / prev_close) * 100, 2) if price and prev_close else None

            stock_item = {
                "symbol": symbol,
                "company_name": name,
                "exchange": "NASDAQ",
                "price": round(price, 2) if price else None,
                "currency": currency,
                "change": change,
                "change_percent": change_percent,
                "market_cap": market_cap,
                "updated_at": current_time,
                "status": "success"
            }
            results.append(stock_item)
            print(f"[OK] Preuzeti podaci za {symbol}: {stock_item['price']} {currency}")

        except Exception as e:
            print(f"[GREŠKA] Neuspješno preuzimanje za {symbol}: {e}")
            results.append({
                "symbol": symbol,
                "company_name": name,
                "exchange": "NASDAQ",
                "updated_at": current_time,
                "status": "error"
            })

    return results

def save_data(data, filename="berze_usa_data.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"\nPodaci su uspješno sačuvani u fajl: {filename}")

if __name__ == "__main__":
    print("Inicijalizacija preuzimanja podataka sa SAD berze (NASDAQ)...")
    data = fetch_stock_data()
    save_data(data)
