import yfinance as yf
import pandas as pd
import json
from datetime import datetime

tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]
data_output = {}

for ticker in tickers:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1d")
    if not hist.empty:
        close_price = hist['Close'].iloc[-1]
        volume = hist['Volume'].iloc[-1]
        data_output[ticker] = {
            "close_price": float(close_price),
            "volume": int(volume),
            "timestamp": str(datetime.now())
        }

print(json.dumps(data_output, indent=4))

with open("berza_amerike.json", "w") as f:
    json.dump(data_output, f, indent=4)
