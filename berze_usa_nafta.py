import yfinance as yf
import json
from datetime import datetime

# Mapa kompanija i njihovih berzanskih simbola (Tickers)
companies = {
    "ExxonMobil": "XOM",
    "Chevron": "CVX",
    "ConocoPhillips": "COP",
    "Occidental Petroleum": "OXY",
    "EOG Resources": "EOG",
    "Devon Energy": "DVN"
}

market_data = {}

print("--- Preuzimanje podataka za SAD naftne gigante ---")

for name, symbol in companies.items():
    try:
        stock = yf.Ticker(symbol)
        info = stock.fast_info
        
        # Bezbedno preuzimanje iz fast_info
        price = getattr(info, 'last_price', None)
        prev_close = getattr(info, 'previous_close', None)
        currency = getattr(info, 'currency', 'USD')
        
        # Rezervni mehanizam ako fast_info ne vrati cenu
        if price is None:
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

# Cuvanje podataka u JSON fajl
with open("berze_usa_nafta.json", "w", encoding="utf-8") as f:
    json.dump(market_data, f, ensure_ascii=False, indent=4)

print("\n[USPEH] Podaci su sacuvani u 'berze_usa_nafta.json'")
