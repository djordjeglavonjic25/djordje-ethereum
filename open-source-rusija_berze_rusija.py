import os
import json
import subprocess
import yfinance as yf
from datetime import datetime

print("==================================================")
print("=== 1. Osvežavanje otvorenih kodova (Rusija) ===")
print("==================================================")

os.makedirs("open-source-rusija", exist_ok=True)

submoduli = [
    ("open-source-rusija/yandex-userver", "https://github.com/yandex/userver.git"),
    ("open-source-rusija/sber-kandinsky", "https://github.com/ai-forever/Kandinsky-3.git")
]

for putanja, url in submoduli:
    if not os.path.exists(putanja):
        subprocess.run(["git", "submodule", "add", url, putanja], check=False)

subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=False)

print("\n==================================================")
print("=== 2. Preuzimanje podataka sa berze (MOEX) ======")
print("==================================================")

tickers = {
    "Gazprom": "GAZP.ME",
    "Rosneft": "ROSN.ME",
    "Lukoil": "LKOH.ME",
    "Sberbank": "SBER.ME",
    "Yandex": "YDEX.ME",
    "Norilsk_Nickel": "GMKN.ME"
}

podaci = {
    "datum_azuriranja": str(datetime.now()),
    "akcije": {}
}

for naziv, symbol in tickers.items():
    try:
        ticker_obj = yf.Ticker(symbol)
        info = ticker_obj.fast_info
        podaci["akcije"][naziv] = {
            "symbol": symbol,
            "trenutna_cena": round(info.last_price, 2) if info.last_price else "N/A",
            "valuta": info.currency if info.currency else "RUB"
        }
        print(f"✓ {naziv} ({symbol}) -> {podaci['akcije'][naziv]['trenutna_cena']} {podaci['akcije'][naziv]['valuta']}")
    except Exception as e:
        print(f"✗ Greska za {naziv}: {e}")

with open("ruske_berze_podaci.json", "w", encoding="utf-8") as f:
    json.dump(podaci, f, indent=4, ensure_ascii=False)

print("\nPodaci su uspešno sačuvani u 'ruske_berze_podaci.json'")
