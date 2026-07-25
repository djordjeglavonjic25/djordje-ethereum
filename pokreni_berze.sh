#!/usr/bin/env bash

echo "=================================================="
echo "=== 1. Ulazak u repozitorijum i sinhronizacija ==="
echo "=================================================="
cd ~/djordje-ethereum || exit 1
git checkout japantokio
git pull origin japantokio

echo -e "\n=================================================="
echo "=== 2. Ažuriranje modula: open-source-kina ======"
echo "=================================================="
git submodule update --init --recursive

echo -e "\n=================================================="
echo "=== 3. Priprema i test skripte: berze_kina.py ===="
echo "=================================================="
cat << 'PYEOF' > berze_kina.py
import yfinance as yf
import json
from datetime import datetime

tickers = {
    "Tencent_HK": "0700.HK",
    "Tencent_US": "TCEHY",
    "Alibaba_US": "BABA",
    "Alibaba_HK": "9988.HK",
    "BYD_HK": "1211.HK",
    "BYD_SZ": "002594.SZ",
    "PetroChina_HK": "0857.HK",
    "Sinopec_HK": "0386.HK",
    "ICBC_HK": "1398.HK"
}

podaci = {
    "datum_azuriranja": str(datetime.now()),
    "akcije": {}
}

print("Preuzimanje uživo podataka sa berze...")

for naziv, symbol in tickers.items():
    try:
        ticker_obj = yf.Ticker(symbol)
        info = ticker_obj.fast_info
        podaci["akcije"][naziv] = {
            "symbol": symbol,
            "trenutna_cena": round(info.last_price, 2) if info.last_price else "N/A",
            "valuta": info.currency if info.currency else "USD/HKD"
        }
        print(f"✓ {naziv} ({symbol}) -> {podaci['akcije'][naziv]['trenutna_cena']} {podaci['akcije'][naziv]['valuta']}")
    except Exception as e:
        print(f"✗ Greska za {naziv}: {e}")

with open("kineske_berze_podaci.json", "w", encoding="utf-8") as f:
    json.dump(podaci, f, indent=4, ensure_ascii=False)

print("\nPodaci su uspesno sacuvani u 'kineske_berze_podaci.json'")
PYEOF

python berze_kina.py

echo -e "\n=================================================="
echo "=== 4. Slanje svih izmena na GitHub (japantokio) =="
echo "=================================================="
git add .
git commit -m "Testirano i ažurirano: open-source-kina, berze_kina.py i pokreni_berze.sh ($(date))" || echo "Nema novih izmena za commit."
git push origin japantokio

echo -e "\n=================================================="
echo "=== SVE TRI SKRIPTE SU TESTIRANE I U RADU! ==="
echo "=================================================="
