# Checklist di setup · macOS

Apri il **Terminale** (Cmd+Spazio, scrivi `Terminale`). Ogni passo finisce con una verifica: se risponde, colora la casella del semaforo su Mural.
Se un comando dice `command not found` subito dopo un'installazione: chiudi e riapri il Terminale (è il PATH).

## 0 · Homebrew, il gestore di pacchetti
```bash
brew --version
```
Se non c'è: incolla il comando di installazione da https://brew.sh e segui le istruzioni a schermo (chiede la password del Mac, non si vede mentre la scrivi). Alla fine esegui le due righe che Homebrew ti mostra per aggiungerlo al PATH.

## 1 · Git
```bash
brew install git
git --version
git config --global user.name "Nome Cognome"
git config --global user.email "la-stessa-email-di-github@esempio.it"
git config --global init.defaultBranch main
git config --list
```
✅ Verifica: `git --version` risponde con una versione e `git config --list` mostra nome ed email.

## 2 · VS Code
1. Scarica da https://code.visualstudio.com e trascina l'app in Applicazioni.
2. Apri VS Code → Cmd+Shift+P → scrivi **Shell Command: Install 'code' command in PATH** → Invio.
3. Estensioni (Cmd+Shift+X): **Python** (Microsoft), **ESLint**, **Prettier**, **Ruff** (Astral), **Live Share**.
```bash
code --version
```

## 3 · Python 3.12 o superiore
```bash
brew install python@3.12
python3 --version
mkdir -p ~/corso && cd ~/corso
python3 -m venv .venv
source .venv/bin/activate
python --version
deactivate
```
✅ Verifica: `python3 --version` ≥ 3.12 e il prompt mostra `(.venv)` dopo `source`.

## 4 · Node LTS con nvm
```bash
brew install nvm
mkdir -p ~/.nvm
```
Aggiungi al file `~/.zshrc` le righe che `brew` ti ha mostrato a fine installazione (iniziano con `export NVM_DIR`). Poi chiudi e riapri il Terminale.
```bash
nvm install --lts
node --version
npm --version
```
✅ Verifica: `node --version` ≥ 20.

## 5 · PostgreSQL
```bash
brew install postgresql@16
brew services start postgresql@16
```
Chiudi e riapri il Terminale, poi:
```bash
createdb prova
psql -d prova -c "select 1"
```
✅ Verifica: stampa `1`. Con Homebrew l'utente del database è il tuo utente del Mac, senza password.
Errore `connection refused`: il servizio è spento → `brew services start postgresql@16`.

## 6 · GitHub CLI
```bash
brew install gh
gh auth login
```
Risposte: **GitHub.com** → **HTTPS** → **Yes** (usa le credenziali per Git) → **Login with a web browser**. Copia il codice, premi Invio, conferma nel browser.
```bash
gh auth status
```

## 7 · Verifica finale
```bash
cd ~/corso
python3 check_setup.py
```
Tutto `[OK]`? Screenshot sulla tua riga del semaforo. Una riga `[KO]`: torna a quel passo. Bloccato da 30 minuti: Codespaces.
