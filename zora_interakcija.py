import os
import requests
from dotenv import load_dotenv

# Ucitavanje kljuceva iz .env fajla
load_dotenv()

novcanik = os.getenv("ZORA_WALLET_ADDRESS")

# Koristimo stabilan Blockscout API za Zora mrezu
url = f"https://explorer.zora.energy/api?module=account&action=balance&address={novcanik}"

try:
    response = requests.get(url)
    data = response.json()

    if data.get("status") == "1" and "result" in data:
        # API vraca stanje u Wei formatu, pretvaramo u ETH
        wei_balance = int(data["result"])
        eth_balance = wei_balance / 10**18
        print(f"Uspešno povezan!")
        print(f"Stanje na Zora novčaniku {novcanik} je: {eth_balance:.6f} ETH")
    else:
        print("Zora API je vratio gresku ili je adresa neispravna.")
        print(f"Poruka sa mreze: {data.get('message')}")
except Exception as e:
    print(f"Greska pri povezivanju sa Zora Explorerom: {e}")
