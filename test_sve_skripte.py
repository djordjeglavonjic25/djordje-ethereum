import subprocess
import os

skripte = [
    "amerika_finansije.py",
    "evropa_finansije.py",
    "rusija_finansije.py",
    "kina_finansije.py",
    "iran_finansije.py",
    "afrika_finansije.py",
    "australija_finansije.py"
]

print("Pokretanje testiranja i ažuriranja svih skripti...")

for skripta in skripte:
    if os.path.exists(skripta):
        print(f"\n--- Izvršavam: {skripta} ---")
        rezultat = subprocess.run(["python", skripta], capture_output=True, text=True)
        print(rezultat.stdout)
        if rezultat.stderr:
            print(f"Greška u {skripta}:\n{rezultat.stderr}")
    else:
        print(f"\nFajl {skripta} ne postoji.")

print("\nTestiranje i ažuriranje svih modula je završeno.")
