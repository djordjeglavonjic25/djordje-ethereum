import telebot
import subprocess
from web3 import Web3

# Tvoj Telegram Bot Token sa slike 1000001824.jpg unijet automatski
API_TOKEN = '8853264700:AAFujEmUvIlCg7fnd9TrKJDfobDkt3-NJHw'
bot = telebot.TeleBot(API_TOKEN)

# Povezivanje na Ethereum preko stabilnog Cloudflare RPC-a
RPC_URL = "https://cloudflare-eth.com"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    dobrodoslica = (
        "🔔 *Termux Obaveštenje: Sistem je povezan!*\n\n"
        "Dostupne komande unutar Nicegrama:\n"
        "➡️ /status - Prikazuje trenutno stanje mreže i tvog GitHuba\n"
        "➡️ /osvezi - Pokreće automatsku skriptu i povlači izmene sa izvora\n"
        "➡️ /trgovina - Pokreće analizu berzi (Binance, BingX, PayPal)"
    )
    bot.reply_to(message, dobrodoslica, parse_mode='Markdown')

@bot.message_handler(commands=['status'])
def status_poruka(message):
    bot.reply_to(message, "⏳ Prikupljam Web3 podatke sa blockchaina i GitHub-a...")
    
    # Provera stanja na Ethereum mreži
    if web3.is_connected():
        blok = web3.eth.block_number
        gas_gwei = web3.from_wei(web3.eth.gas_price, 'gwei')
        stanja_mreze = f"✅ ETH Mreža na mreži\n📦 Trenutni Blok: {blok}\n⛽ Gas: {gas_gwei:.2f} Gwei"
    else:
        stanja_mreze = "❌ Greška pri čitanju mreže ETH"

    # MetaMask adresa sa slike 1000001824.jpg postavljena kao glavna za praćenje
    glavna_adresa = "0x202c502107D0193DB4a30eb8DAc0cFAC2bF86E1C"
    
    try:
        if web3.is_connected():
            balans_wei = web3.eth.get_balance(web3.to_checksum_address(glavna_adresa))
            balans = web3.from_wei(balans_wei, 'ether')
            status_balansa = f"{balans:.4f} ETH"
        else:
            status_balansa = "Greška pri čitanju mreže ETH"
    except:
        status_balansa = "Greška pri čitanju mreže ETH"

    odgovor = (
        "✅ *Web3 & Internet Trgovina Status*\n\n"
        f"🦊 *MetaMask Novčanik:* {glavna_adresa}\n"
        f"💰 Stanje na novčaniku: {status_balansa}\n\n"
        f"🌐 *Blockchain Status:*\n{stanja_mreze}\n\n"
        "🐙 *GitHub Nalog:* djordjeglavonjic25\n"
        "📁 Krovni projekat: djordje-ethereum\n\n"
        "🤖 *Sistem:* Termux uspešno prati tvoje Web3 poslovanje."
    )
    bot.reply_to(message, odgovor, parse_mode='Markdown')

@bot.message_handler(commands=['osvezi'])
def pokreni_osvezavanje(message):
    bot.reply_to(message, "🔄 Pokrećem `prati_promjene.sh` u Termuxu... Sačekaj trenutak.")
    try:
        # Pokretanje tvoje bash skripte za osvežavanje izvora i slanje na GitHub
        subprocess.run(['./prati_promjene.sh'], capture_output=True, text=True, cwd='/data/data/com.termux/files/home/djordje-ethereum')
        bot.reply_to(message, "✅ Skripta je izvršena i promjene su sinhronizovane sa GitHubom!")
    except Exception as e:
        bot.reply_to(message, f"❌ Greška prilikom pokretanja skripte: {str(e)}")

@bot.message_handler(commands=['trgovina'])
def pokreni_trgovinu(message):
    bot.reply_to(message, "📊 Pokrećem analizu integracija (Binance, BingX, PayPal)...")
    try:
        # Pokretanje berze.py skripte i slanje rezultata direktno u chat
        rezultat = subprocess.run(['python', 'berze.py'], capture_output=True, text=True, cwd='/data/data/com.termux/files/home/djordje-ethereum')
        bot.reply_to(message, f"```\n{rezultat.stdout}\n```", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"❌ Greška prilikom pokretanja berze: {str(e)}")

if __name__ == "__main__":
    print("[+] Bot je pokrenut i sluša komande sa Nicegrama...")
    bot.infinity_polling()
