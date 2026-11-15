# Giorno 6 · HTTP e la prima API

Python e il database li sapete già. Oggi nasce il pezzo in mezzo: il server che riceve le richieste e risponde.

| Quando | Cartella | Cosa |
|---|---|---|
| 9:45 | questo README, poi [`primo-server/`](primo-server/main.py) | Installiamo FastAPI e accendiamo il primo server |
| 11:15 | [`pokedex/`](pokedex/README.md) | **Il Pokédex del professor Oak**: undici richieste HTTP a un'API vera, a squadre |
| 14:00 | [`oggetti/`](oggetti/nave.py) | Palestra: una nave come oggetto, dallo stampo al biscotto |
| 15:00 | [`flotta/`](flotta/README.md) | **L'API della flotta**: il CRUD delle navi dei Caraibi, con i test già scritti |
| 17:00 | [`progetto/`](progetto/ROTTE.md) | Dal canvas alle rotte: il contratto della vostra API |

## Una volta sola: prendere il materiale e installare FastAPI

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-06
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi il venv di oggi, come al giorno 3:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

L'ultimo comando scarica parecchio: ci vuole qualche minuto. Alla fine, la prova:

```bash
fastapi dev primo-server/main.py
```

Aprite nel browser **http://127.0.0.1:8000/docs**. Vedete la pagina dell'API? Siete pronti. Il server si spegne con **Ctrl+C**.

Ogni volta che aprite un terminale nuovo, il venv va riacceso: `cd ~/corso-coding-arkemis/giorno-06` e `source .venv/bin/activate`. Vedete `(.venv)` all'inizio della riga? È acceso.

## Il laboratorio della flotta: i branch

Come al giorno 2: uno per gruppo crea il branch e lo manda su GitHub, gli altri lo prendono.

```bash
# chi crea il branch (a, b, c… è la lettera del gruppo)
git switch -c flotta-a
git push -u origin flotta-a

# gli altri del gruppo
git pull
git switch flotta-a
```

A ogni test verde: `git pull`, poi `git add`, `git commit`, `git push`. Alla fine, una pull request verso `main`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `command not found: fastapi` oppure `No module named fastapi` | Il venv è spento: `source .venv/bin/activate` dalla cartella `giorno-06` |
| `externally-managed-environment` | State installando fuori dal venv: accendetelo, poi rifate `pip install` |
| `Address already in use` | C'è già un server acceso in un altro terminale. Spegnetelo con Ctrl+C, oppure: `fastapi dev main.py --port 8001` |
| La pagina `/docs` non si apre (Windows) | Il server deve essere acceso nel terminale di Ubuntu. L'indirizzo è `http://127.0.0.1:8000/docs`, nel browser di Windows |
| `ModuleNotFoundError: No module named 'main'` in pytest | Siete nella cartella sbagliata: `pytest` va lanciato dentro `flotta` |
| pokeapi.co non risponde | Provate dal browser. Se non si apre neanche lì, la vostra rete la blocca: lavorate dal computer di un compagno del gruppo |
