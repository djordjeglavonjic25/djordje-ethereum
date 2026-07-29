def setup_keys():
    print("--- AUTOMATSKI UNOS API KLJUCEVA ---")
    key = input("Unesi API_KEY: ")
    secret = input("Unesi API_SECRET: ")
    
    with open(".env", "w") as f:
        f.write(f"API_KEY={key}\n")
        f.write(f"API_SECRET={secret}\n")
    
    print("✅ Ključevi su uspješno sačuvani u .env fajl!")

if __name__ == "__main__":
    setup_keys()
