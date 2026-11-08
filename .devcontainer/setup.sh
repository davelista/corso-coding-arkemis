#!/usr/bin/env bash
# Prepara PostgreSQL dentro il Codespace e crea il database "prova".
set -e
sudo apt-get update -qq
sudo apt-get install -y -qq postgresql
sudo service postgresql start
sudo -u postgres createuser --superuser "$USER" 2>/dev/null || true
createdb prova 2>/dev/null || true
git config --global init.defaultBranch main
echo "Pronto: lancia 'python3 giorno-01/setup/check_setup.py'. Ricorda: ogni volta che il Codespace riparte, 'sudo service postgresql start'."
