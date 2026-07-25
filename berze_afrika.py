from datetime import datetime
import json
import yfinance as yf

CUSTOM_AUTORIZACIONI_KOD = "djordje2026"


def autorizacija():
  uneseni_kod = input(
      "Unesi custom autorizacioni kod za pokretanje berzanske skripte: "
  )
  if uneseni_kod == CUSTOM_AUTORIZACIONI_KOD:
    print("Autorizacija uspešna! Pokrećem prikupljanje podataka...")
    return True
  else:
    print("Greška: Pogrešan autorizacioni kod!")
    return False


if __name__ == "__main__":
  if autorizacija():
    simboli = {"FTSE_JSE_Top_40": "^JTOPI.JO", "EGX_30": "^EGX30.CA"}

    rezultati = {
        "timestamp": datetime.utcnow().isoformat(),
        "trziste": "Afrika",
        "podaci": {},
    }

    for naziv, simbol in simboli.items():
      try:
        t = yf.Ticker(simbol)
        hist = t.history(period="1d")
        if not hist.empty:
          trenutna_cena = hist["Close"].iloc[-1]
          rezultati["podaci"][naziv] = {
              "simbol": simbol,
              "cena": round(float(trenutna_cena), 2),
          }
      except Exception as e:
        print(f"Greska za {naziv}: {e}")

    fajl_naziv = "berze_afrika_podaci.json"
    with open(fajl_naziv, "w", encoding="utf-8") as f:
      json.dump(rezultati, f, ensure_ascii=False, indent=4)

    print(f"Uspesno sacuvano u {fajl_naziv}")
