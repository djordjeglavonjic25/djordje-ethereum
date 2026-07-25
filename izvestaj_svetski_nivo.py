# Pregled rezultata i postignutih ciljeva za globalne programske skripte
rezultati = {
    "Amerika": "Preuzeti podaci o vodećim američkim kompanijama (AAPL, MSFT, GOOGL) preko yfinance biblioteke i sačuvani u amerika_podaci.json.",
    "Evropa": "Evropski berzanski simboli i indeksi (SIE.DE, SAP.DE, STOXX50E) uspešno obrađeni i sačuvani u evropa_podaci.json.",
    "Rusija": "Uspostavljena veza sa Moskovskom berzom (MOEX) i preuzeti podaci u rusija_podaci.json.",
    "Kina": "Kineske berze obuhvaćene kroz AKShare biblioteku i sačuvane u kina_podaci.json.",
    "Iran": "Parsirani javni podaci Teheranske berze (TSETMC) i sačuvani u iran_podaci.json.",
    "Afrika": "Automatski konfigurisan sistem za preuzimanje podataka sa JSE i generisanje afrika_podaci.json.",
    "Australija": "Preuzeti podaci za australijski rudarski i finansijski sektor (BHP, RIO, CBA) u australija_podaci.json."
}

print("=== REkapitulacija Globalnih Skripti i Rezultata ==")
for region, opis in rezultati.items():
    print(f"[{region}]: {opis}")
