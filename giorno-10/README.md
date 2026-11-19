# Giorno 10 · Chiave e biglietto

Chi bussa alla porta? Stamattina la risposta più semplice: **la chiave** (API Key), quella che usano i programmi. Una stringa segreta in un header: il server la confronta con la sua copia, e risponde 200 o 401. Poi **il biglietto** (JWT), accanto alla chiave. E poi le funzioni di sicurezza le **costruiamo insieme, da zero**.

Il pomeriggio è solo esercizio: la fabbrica di Wonka, da capo, a due livelli. **Al latte**: le funzioni di sicurezza già pronte, in `main.py` solo indizi. **Fondente**: le funzioni di sicurezza le riscrivete voi.

| Quando | Cartella | Cosa |
|---|---|---|
| 10:20 | [`chiave/`](chiave/README.md) | **Il magazzino di Wonka**: il controllore delle chiavi (insieme), poi `POST /consegne` (a gruppi) |
| 11:30 | [`insieme/`](insieme/README.md) | **Costruiamolo insieme**: password, biglietto, controllore, da zero |
| 14:00 | [`wonka/`](wonka/README.md) | **La fabbrica, al latte**: `sicurezza.py` pronto, voi scrivete le rotte |
| 14:00 | [`wonka-fondente/`](wonka-fondente/README.md) | **La fabbrica, fondente**: prima `sicurezza.py`, poi le rotte |

## Una volta sola: il materiale e il venv di oggi

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-10
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi il venv, come ieri. Le librerie sono le stesse di ieri: il venv di oggi serve per tutte le cartelle.

```bash
python3 --version            # deve dire 3.12 o più
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Ogni volta che aprite un terminale nuovo, il venv va riacceso: `cd ~/corso-coding-arkemis/giorno-10` e `source .venv/bin/activate`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `python3 --version` dice meno di 3.12 | `rm -rf .venv`, poi `python3.12 -m venv .venv`, di nuovo `source` e `pip install` |
| `command not found: fastapi` oppure `No module named …` | Il venv è spento: `source .venv/bin/activate` dalla cartella `giorno-10` |
| `Address already in use` | C'è già un server acceso in un altro terminale. Spegnetelo con Ctrl+C, oppure: `fastapi dev main.py --port 8001` |
| `connection failed` / `Connection refused` | PostgreSQL è spento. WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| Postman: `Could not send request` / `ECONNREFUSED` | Il server è spento, oppure state usando Postman nel browser: serve l'app desktop |
