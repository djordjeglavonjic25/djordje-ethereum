#!/bin/bash
while true; do
  git add .
  git commit -m "Auto-sync: $(date)" || true
  git push origin japantokio
  sleep 300
done
