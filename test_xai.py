import os
import requests
from dotenv import load_dotenv

load_dotenv()

XAI_KEY = os.getenv("XAI_API_KEY")

print("=== SpaceX API Test ===")
headers = {"User-Agent": "Mozilla/5.0 (Termux; Android)"}

try:
    response = requests.get("https://api.spacexdata.com/v4/launches/latest", headers=headers, timeout=10)
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Najnovije SpaceX lansiranje: {data.get('name')}")
    else:
        print(f"⚠️ SpaceX API status kod: {response.status_code}")
except Exception as e:
    print(f"❌ Greška pri konekciji sa SpaceX-om: {e}")

print("\n=== xAI SDK Test ===")
if XAI_KEY and XAI_KEY != "VAŠ_XAI_API_KEY":
    try:
        from xai_sdk import Client
        client = Client(api_key=XAI_KEY)
        print("✅ xAI Klijent je uspješno inicijalizovan!")
    except Exception as e:
        print(f"❌ Greška pri pokretanju xAI SDK: {e}")
else:
    print("ℹ️ Unesite stvarni XAI_API_KEY u .env fajl ako želite koristiti xAI.")
