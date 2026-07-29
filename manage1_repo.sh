#!/bin/bash

# ==========================================
# Glavna menadžerska skripta za repozitorijum
# Repozitorijum: djordje-kaspersky
# ==========================================

BRANCHES=("japantokio" "main" "dev" "staging")

# Funkcija za popravku i resetovanje Git stanja
fix_git_state() {
    echo ""
    echo "==> [1/3] Proveravam Git status..."
    git status

    if [ $? -ne 0 ]; then
        echo "GRESKA: Ovo nije Git repozitorijum!"
        return 1
    fi

    echo "==> Prekidam aktivne procese spajanja/rebase-ovanja..."
    git merge --abort 2>/dev/null
    git rebase --abort 2>/dev/null

    echo "==> Osvežavam podatke sa udaljenog servera (fetch origin)..."
    git fetch origin --all --prune

    echo "==> Git okruženje je uspešno očišćeno i spremno za rad!"
}

# Funkcija za sinhronizaciju svih grana pojedinačno
sync_branches() {
    echo ""
    echo "==> [2/3] Pokrećem sinhronizaciju za sve grane..."
    
    CURRENT_BRANCH=$(git symbolic-ref --short HEAD)
    echo "==> Trenutna grana: $CURRENT_BRANCH"

    git fetch origin --all

    for branch in "${BRANCHES[@]}"; do
        echo "--------------------------------------------------"
        echo "==> Obrađujem granu: $branch"
        
        git checkout "$branch" 2>/dev/null
        if [ $? -ne 0 ]; then
            echo "UPOZORENJE: Grana '$branch' ne postoji lokalno. Kreiram je..."
            git checkout -b "$branch" "origin/$branch"
            if [ $? -ne 0 ]; then
                echo "GRESKA: Ne mogu da pronađem granu '$branch' na origin-u. Preskačem."
                continue
            fi
        fi

        git pull origin "$branch"
        git push origin "$branch"
    done

    echo "--------------------------------------------------"
    echo "==> Vraćam se na početnu granu: $CURRENT_BRANCH"
    git checkout "$CURRENT_BRANCH"

    echo "==> Sinhronizacija svih grana je uspešno završena!"
}

# Funkcija za automatski rad i saradnju (spajanje) između grana
collaborate_branches() {
    echo ""
    echo "==> [3/3] Pokrećem automatski tok spajanja (saradnju) između grana..."
    
    CURRENT_BRANCH=$(git symbolic-ref --short HEAD)

    # 1. Osveži sve
    git fetch origin --all

    # 2. Spoji dev u staging
    echo "==> Spajam 'dev' u 'staging'..."
    git checkout staging || git checkout -b staging origin/staging
    git pull origin staging
    git merge dev --no-edit || { echo "GRESKA pri spajanju dev u staging. Razreši sukobe!"; git checkout "$CURRENT_BRANCH"; return 1; }
    git push origin staging

    # 3. Spoji staging u main
    echo "==> Spajam 'staging' u 'main'..."
    git checkout main || git checkout -b main origin/main
    git pull origin main
    git merge staging --no-edit || { echo "GRESKA pri spajanju staging u main. Razreši sukobe!"; git checkout "$CURRENT_BRANCH"; return 1; }
    git push origin main

    # 4. Spoji main u japantokio
    echo "==> Spajam 'main' u 'japantokio'..."
    git checkout japantokio || git checkout -b japantokio origin/japantokio
    git pull origin japantokio
    git merge main --no-edit || { echo "GRESKA pri spajanju main u japantokio. Razreši sukobe!"; git checkout "$CURRENT_BRANCH"; return 1; }
    git push origin japantokio

    echo "--------------------------------------------------"
    echo "==> Vraćam se na početnu granu: $CURRENT_BRANCH"
    git checkout "$CURRENT_BRANCH"
    echo "==> Automatska saradnja i spajanje grana je uspešno završeno!"
}

# Glavni meni
clear
echo "=================================================="
echo "    REPOZITORIJUM MENADŽER: djordje-kaspersky"
echo "=================================================="
echo "1) Samo očisti i popravi Git stanje"
echo "2) Samo sinhronizuj sve grane sa GitHub-om"
echo "3) Automatski poveži i spoji grane (Saradnja: dev -> staging -> main -> japantokio)"
echo "4) Uradi SVE (Popravi stanje + Sinhronizuj + Spoji grane)"
echo "5) Izlaz"
echo "=================================================="
read -p "Izaberi opciju (1-5): " choice

case $choice in
    1)
        fix_git_state
        ;;
    2)
        sync_branches
        ;;
    3)
        collaborate_branches
        ;;
    4)
        fix_git_state
        sync_branches
        collaborate_branches
        ;;
    5)
        echo "Izlaz iz skripte."
        exit 0
        ;;
    *)
        echo "GRESKA: Nepoznata opcija!"
        exit 1
        ;;
esac
