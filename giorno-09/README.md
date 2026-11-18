# Giorno 9 · SQLAlchemy e il biglietto d'oro

Ieri il SQL lo scrivevate voi, dentro una stringa. Stamattina lo scrive **SQLAlchemy**: le tabelle diventano classi, le righe diventano oggetti. Stessa villa, stesse rotte, meno SQL da scrivere. E per provare le rotte, oltre a `/docs`, arriva **Postman**.

Nel pomeriggio si apre la fabbrica di cioccolato: si entra solo con il **biglietto d'oro**. Registrazione, password salvate come impronta, login e token JWT.

| Quando | Cartella | Cosa |
|---|---|---|
| 11:50 | [`villa-orm/`](villa-orm/README.md) | **La villa con SQLAlchemy**: le rotte di ieri, con `db.get`, `add`, `commit`, `delete` |
| 15:55 | [`wonka/`](wonka/README.md) | **La fabbrica di cioccolato**: registrazione, login, biglietto d'oro, sale protette |

## Una volta sola: il materiale e il venv di oggi

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-09
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi il venv, come ieri. Oggi ci sono librerie nuove: `sqlalchemy` (l'ORM), `pwdlib` (le password), `pyjwt` (i biglietti), `python-dotenv` (il file `.env`).

```bash
python3 --version            # deve dire 3.12 o più
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

La prova: `cd villa-orm` e poi `fastapi dev main.py`. Aprite **http://127.0.0.1:8000/docs** e provate `GET /ospiti`: arrivano gli ospiti della villa? Nel terminale del server vedete il SQL scritto da SQLAlchemy? Siete pronti.

Ogni volta che aprite un terminale nuovo, il venv va riacceso: `cd ~/corso-coding-arkemis/giorno-09` e `source .venv/bin/activate`.

## Postman

Serve l'**app desktop** (non la versione nel browser: dal browser Postman non raggiunge `127.0.0.1`), con un account gratuito. Scaricatela da **postman.com/downloads**. Su Windows installatela su Windows, non dentro Ubuntu: l'API accesa in WSL risponde lo stesso su `127.0.0.1:8000`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `python3 --version` dice meno di 3.12 | `rm -rf .venv`, poi `python3.12 -m venv .venv`, di nuovo `source` e `pip install` |
| `command not found: fastapi` oppure `No module named …` | Il venv è spento: `source .venv/bin/activate` dalla cartella `giorno-09` |
| `No module named 'sqlalchemy'` | Siete nel venv di ieri: questo è quello di `giorno-09`. `cd ~/corso-coding-arkemis/giorno-09`, `source .venv/bin/activate`, `pip install -r requirements.txt` |
| `Address already in use` | C'è già un server acceso in un altro terminale. Spegnetelo con Ctrl+C, oppure: `fastapi dev main.py --port 8001` |
| `connection failed` / `Connection refused` | PostgreSQL è spento. WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| `connection failed … No such file or directory` (il socket) | WSL: `export PGHOST=/var/run/postgresql` · Mac: `export PGHOST=/tmp`. Poi riaccendete il server |
| Postman: `Could not send request` / `ECONNREFUSED` | Il server è spento, oppure state usando Postman nel browser: serve l'app desktop |
