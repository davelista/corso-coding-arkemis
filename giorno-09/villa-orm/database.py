"""Il collegamento al database villa, con SQLAlchemy. QUESTO FILE NON SI TOCCA.

Tre cose, sempre le stesse in ogni progetto:

    engine   la strada verso il database (si apre una volta sola, all'avvio)
    Base     la madre di tutte le classi-tabella (in modelli.py)
    get_db   presta una sessione a ogni richiesta, poi la chiude

Da main.py si usa così, come parametro della rotta:

    def leggi_ospite(ospite_id: int, db: Session = Depends(get_db)) -> Ospite:
        ...
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# Il nome del database. I test usano villa_test, così non toccano i vostri dati.
NOME_DB = os.environ.get("VILLA_DB", "villa")

# postgresql   il database
# +psycopg     il driver: la libreria di ieri, che parla davvero con PostgreSQL
# :///         nessun computer scritto: questo computer, come ieri
# villa        il nome del database
#
# echo=True: nel terminale del server vedete il SQL che SQLAlchemy scrive per voi.
engine = create_engine(f"postgresql+psycopg:///{NOME_DB}", echo=True)


class Base(DeclarativeBase):
    """Ogni classe che eredita da Base diventa una tabella (vedi modelli.py)."""


def get_db():
    """Apre una sessione, la presta alla rotta (yield), e alla fine la chiude."""
    with Session(engine) as db:
        yield db
