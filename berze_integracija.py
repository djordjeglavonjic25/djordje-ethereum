import os
import json
import requests
import yfinance as yf
import pandas as pd

def prikupi_podatke():
    simboli = {
        "Kina_Alibaba": "BABA",
        "Kina_Tencent": "TCEHY",
        "Rusija_Gazprom": "OGZPY"
    }
    
    rezultati = {}
    for naziv, simbol in simboli.items():
        try:
            tacka = yf.Ticker(simbol)
            istorija = tacka.history(period="1d")
            if not istorija.empty:
                cena = istorija['Close'].iloc[-1]
                rezultati[naziv] = {"simbol": simbol, "poslednja_cena": float(cena)}
        except Exception as e:
            rezultati[naziv] = {"greska": str(e)}

    os.makedirs("podaci", exist_ok=True)
    fajl_putanja = "podaci/berze_status.json"
    
    with open(fajl_putanja, "w", encoding="utf-8") as f:
        json.dump(rezultati, f, ensure_ascii=False, indent=4)
    
    print(f"Podaci sacuvani u {fajl_putanja}")

if __name__ == "__main__":
    prikupi_podatke()
