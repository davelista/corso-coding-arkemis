# Checklist di setup · Windows con WSL 2

Si lavora **dentro Ubuntu**, non in PowerShell: da qui in poi i comandi sono gli stessi di Linux.
Ogni passo finisce con una verifica: se risponde, colora la casella del semaforo su Mural.

## 0 · WSL 2 e Ubuntu (fatto prima di pranzo)
In PowerShell:
```powershell
wsl -l -v
```
Devi vedere `Ubuntu` con `VERSION 2`. Se non c'è: PowerShell **come amministratore** → `wsl --install` → riavvia il PC.
Al primo avvio di Ubuntu (menu Start → Ubuntu) crea nome utente e password: **segnateli**, servono per `sudo`.
Errore sulla virtualizzazione: scrivi nel canale domande e passa a Codespaces per oggi.

Da qui in poi **tutti i comandi vanno nel terminale di Ubuntu**. Con `sudo` la password non si vede mentre la scrivi.

## 1 · Git
```bash
sudo apt update
sudo apt install -y git
git --version
git config --global user.name "Nome Cognome"
git config --global user.email "la-stessa-email-di-github@esempio.it"
git config --global init.defaultBranch main
```

## 2 · VS Code
1. **Su Windows** scarica e installa VS Code da https://code.visualstudio.com (lascia spuntato "Aggiungi al PATH").
2. In VS Code installa l'estensione **WSL** (Microsoft). Poi **Python**, **ESLint**, **Prettier**, **Ruff** (Astral), **Live Share**.
3. Nel terminale di Ubuntu:
```bash
mkdir -p ~/corso && cd ~/corso
code .
```
La prima volta ci mette un minuto: installa un piccolo server dentro Ubuntu. In basso a sinistra di VS Code deve comparire **WSL: Ubuntu**.
```bash
code --version
```

## 3 · Python 3.12 o superiore
```bash
sudo apt install -y python3 python3-venv python3-pip
python3 --version
cd ~/corso
python3 -m venv .venv
source .venv/bin/activate
python --version
deactivate
```
Se la versione è sotto 3.12: `sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt update && sudo apt install -y python3.12 python3.12-venv`, poi usa `python3.12`.

## 4 · Node LTS con nvm
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```
Chiudi e riapri il terminale di Ubuntu, poi:
```bash
nvm install --lts
node --version
npm --version
```

## 5 · PostgreSQL
```bash
sudo apt install -y postgresql
sudo service postgresql start
sudo -u postgres createuser --superuser "$USER"
createdb prova
psql -d prova -c "select 1"
```
✅ Verifica: stampa `1`.
Nota: in WSL il servizio **non riparte da solo** dopo un riavvio. Ogni mattina: `sudo service postgresql start` (lo ricorderemo in aula).

## 6 · GitHub CLI
```bash
sudo mkdir -p -m 755 /etc/apt/keyrings
wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install -y gh
gh auth login
```
Risposte: **GitHub.com** → **HTTPS** → **Yes** → **Login with a web browser**. Da WSL il browser a volte non si apre da solo: copia l'indirizzo e il codice che `gh` mostra e incollali nel browser di Windows.
```bash
gh auth status
```

## 7 · Verifica finale
```bash
cd ~/corso
python3 check_setup.py
```
Tutto `[OK]`? Screenshot sulla tua riga del semaforo. Una riga `[KO]`: torna a quel passo. Bloccato da 30 minuti: Codespaces.

## I file: dove stanno
Tieni i progetti dentro Ubuntu (`~/corso`), non in `/mnt/c/...`: è molto più veloce e Git non si confonde con i permessi di Windows. Da Esplora file li trovi in `\\wsl$\Ubuntu\home\<utente>\corso`.
