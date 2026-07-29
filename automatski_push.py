import subprocess
import os

def izvrsi_komandu(komanda):
    rezultat = subprocess.run(komanda, shell=True, capture_output=True, text=True)
    if rezultat.returncode != 0:
        print(f"Greška pri izvršavanju '{komanda}':\n{rezultat.stderr}")
    else:
        print(rezultat.stdout)
    return rezultat.returncode == 0

print("Pokretanje automatskog i autorizacionog git push procesa...")

izvrsi_komandu("git config --global user.email '236400041+djordjeglavonjic25@users.noreply.github.com'")
izvrsi_komandu("git config --global user.name 'djordjeglavonjic25'")

izvrsi_komandu("git add .")
izvrsi_komandu("git commit -m 'Automatsko ažuriranje i sinhronizacija svih regionalnih finansijskih skripti'")

# Slanje promena na udaljeni repozitorijum sa autorizacionom granom japantokio
uspeh = izvrsi_komandu("git push origin japantokio")

if uspeh:
    print("Uspešno izvršen automatski push na grani japantokio u repozitorijumu djordje-ethereum.")
else:
    print("Push nije uspeo. Proverite pristupne podatke ili git konfiguraciju.")
