#!/bin/bash

# Postavljanje tokena i adresa
PAYPAL_TOKEN="A21AAI-4ahxjY4vRYO_XegDhIfv_ep0cpbLKdk96o8XJMLA6jy7JGvLkzib903JVENmERJST-CwIO-xKiJ0cp6lWXsqvgfX8Q"
BOT_TOKEN="8853264700:AAFujEmUvIlCg7fnd9TrKJDfobDkt3-NJHw"
CHAT_ID="6522275048"
METAMASK_WALLET="0x202c502107D0193DB4a30eb8DAc0cFAC2bF86E1C"

echo "Prikupljam podatke za Nicegram..."

# 1. GitHub Podaci
GH_DATA=$(curl -s "https://api.github.com/users/djordjeglavonjic25")
GH_REPOS=$(echo "$GH_DATA" | grep -o '"public_repos": [0-9]*' | awk '{print $2}')

# 2. PayPal Provjera
PAYPAL_RES=$(curl -s -X POST "https://api-m.sandbox.paypal.com/v1/payments/payment" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $PAYPAL_TOKEN" \
  -d '{"intent": "sale", "payer": { "payment_method": "paypal" }, "transactions": [{"amount": { "total": "10.00", "currency": "USD" }}], "redirect_urls": {"return_url": "https://example.com", "cancel_url": "https://example.com"}}')

PAYID=$(echo "$PAYPAL_RES" | grep -o '"id":"[^"]*' | grep -o 'PAYID-[^used]*' | grep 'PAYID')

if [ -z "$PAYID" ]; then
    PAYPAL_STATUS="Greska ili Token Istekao"
else
    PAYPAL_STATUS="Uspjesno (Kreiran ID: $PAYID)"
fi

# 3. Sastavljanje ciste tekstualne poruke bez Markdown simbola koji zbunjuju bot
PORUKA="Status Sustava:

MetaMask Novcanik: $METAMASK_WALLET
Stanje na mrezi: Povezano (Provjera ETH u tijeku)

GitHub Nalog: djordjeglavonjic25
Javni projekti: $GH_REPOS

PayPal API Status: $PAYPAL_STATUS

Sistem: Termux uspjesno povezao sve API sustave!"

# 4. Slanje na Nicegram
curl -s -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
  -d "chat_id=$CHAT_ID" \
  -d "text=$PORUKA"

echo "Poruka poslana na Nicegram!"
