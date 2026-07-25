import yfinance as yf
import pandas as pd
import numpy as np

# Evropski berzanski simboli (nemačka berza / Frankfurtska berza i evropski indeksi)
tickers = ["SIE.DE", "SAP.DE", "^STOXX50E"]
print("Preuzimanje podataka za evropske kompanije i indekse...")
data = yf.download(tickers, period="5d", interval="1d", progress=False)

if not data.empty:
    print(data.head())
    data.to_json("evropa_podaci.json", orient="index", indent=4)
    print("Podaci uspešno sačuvani u evropa_podaci.json")
else:
    print("Nema podataka.")
