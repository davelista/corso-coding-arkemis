"""Il collegamento al database agrabah, con SQLAlchemy. QUESTO FILE NON SI TOCCA.

È lo stesso della villa e della fabbrica: cambia solo il nome del database.
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session

# Il nome del database. I test usano agrabah_test, così non toccano i vostri dati.
NOME_DB = os.environ.get("AGRABAH_DB", "agrabah")

engine = create_engine(f"postgresql+psycopg:///{NOME_DB}", echo=True)


class Base(DeclarativeBase):
    """Ogni classe che eredita da Base diventa una tabella (vedi modelli.py)."""


def get_db():
    """Apre una sessione, la presta alla rotta (yield), e alla fine la chiude."""
    with Session(engine) as db:
        yield db
