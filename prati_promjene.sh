#!/bin/bash

echo "========================================="
echo " Započinje praćenje i ažuriranje kodova "
echo "========================================="

# Funkcija za povlačenje novih izmena sa zvaničnog Ethereum repozitorijuma
azuriraj_izvor() {
    if [ -d "$1" ]; then
        echo "[+] Provera zvaničnih izmena za folder: $1"
        cd "$1"
        
        # Ako upstream (originalni izvor) nije podešen, dodajemo ga
        if ! git remote | grep -q "upstream"; then
            git remote add upstream "https://github.com/ethereum/$1.git" 2>/dev/null
        fi
        
        # Povlačenje i spajanje novih kodova sa zvaničnog repozitorijuma
        git fetch upstream
        if git branch -r | grep -q "upstream/main"; then
            git merge upstream/main --no-edit 2>/dev/null
        fi
        if git branch -r | grep -q "upstream/master"; then
            git merge upstream/master --no-edit 2>/dev/null
        fi
        if git branch -r | grep -q "upstream/dev"; then
            git merge upstream/dev --no-edit 2>/dev/null
        fi
        cd ..
    fi
}

# Spisak svih do sada preuzetih projekata za proveru novih kodova
projekti=(
    "eth-rnd-archive" "forkcast" "EIPs" "go-ethereum" "consensus-specs" 
    "ethereum-org-website" "ethspecify" "esp-website" "beacon-APIs" 
    "epbs-security-analysis" "hive" "devp2p" "sys-asm" "execution-spec-tests" 
    "steel" "protocol-prototyping-site" "kohaku" "cryptography-specs"
)

for p in "${projekti[@]}"; do
    azuriraj_izvor "$p"
done

echo "-----------------------------------------"
echo " Snimanje tvojih izmena i slanje na GitHub "
echo "-----------------------------------------"

# Registrovanje svih lokalnih izmena u kodu, novih fajlova i ažuriranih podovnih foldera
git add .

# Slanje izmena na tvoj djordje-ethereum repozitorijum u granu Dzen
if git commit -m "Automatsko praćenje, izmena kodova i osvežavanje Ethereum izvora" 2>/dev/null; then
    echo "[+] Pronađene su nove izmene. Šaljem na GitHub..."
    git push origin Dzen
else
    echo "[~] Nema novih izmena u kodu za slanje."
fi

echo "========================================="
echo " Ažuriranje završeno! Sve je sinhronizovano. "
echo "========================================="
