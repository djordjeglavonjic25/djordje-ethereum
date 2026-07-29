cd ~/djordje-ethereum || cd /sdcard/djordje-ethereum
git checkout japantokio || git checkout -b japantokio

# Kreiranje fajla sa skriptom
cat << 'EOF' > us_mjenjacnice_sync.sh
#!/bin/bash
mkdir -p US-Mjenjacnice-Konektor

cat << 'JSONEOF' > US-Mjenjacnice-Konektor/us_mjenjacnice.json
{
    "klasicne_mjenjacnice": [
        {"name": "Travelex", "link": "travelex.com", "desc": "Najpoznatiji lanac fizičkih mjenjačnica u SAD-u."},
        {"name": "Western Union", "link": "westernunion.com", "desc": "Globalni gigant za slanje i prijem novca."},
        {"name": "MoneyGram", "link": "moneygram.com", "desc": "Brzi međunarodni transferi i konverzija valuta."},
        {"name": "Wise", "link": "wise.com", "desc": "Digitalni servis za konverziju valuta sa srednjim tržišnim kursom."},
        {"name": "Remitly", "link": "remitly.com", "desc": "Digitalni servis za slanje novca iz SAD-a u inostranstvo."}
    ],
    "e_mjenjacnice": [
        {"name": "Coinbase", "link": "coinbase.com", "desc": "Najveća kripto mjenjačnica u SAD-u pod SEC nadzorom."},
        {"name": "Kraken", "link": "kraken.com", "desc": "Starija i pouzdana kripto mjenjačnica sa sjedištem u SAD-u."},
        {"name": "Gemini", "link": "gemini.com", "desc": "Kripto mjenjačnica sa velikim fokusom na sigurnost i usklađenost."},
        {"name": "Binance.US", "link": "binance.us", "desc": "Američka verzija Binance platforme prilagođena lokalnim propisima."},
        {"name": "Crypto.com", "link": "crypto.com", "desc": "Mobilna platforma za e-razmjenu valuta prisutna na US tržištu."},
        {"name": "Robinhood", "link": "robinhood.com", "desc": "Trgovanje dionicama i osnovnim kriptovalutama bez provizija."}
    ]
}
JSONEOF

git add US-Mjenjacnice-Konektor/us_mjenjacnice.json us_mjenjacnice_sync.sh
git commit -m "Dodata skripta us_mjenjacnice_sync.sh i podaci za US mjenjačnice"
git push origin japantokio
echo "Uspješno završeno!"
EOF

# Dati dozvolu skripti da se može pokretati
chmod +x us_mjenjacnice_sync.sh
