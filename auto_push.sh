#!/bin/bash
cd ~/djordje-ethereum
python berze_integracija.py
git add podaci/berze_status.json berze_integracija.py
git commit -m "Automatsko azuriranje berzi i sinhronizacija"
git push origin japantokio
