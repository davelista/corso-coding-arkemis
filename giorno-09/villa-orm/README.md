# La villa, con SQLAlchemy

Ieri, per leggere un ospite, scrivevate il SQL in una stringa:

```python
with connetti() as conn:
    riga = conn.execute("SELECT * FROM ospiti WHERE id = %s", (ospite_id,)).fetchone()
```

Oggi la stessa cosa si scrive così:

```python
ospite = db.get(OspiteDB, ospite_id)
```

Il SQL c'è ancora: lo scrive **SQLAlchemy**, e lo vedete nel terminale del server. Il database è lo stesso di ieri (`villa`), le rotte sono le stesse di ieri, i test sono gli stessi di ieri. Cambia solo **come** si parla con il database.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `database.py` | La strada verso il database (`engine`), la madre delle tabelle (`Base`), la sessione in prestito (`get_db`) | No, si legge |
| `modelli.py` | Le tabelle viste da Python: `StanzaDB`, `TelecameraDB`, `GuardiaDB`, `OspiteDB` | No, si legge |
| `main.py` | L'API: `GET /ospiti` già fatta, poi un livello alla volta | **Sì, solo questo** |
| `test_main.py` | I test, sul database `villa_test` | No |
| `villa.sql` | Le tabelle e i dati della villa: ai test serve per rifare `villa_test` da capo | No |

## Una volta sola

Il database `villa` c'è già da ieri. Oggi ne serve un secondo, **`villa_test`**, solo per i test: prima di ogni test lo rifanno da capo, così i vostri dati in `villa` non si toccano mai.

```bash
createdb villa_test
```

Se `villa` non c'è (o volete ripartire da capo), dalla cartella `villa-orm`:

```bash
createdb villa
psql -d villa -f villa.sql
```

Poi, con il venv di `giorno-09` acceso:

```bash
cd villa-orm
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

In un secondo terminale, con il venv acceso, dentro `villa-orm`: `pytest -v -k livello_1`.

## Le sei mosse

| Cosa volete | Ieri, con psycopg | Oggi, con SQLAlchemy |
|---|---|---|
| Tutte le righe | `SELECT * FROM ospiti` + `.fetchall()` | `db.scalars(select(OspiteDB)).all()` |
| Una riga, per id | `… WHERE id = %s` + `.fetchone()` | `db.get(OspiteDB, ospite_id)` |
| Una riga, per un altro campo | `… WHERE nome = %s` + `.fetchone()` | `db.scalar(select(OspiteDB).where(OspiteDB.nome == nome))` |
| Una riga nuova | `INSERT … RETURNING *` | `db.add(ospite)`, `db.commit()`, `db.refresh(ospite)` |
| Cambiare una riga | `UPDATE … SET …` | `guardia.nome = …`, poi `db.commit()` |
| Togliere una riga | `DELETE … WHERE id = %s` | `db.delete(ospite)`, poi `db.commit()` |

**Senza `db.commit()` non resta niente.** La sessione è un carrello: `add` e `delete` mettono nel carrello, `commit` consegna al database.

## I livelli

| Livello | Rotta | Le mosse | Risponde |
|---|---|---|---|
| 1 · **insieme** | `GET /ospiti/{ospite_id}` | `db.get` | 200, oppure 404 `"Ospite non trovato"` |
| 2 | `POST /ospiti` | `add`, `commit`, `refresh` | 201 con l'ospite e il suo id |
| 3 | `DELETE /ospiti/{ospite_id}` | `db.get`, `delete`, `commit` | 204, oppure 404 |
| 4 | `PUT /guardie/{guardia_id}` | `db.get`, quattro attributi, `commit` | 200, oppure 404 `"Guardia non trovata"` |

**Oggi: il livello 1 insieme, poi il 2 e il 3 da soli. Il 4 se c'è tempo.**

Ogni livello finisce così:

1. `pytest -v -k livello_N`: verde?
2. La stessa richiesta **in Postman**, salvata nella collezione «Giorno 09» (Ctrl+S, oppure Cmd+S su Mac).
3. Guardate il terminale del server: qual è il SQL che ha scritto SQLAlchemy?

<details>
<summary>Aiutino del livello 2</summary>

```python
@app.post("/ospiti", status_code=status.HTTP_201_CREATED)
def nuovo_ospite(dati: OspiteNuovo, db: Session = Depends(get_db)) -> Ospite:
    ospite = OspiteDB(nome=..., professione=...)
    # nel carrello, consegna, rileggi
    return ospite
```

</details>

<details>
<summary>Aiutino del livello 3</summary>

Le prime tre righe sono quelle del livello 1. Poi due mosse: `db.delete(ospite)` e `db.commit()`. Nessun `return`.

</details>

<details>
<summary>Aiutino del livello 4</summary>

Come il livello 1, ma con `GuardiaDB`. Poi un attributo per riga: `guardia.nome = dati.nome`, e così per `stanza_id`, `turno` e `anni_servizio`. Poi `db.commit()` e `return guardia`.

</details>

## Se finite prima · extra

1. **Chi c'è davanti a una stanza:** `GET /stanze/{stanza_id}/guardie`. Prima `db.get(StanzaDB, stanza_id)` per il 404 `"Stanza non trovata"`, poi `select(GuardiaDB).where(GuardiaDB.stanza_id == stanza_id)` e `db.scalars(…).all()`.
2. **Il 409 del nome:** `POST /ospiti` con un nome già in lista. Il database dice di no (`UNIQUE`), e in Python arriva al `db.commit()` come `IntegrityError` (da `sqlalchemy.exc`). Prendetela con `try/except`, fate `db.rollback()` e rispondete 409 `"Nome già in lista"`.
3. **La stanza che non c'è:** `PUT /guardie/3` con `stanza_id` 42 → 404 `"Stanza non trovata"`. Controllate con `db.get(StanzaDB, dati.stanza_id)` prima di cambiare la guardia.

I test: `pytest -v -k extra`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `501` nei test | Non avete ancora tolto la riga del «da fare» |
| La riga non è nel database (il test lo dice) | Manca `db.commit()` |
| Il server non parte: `Invalid args for response field` | Nel `->` della rotta c'è `OspiteDB` (la tabella): deve esserci lo stampo `Ospite` |
| `TypeError: … unexpected keyword argument` | State costruendo `OspiteDB(...)` con un nome di campo sbagliato: guardate `modelli.py` |
| `AttributeError: 'NoneType' object has no attribute …` | `db.get` ha restituito `None` e siete andati avanti: manca l'`if … is None` con il 404 |
| `ArgumentError` su `select(...)` | Dentro `select` va la classe del database, `OspiteDB`, non lo stampo `Ospite` |
| `500 Internal Server Error` | Guardate il terminale dove gira il server: l'errore vero è lì, sopra c'è il SQL che SQLAlchemy ha provato |
