# Giorno 7 · Oggetti, il colpo e il database

Ieri l'API l'avete vista nascere. Oggi la scriviamo con calma, un gradino alla volta: prima gli oggetti e i dizionari, disegnati; poi un colpo alla villa Dumarais, tutto a richieste HTTP; poi la banda di Lupin, da soli; solo alla fine, il database.

| Quando | Cartella | Cosa |
|---|---|---|
| 9:35 | [`oggetti/`](oggetti/DISEGNI.md) | **Prevedi il disegno**: etichette, scatole, `self` ed ereditarietà, con Python Tutor |
| 11:35 | questo README, poi [`DEBUG.md`](DEBUG.md) | Il venv di oggi, poi **il debugger su FastAPI**: il `launch.json` lo scrivete voi |
| 11:55 | [`colpo/`](colpo/README.md) | **Il colpo**: l'API della villa Dumarais, sette livelli e una cassaforte |
| 15:25 | [`talpa/`](talpa/README.md) | **La talpa**: tre bug silenziosi, da trovare con il debugger |
| 15:55 | [`banda/`](banda/README.md) | **La banda, da soli**: POST, PUT e DELETE, adesso che avete tutti gli strumenti |
| 16:45 | [`villa-db/`](villa-db/README.md) | **La villa su PostgreSQL**: le rotte del colpo, con le query di venerdì |

## Una volta sola: il materiale e il venv di oggi

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-07
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi il venv, come ieri. Oggi c'è una libreria in più, `psycopg`: serve a Python per parlare con PostgreSQL.

```bash
python3 --version            # deve dire 3.12 o più
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

La prova: `cd colpo` e poi `fastapi dev main.py`. Aprite **http://127.0.0.1:8000/docs**: vedete l'API della villa? Siete pronti.

Ogni volta che aprite un terminale nuovo, il venv va riacceso: `cd ~/corso-coding-arkemis/giorno-07` e `source .venv/bin/activate`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `python3 --version` dice meno di 3.12 | Il venv nasce con la versione sbagliata. Cancellatelo e rifatelo con quella giusta: `rm -rf .venv`, poi `python3.12 -m venv .venv` e di nuovo `source` e `pip install` |
| `command not found: fastapi` oppure `No module named …` | Il venv è spento: `source .venv/bin/activate` dalla cartella `giorno-07` |
| `externally-managed-environment` | State installando fuori dal venv: accendetelo, poi rifate `pip install` |
| `Address already in use` | C'è già un server acceso in un altro terminale (magari quello di ieri). Spegnetelo con Ctrl+C, oppure: `fastapi dev main.py --port 8001` |
| La pagina `/docs` non si apre (Windows) | Il server deve essere acceso nel terminale di Ubuntu. L'indirizzo è `http://127.0.0.1:8000/docs`, nel browser di Windows |
| `ModuleNotFoundError: No module named 'main'` in pytest | Siete nella cartella sbagliata: `pytest` va lanciato dentro `colpo`, `talpa`, `banda` o `villa-db` |
