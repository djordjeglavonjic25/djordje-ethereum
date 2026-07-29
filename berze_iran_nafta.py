#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Open-Source Iran Energy Sector Data Tracker
Author: djordjeglavonjic25
License: MIT
Repository: djordje-ethereum
Branch: japantokio
"""

import json
from datetime import datetime

IRAN_ENERGY_COMPANIES = {
    "NIOC": {
        "full_name": "National Iranian Oil Company",
        "role": "Upravljanje resursima nafte i prirodnog gasa",
        "type": "State-Owned Monopoly",
        "status": "Active / Primary Extraction"
    },
    "NIGC": {
        "full_name": "National Iranian Gas Company",
        "role": "Prerada, transport i distribucija gasa (South Pars)",
        "type": "State-Owned Monopoly",
        "status": "Active / Midstream & Gas Infrastructure"
    },
    "NPC": {
        "full_name": "National Petrochemical Company",
        "role": "Proizvodnja i izvoz petrohemijskih derivata",
        "type": "State-Owned Subsidiary",
        "status": "Active / Downstream Petrochemicals"
    }
}

def fetch_iran_energy_data():
    market_data = {}
    print("--- Evidentiranje podataka za nacionalne energetske gigante Irana ---")

    for key, info in IRAN_ENERGY_COMPANIES.items():
        try:
            market_data[key] = {
                "company_name": info["full_name"],
                "sector_role": info["role"],
                "ownership_structure": info["type"],
                "operational_status": info["status"],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(f"[OK] {key} - {info['full_name']} | Status: {info['status']}")

        except Exception as e:
            print(f"[GRESKA] {key}: {e}")
            market_data[key] = {
                "error": str(e),
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

    with open("berze_iran_nafta.json", "w", encoding="utf-8") as f:
        json.dump(market_data, f, ensure_ascii=False, indent=4)

    print("\n[USPEH] Podaci su sačuvani u 'berze_iran_nafta.json'")

if __name__ == "__main__":
    fetch_iran_energy_data()
