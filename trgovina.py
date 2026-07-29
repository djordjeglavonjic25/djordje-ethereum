import json
from web3 import Web3

# 1. Povezivanje na Ethereum mrežu (Koristi se stabilni javni Cloudflare RPC)
# Možeš zamijeniti sa svojim Infura/Alchemy URL-om ako imaš svoj privatni ključ/node
RPC_URL = "https://cloudflare-eth.com"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# Minimalni ABI za ERC-20 tokene (potreban za čitanje balansa USDT, USDC, itd.)
ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "type": "function"
    }
]

def provjeri_mrezu():
    """Provjerava vezu sa Ethereum mrežom i trenutno stanje gasa."""
    print("=========================================")
    print(" UNIVERSALNA WEB3 ETHEREUM SKRIPTA       ")
    print("=========================================")
    
    if not web3.is_connected():
        print("[-] Greška: Nije moguće uspostaviti vezu sa Ethereum mrežom.")
        return False
        
    print("[+] Veza sa Ethereum mrežom uspješno uspostavljena!")
    trenutni_blok = web3.eth.block_number
    trenutni_gas_wei = web3.eth.gas_price
    trenutni_gas_gwei = web3.from_wei(trenutni_gas_wei, 'gwei')
    
    print(f"[+] Trenutni blok na mreži: {trenutni_blok}")
    print(f"[+] Trenutna cijena gasa: {trenutni_gas_gwei:.2f} Gwei")
    return True

def provjeri_balans_adrese(adresa):
    """Provjerava balans osnovnog ETH-a za unijetu adresu."""
    if not web3.is_address(adresa):
        print([-] Greška: Adresa {adresa} nije validna Ethereum adresa.)
        return
        
    # Dobavljanje balansa u Wei i konverzija u ETH
    balans_wei = web3.eth.get_balance(adresa)
    balans_eth = web3.from_wei(balans_wei, 'ether')
    print(f"\n[~] Analiza za adresu: {adresa}")
    print(f"    -> Native ETH Balans: {balans_eth:.6f} ETH")

def provjeri_erc20_token(adresa_novcanika, adresa_tokena):
    """Provjerava balans specifičnog ERC-20 tokena (npr. USDT) za unijetu adresu novčanika."""
    if not web3.is_address(adresa_novcanika) or not web3.is_address(adresa_tokena):
        return
        
    try:
        # Inicijalizacija pametnog ugovora za token
        ugovor = web3.eth.contract(address=web3.to_checksum_address(adresa_tokena), abi=ERC20_ABI)
        simbol = ugovor.functions.symbol().call()
        decimale = ugovor.functions.decimals().call()
        balans_sirovi = ugovor.functions.balanceOf(web3.to_checksum_address(adresa_novcanika)).call()
        
        # Konverzija u čitljiv format na osnovu decimala tokena
        balans_tokena = balans_sirovi / (10 ** decimale)
        print(f"    -> {simbol} Token Balans: {balans_tokena:.2f} {simbol}")
    except Exception as e:
        print(f"    [-] Nije moguće učitati token na adresi {adresa_tokena}: {e}")

if __name__ == "__main__":
    # Pokretanje provjere mreže
    if provjeri_mrezu():
        # Testna adresa (Vitalik Buterin)
        test_novcanik = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
        
        # Poznate adrese tokena na Ethereum Mainnetu
        USDT_ADRESA = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
        USDC_ADRESA = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
        
        # Izvršavanje analiza
        provjeri_balans_adrese(test_novcanik)
        provjeri_erc20_token(test_novcanik, USDT_ADRESA)
        provjeri_erc20_token(test_novcanik, USDC_ADRESA)
        print("=========================================")
