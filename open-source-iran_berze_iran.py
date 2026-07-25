import os, json, subprocess, yfinance as yf
from datetime import datetime

os.makedirs("open-source-iran", exist_ok=True)
if not os.path.exists("open-source-iran/iran-open-data"):
    subprocess.run(["git", "submodule", "add", "https://github.com/iran-open-data/datasets.git", "open-source-iran/iran-open-data"], check=False)
subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=False)

kompanije = {
    "Iran_Khodro_IKCO": "IKCO.TE",
    "Saipa": "SAIPA.TE",
    "Mobarakeh_Steel": "FOLD.TE",
    "NIOC_National_Iranian_Oil": "STATE_OWNED",
    "NPC_National_Petrochemical": "STATE_OWNED"
}

podaci = {"datum_azuriranja": str(datetime.now()), "kompanije": {}}
print(f"--- AŽURIRANJE IRANSKIH BERZI [{datetime.now().strftime('%H:%M:%S')}] ---")

for naziv, symbol in kompanije.items():
    if symbol != "STATE_OWNED":
        try:
            cena = round(yf.Ticker(symbol).fast_info.last_price, 2)
        except Exception:
            cena = "Pratnja aktivna (TSE)"
        podaci["kompanije"][naziv] = {"symbol": symbol, "trenutna_cena": cena, "valuta": "IRR"}
    else:
        podaci["kompanije"][naziv] = {"symbol": symbol, "trenutna_cena": "Državni gigant", "valuta": "N/A"}
    
    print(f"✓ {naziv} -> {podaci['kompanije'][naziv]['trenutna_cena']}")

with open("iranske_berze_podaci.json", "w", encoding="utf-8") as f:
    json.dump(podaci, f, indent=2, ensure_ascii=False)

print("\nPodaci su uspešno sačuvani u 'iranske_berze_podaci.json'")
