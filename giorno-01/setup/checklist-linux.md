# Checklist di setup · Linux (Ubuntu / Debian)

Apri il terminale. Ogni passo finisce con una verifica: se risponde, colora la casella del semaforo su Mural.
`sudo` chiede la tua password: mentre la scrivi non compare niente, è normale.

## 0 · Aggiorna l'elenco dei pacchetti
```bash
sudo apt update
```

## 1 · Git
```bash
sudo apt install -y git
git --version
git config --global user.name "Nome Cognome"
git config --global user.email "la-stessa-email-di-github@esempio.it"
git config --global init.defaultBranch main
git config --list
```

## 2 · VS Code
1. Scarica il pacchetto `.deb` da https://code.visualstudio.com e installalo (doppio clic, oppure `sudo apt install ./code_*.deb` dalla cartella dei download).
2. Estensioni (Ctrl+Shift+X): **Python** (Microsoft), **ESLint**, **Prettier**, **Ruff** (Astral), **Live Share**.
```bash
code --version
```

## 3 · Python 3.12 o superiore
```bash
sudo apt install -y python3 python3-venv python3-pip
python3 --version
mkdir -p ~/corso && cd ~/corso
python3 -m venv .venv
source .venv/bin/activate
python --version
deactivate
```
Se `python3 --version` è sotto 3.12 (Ubuntu 22.04): `sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install -y python3.12 python3.12-venv`, poi usa `python3.12` al posto di `python3`.

## 4 · Node LTS con nvm
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```
Chiudi e riapri il terminale, poi:
```bash
nvm install --lts
node --version
npm --version
```
✅ Verifica: `node --version` ≥ 20. Se `nvm: command not found`: riapri il terminale (è il PATH).

## 5 · PostgreSQL
```bash
sudo apt install -y postgresql
sudo systemctl enable --now postgresql
sudo -u postgres createuser --superuser "$USER"
createdb prova
psql -d prova -c "select 1"
```
✅ Verifica: stampa `1`. Errore `role "tuo-nome" does not exist`: manca il passo `createuser`.
Errore `connection refused`: `sudo systemctl start postgresql`.

## 6 · GitHub CLI
```bash
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install -y gh
gh auth login
```
Risposte: **GitHub.com** → **HTTPS** → **Yes** → **Login with a web browser**. Copia il codice, Invio, conferma nel browser.
```bash
gh auth status
```

## 7 · Verifica finale
```bash
cd ~/corso
python3 check_setup.py
```
Tutto `[OK]`? Screenshot sulla tua riga del semaforo. Una riga `[KO]`: torna a quel passo. Bloccato da 30 minuti: Codespaces.
