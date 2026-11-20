# Insieme, dal vivo · password, biglietto, controllore

Stamattina, dalle 11:30, le funzioni di sicurezza di Wonka le costruiamo **da zero, insieme**: io scrivo a schermo condiviso, voi scrivete con me in questi tre file. Si va avanti quando gira a tutti.

| File | Cosa costruiamo | In Wonka diventa | Si prova con |
|---|---|---|---|
| `password.py` | L'impronta, il sale, il controllo | `calcola_hash`, `password_giusta` | `python3 password.py` |
| `biglietto.py` | Il JWT: crearlo, leggerlo, falsificarlo | `crea_biglietto` | `python3 biglietto.py` |
| `main.py` | Il controllore, dalla chiave al biglietto | `bambino_corrente` | `fastapi dev main.py`, poi Postman |

Prima di partire, con il venv di `giorno-10` acceso:

```bash
cd ~/corso-coding-arkemis/giorno-10/insieme
```

## La prova finale, in Postman

1. `python3 biglietto.py`: copiate la prima riga stampata (il biglietto).
2. In un altro terminale, sempre in `insieme`: `fastapi dev main.py`.
3. `GET http://127.0.0.1:8000/saluto` → **Authorization** → **Bearer Token** → incollate il biglietto: «Ciao, Charlie!».
4. **No Auth**: 401 «Manca il biglietto». Una lettera cambiata nel biglietto: 401 «Biglietto non valido».

Il biglietto dura 30 minuti: dopo, rilanciate `python3 biglietto.py`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `No module named 'jwt'` | Il venv è spento: `source ../.venv/bin/activate` |
| `ValueError: not enough values to unpack` in `password_giusta` | La stringa salvata non ha il `$` in mezzo: controllate il `return f"{sale}${impronta}"` |
| `ImportError: cannot import name 'SECRET_KEY'` | In `biglietto.py` manca `SECRET_KEY`, oppure state lanciando `main.py` da un'altra cartella |
| `/saluto` risponde 401 con il biglietto giusto | Copiato con le virgolette o con uno spazio? Oppure è scaduto: rilanciate `python3 biglietto.py` |
