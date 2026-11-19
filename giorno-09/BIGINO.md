# Il bigino di SQLAlchemy

Tutto quello che serve oggi, in una pagina. Gli esempi sono sulla villa (`villa-orm`).

## Le parole

| Parola | Cosa vuol dire |
|---|---|
| **ORM** | Object Relational Mapping: le tabelle viste come classi, le righe come oggetti |
| **modello** | Una classe che è una tabella: `OspiteDB`, in `modelli.py` |
| **`Mapped[str]`** | «Questo attributo è una colonna, e contiene un testo». `int` → INTEGER, `bool` → BOOLEAN |
| **`mapped_column(...)`** | Serve solo se c'è altro da dire: `primary_key=True`, `ForeignKey("stanze.id")`, `unique=True` |
| **engine** | La strada verso il database. Si apre una volta sola, all'avvio (`database.py`) |
| **sessione** (`db`) | La conversazione con il database durante una richiesta. Ricorda cosa leggete, aggiungete, cambiate, togliete. Con `commit` manda tutto |
| **`get_db`** | Apre una sessione, la presta alla rotta, poi la chiude |
| **`from_attributes=True`** | Nello stampo di Pydantic: «puoi riempirmi leggendo un oggetto (`ospite.nome`), non solo un dizionario» |

## Le importazioni

```python
from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_db
from modelli import OspiteDB
```

## In ogni rotta che usa il database

```python
def leggi_ospite(ospite_id: int, db: Session = Depends(get_db)) -> Ospite:
```

## Leggere

```python
db.get(OspiteDB, 4)                                   # uno, per id: l'oggetto, oppure None
db.scalars(select(OspiteDB)).all()                    # tutti: una lista, anche vuota
db.scalars(select(OspiteDB).order_by(OspiteDB.id)).all()           # tutti, in ordine
db.scalars(select(OspiteDB)
           .where(OspiteDB.professione == "notaio")).all()        # solo quelli del filtro
db.scalar(select(OspiteDB).where(OspiteDB.nome == "Sophie Lenoir"))  # uno, per un altro campo (o None)
```

Dentro `select(...)` va la classe della tabella (`OspiteDB`), mai lo stampo (`Ospite`).

## Scrivere: prima si prepara, poi si consegna

```python
ospite = OspiteDB(nome="Paul Sernine", professione="collezionista")   # l'oggetto nuovo: id ancora None
db.add(ospite)              # una riga nuova, nel carrello
guardia.stanza_id = 9       # cambiare: basta l'attributo (la guardia l'avete presa con db.get)
db.delete(ospite)           # togliere, nel carrello

db.commit()                 # consegna: INSERT, UPDATE, DELETE, tutti insieme
db.refresh(ospite)          # rilegge dal database: per esempio l'id appena scelto
db.rollback()               # svuota il carrello, dopo un errore (per esempio IntegrityError)
```

**Senza `db.commit()` non resta niente**: a fine richiesta la sessione si chiude e il carrello si svuota.

## Ieri e oggi

| Cosa volete | Ieri, con psycopg | Oggi, con SQLAlchemy |
|---|---|---|
| Tutte le righe | `SELECT * FROM ospiti` + `.fetchall()` | `db.scalars(select(OspiteDB)).all()` |
| Una riga, per id | `… WHERE id = %s` + `.fetchone()` | `db.get(OspiteDB, ospite_id)` |
| Una riga, per un altro campo | `… WHERE nome = %s` + `.fetchone()` | `db.scalar(select(OspiteDB).where(OspiteDB.nome == nome))` |
| Una riga nuova | `INSERT … RETURNING *` | `db.add(ospite)`, `db.commit()`, `db.refresh(ospite)` |
| Cambiare una riga | `UPDATE … SET …` | `guardia.nome = …`, `db.commit()` |
| Togliere una riga | `DELETE … WHERE id = %s` | `db.delete(ospite)`, `db.commit()` |
| Il commit | da solo, all'uscita dal `with` | lo scrivete voi: `db.commit()` |
| Cosa torna | dizionari | oggetti |

Il SQL che SQLAlchemy scrive per voi lo vedete nel terminale del server (`echo=True` in `database.py`).
