import json
import yfinance as yf

# Definisanje berzanskih indeksa za SAD
indeksi = {
    "S&P 500": "^GSPC",
    "Dow Jones": "^DJI",
    "NASDAQ": "^IXIC",
}

podaci = {}

for naziv, simbol in indeksi.items():
  try:
    tiker = yf.Ticker(simbol)
    istorija = tiker.history(period="1d")
    if not istorija.empty:
      cena = istorija["Close"].iloc[-1]
      podaci[naziv] = round(float(cena), 2)
    else:
      podaci[naziv] = None
  except Exception as e:
    print(f"Greška za {naziv}: {e}")
    podaci[naziv] = None

# Upisivanje u JSON fajl
with open("berze_sad_podaci.json", "w", encoding="utf-8") as f:
  json.dump(podaci, f, ensure_ascii=False, indent=4)

print("Podaci za SAD berze su uspešno sačuvani u berze_sad_podaci.json")
