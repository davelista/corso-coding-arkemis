"""Le tabelle di Agrabah, viste da Python.

TesoroDB è già scritto: è l'esempio. Le altre due le scrivete voi, guardando agrabah.sql:

    PadroneDB      la tabella padroni      serve dal livello 3
    DesiderioDB    la tabella desideri     serve dal livello 5
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class TesoroDB(Base):
    __tablename__ = "tesori"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    valore: Mapped[int]
    maledetto: Mapped[bool] = mapped_column(default=False)    # se non lo dite voi, vale False


# ============================================================ LIVELLO 3 · PadroneDB
# La tabella padroni: guardate le colonne in agrabah.sql, e scrivetele come in TesoroDB.
# - username è UNIQUE: mapped_column(unique=True)
# - la colonna ruolo serve solo al livello 6: per ora potete lasciarla fuori.

class PadroneDB(Base):
    __tablename__ = "padroni"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    nome: Mapped[str]
    password_hash: Mapped[str]
    ruolo: Mapped[str] = mapped_column(default="padrone")

# ============================================================ LIVELLO 5 · DesiderioDB
# La tabella desideri.
# - esaudito parte da False: mapped_column(default=False), come maledetto qui sopra
# - padrone_id dice di chi è il desiderio: è un numero intero, Mapped[int].
#   La chiave esterna c'è già nel database: qui non serve altro.

class DesiderioDB(Base):
    __tablename__ = "desideri"

    id: Mapped[int] = mapped_column(primary_key=True)
    testo: Mapped[str]
    esaudito: Mapped[bool] = mapped_column(default=False)
    padrone_id: Mapped[int] = mapped_column(ForeignKey("padroni.id"))