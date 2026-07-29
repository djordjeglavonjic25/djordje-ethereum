import urllib.request, json
url = "http://www.tsetmc.com/tsev2/data/MarketWatchInit.aspx?h=0&r=0"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=5) as res:
        content = res.read().decode('utf-8')
        parts = content.split(';')[:20]
        rows = [{'Symbol': p.split(',')[2], 'Name': p.split(',')[3]} for p in parts if len(p.split(',')) > 3]
    with open("iran_podaci.json", "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=4)
    print("Ok")
except Exception as e:
    print(f"Greska: {e}")
