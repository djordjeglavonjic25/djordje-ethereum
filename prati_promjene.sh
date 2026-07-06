#!/bin/bash

echo "========================================="
echo " Započinje praćenje i ažuriranje kodova "
echo "========================================="

# Funkcija za povlačenje novih izmena sa zvaničnih izvora
azuriraj_izvor() {
    if [ -d "$1" ]; then
        echo "[+] Provera zvaničnih izmena za folder: $1"
        cd "$1"
        
        # Ako upstream (originalni izvor) nije podešen, dodajemo ga na osnovu organizacije
        if ! git remote | grep -q "upstream"; then
            if [ "$1" == "MetaMask-Ekstenzija" ]; then
                git remote add upstream "https://github.com/MetaMask/metamask-extension.git" 2>/dev/null
            elif [ "$1" == "MetaMask-Mobilna-Aplikacija" ]; then
                git remote add upstream "https://github.com/MetaMask/metamask-mobile.git" 2>/dev/null
            else
                git remote add upstream "https://github.com/ethereum/$1.git" 2>/dev/null
            fi
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

# Spisak svih projekata u tvom djordje-ethereum direktorijumu
projekti=(
    "MetaMask-Ekstenzija" "MetaMask-Mobilna-Aplikacija" "eth-rnd-archive" 
    "forkcast" "EIPs" "go-ethereum" "consensus-specs" "ethereum-org-website" 
    "ethspecify" "esp-website" "beacon-APIs" "epbs-security-analysis" "hive" 
    "devp2p" "sys-asm" "execution-spec-tests" "steel" "protocol-prototyping-site" 
    "kohaku" "cryptography-specs"
)

for p in "${projekti[@]}"; do
    azuriraj_izvor "$p"
done

echo "-----------------------------------------"
echo " Snimanje tvojih izmena i slanje na GitHub "
echo "-----------------------------------------"

git add .

if git commit -m "Automatsko pracenje, osvezavanje Ethereum i MetaMask izvora sa slike" 2>/dev/null; then
    echo "[+] Pronađene su nove izmene. Šaljem na GitHub..."
    git push origin Dzen
else
    echo "[~] Nema novih izmena u kodu za slanje."
fi

echo "========================================="
echo " Ažuriranje završeno! Sve je sinhronizovano. "
echo "========================================="
