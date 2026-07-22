#!/bin/bash
git add .
git commit -m "Automatsko azuriranje: $(date)"
git push origin main
