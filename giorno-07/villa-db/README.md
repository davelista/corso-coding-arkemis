# La villa, su PostgreSQL

Stanotte, alla villa, è bastato salvare `main.py`: il server si è riavviato e Paul Sernine è sparito dalla lista. **Un dizionario vive finché il programma è acceso.**

Il database invece resta. Oggi la villa passa nel database `villa`: le stesse stanze, guardie, telecamere e ospiti del colpo, in quattro tabelle. Gli stampi (`OspiteNuovo`, `Ospite`, `GuardiaNuova`, `Guardia`) restano identici: cambia solo **dove** stanno i dati. Le query sono quelle di venerdì, su tabelle nuove.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `database.py` | Il collegamento al database: la funzione `connetti()` | No, si legge |
| `main.py` | L'API: `GET /ospiti` già fatta, poi un livello alla volta | **Sì, solo questo** |
| `test_main.py` | I test, sul database `villa_test` | No |
| `villa.sql` | Le tabelle e i dati della villa: serve per creare `villa`, e ai test per rifare `villa_test` da capo | No |

## Una volta sola

Dalla cartella `giorno-07`, con il venv acceso:

```bash
cd villa-db
createdb villa
psql -d villa -f villa.sql
createdb villa_test
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

Se `createdb` risponde «already exists», va bene. Su `/docs` provate `GET /ospiti`: gli otto ospiti arrivano **dal database**.

In un secondo terminale, con il venv acceso, dentro `villa-db`: `pytest -v -k livello_1`.

## Il modo di lavorare con il database

Ogni rotta fa sempre le stesse tre cose:

```python
with connetti() as conn:                                         # 1. apro
    riga = conn.execute("SELECT * FROM ospiti WHERE id = %s",    # 2. chiedo
                        (ospite_id,)).fetchone()
                                                                 # 3. il with chiude (e fa il COMMIT)
```

| Pezzo | Cosa fa |
|---|---|
| `conn.execute(query, valori)` | Manda la query al database |
| `%s` | Un buco nella query: il valore arriva a parte, nella tupla |
| `(ospite_id,)` | La tupla dei valori. Con un valore solo ci vuole la virgola |
| `.fetchall()` | Tutte le righe: una lista di dizionari |
| `.fetchone()` | Una riga sola: un dizionario, oppure `None` se non c'è |
| `RETURNING *` | Fa restituire a `INSERT`, `UPDATE` e `DELETE` le righe che hanno toccato |

**Mai la f-string dentro la query.** `f"SELECT * FROM ospiti WHERE id = {ospite_id}"` funziona, ed è proprio il problema: chiunque può scrivere un pezzo di SQL al posto dell'id. Con `%s` il database sa che lì c'è un valore, e basta.

## I livelli

| Livello | Rotta | La query | Risponde |
|---|---|---|---|
| 1 | `GET /ospiti/{ospite_id}` | `SELECT … WHERE id = %s` | 200, oppure 404 `"Ospite non trovato"` |
| 2 | `POST /ospiti` | `INSERT … RETURNING *` | 201 con l'ospite e il suo id |
| 3 | `DELETE /ospiti/{ospite_id}` | `DELETE … WHERE id = %s RETURNING id` | 204, oppure 404 |
| 4 | `PUT /guardie/{guardia_id}` | `UPDATE … SET … WHERE id = %s RETURNING *` | 200, oppure 404 `"Guardia non trovata"` |

**Oggi: il livello 1, e il 2 se c'è tempo.** Il 3 e il 4 sono per chi finisce prima: li riprendiamo insieme.

In `main.py`, sopra ogni livello, c'è la query già scritta: il lavoro è metterla nella rotta giusta, con i valori giusti, e gestire il caso in cui la riga non c'è.

Dopo il livello 2, **la prova del nove**: mettete Paul Sernine in lista da `/docs`, spegnete il server (Ctrl+C), riaccendetelo e richiedete `GET /ospiti`. Paul Sernine c'è ancora? Potete controllare anche da `psql -d villa`: `SELECT * FROM ospiti;`.

## Se finite prima · extra

1. **Chi c'è davanti a una stanza:** `GET /stanze/{stanza_id}/guardie`, come il livello 4 del colpo, ma con un `WHERE stanza_id = %s`. 404 se la stanza non c'è.
2. **Il 409 del nome:** `POST /ospiti` con un nome già in lista. Il database dice di no (`UNIQUE`): in Python arriva come `psycopg.errors.UniqueViolation`. Prendetela con `try/except` e rispondete 409 `"Nome già in lista"`.
3. **La stanza che non c'è:** `PUT /guardie/3` con `stanza_id` 42. Il database dice di no (`REFERENCES`): `psycopg.errors.ForeignKeyViolation`. Rispondete 404 `"Stanza non trovata"`.

I test: `pytest -v -k extra`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `No module named psycopg` | Il venv è spento, oppure manca `pip install -r requirements.txt` nella cartella `giorno-07` |
| `connection failed` / `Connection refused` | PostgreSQL è spento. WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| `connection failed … No such file or directory` (il socket) | Ditegli dove cercare. WSL: `export PGHOST=/var/run/postgresql` · Mac: `export PGHOST=/tmp`. Poi riaccendete il server |
| `database "villa_test" does not exist` | `createdb villa_test` |
| `database "villa" does not exist` | `createdb villa`, poi `psql -d villa -f villa.sql` |
| `relation "ospiti" does not exist` | Il database c'è ma è vuoto: `psql -d villa -f villa.sql` |
| `501` nei test | Non avete ancora tolto la riga del «da fare» |
| `500 Internal Server Error` | Guardate il terminale dove gira il server: l'errore vero è lì, di solito nella query |
| `the query has 5 placeholders but 4 parameters were passed` | I `%s` e i valori nella tupla devono essere tanti quanti, e nello stesso ordine |
