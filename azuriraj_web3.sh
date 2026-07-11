#!/bin/bash

echo "=== Pokretanje automatskog ažuriranja ==="

# 1. Povuci najnovije izmene sa GitHub-a za svaki slučaj
echo "Provera Git repozitorijuma..."
git pull origin japantokio

# 2. Automatsko ažuriranje Web3Auth biblioteke za Python
echo "Provera i ažuriranje Web3Auth SDK-a..."
pip install --upgrade web3auth

# 3. PRIMENA WORKAROUND-A:
# Ova komanda prolazi kroz sve .py fajlove i briše liniju 'is_mfa_settings=False'
# jer izostavljanje tog parametra rešava bag na Web3Auth serveru.
echo "Primenjujem privremeno rešenje za MFA bag (izbacivanje parametra)..."
find . -name "*.py" -exec sed -i '/is_mfa_settings.*[Ff]alse/d' {} +
find . -name "*.py" -exec sed -i '/mfaSettings.*[Ff]alse/d' {} +

# 4. Automatski Git Push ako ima izmena
echo "Provera statusa radnog direktorijuma..."
if [[ -n $(git status --porcelain) ]]; then
    echo "Pronađene su izmene. Automatsko slanje na GitHub..."
    git add .
    git commit -m "Automatsko ažuriranje SDK-a i primena MFA fix-a"
    git push origin japantokio
    echo "Sve je uspešno ažurirano i gurnuto na GitHub!"
else
    echo "Nema novih izmena u kodu niti potrebe za push-om."
fi

echo "=== Završeno ==="
# Test
