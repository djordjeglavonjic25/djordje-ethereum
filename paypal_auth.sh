#!/bin/bash

# Provjera jesu li varijable postavljene u Termuxu
if [ -z "$PAYPAL_CLIENT_ID" ] || [ -z "$PAYPAL_SECRET" ]; then
    echo "Greška: PAYPAL_CLIENT_ID ili PAYPAL_SECRET nisu postavljeni u Termuxu!"
    exit 1
fi

echo "Dohvaćam PayPal pristupnog tokena na siguran način..."
curl -s -X POST "https://api-m.sandbox.paypal.com/v1/oauth2/token" \
  -u "$PAYPAL_CLIENT_ID:$PAYPAL_SECRET" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"
