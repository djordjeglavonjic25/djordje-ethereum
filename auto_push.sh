#!/bin/bash
cd ~/djordje-ethereum

echo "Provera git statusa..."
git status

git add podaci/berze_status.json berze_integracija.py auto_push.sh

if git diff-index --quiet HEAD --; then
    echo "Nema novih promena za commit."
else
    git commit -m "Automatska sinhronizacija celokupnog jutrasnjeg rada i berza"
    echo "Pokrecem git push prema GitHub-u..."
    git push origin japantokio
    echo "Sinhronizacija uspesno završena!"
fi
