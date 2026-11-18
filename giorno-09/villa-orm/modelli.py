"""Le tabelle della villa, viste da Python. QUESTO FILE NON SI TOCCA: si legge.

Una classe = una tabella. Un attributo = una colonna. Un oggetto = una riga.
Il nome finisce con DB per non confonderle con gli stampi di Pydantic in main.py:

    OspiteNuovo   (Pydantic)    il corpo che arriva, senza id
    Ospite        (Pydantic)    la risposta che parte, con l'id
    OspiteDB      (SQLAlchemy)  la riga nella tabella ospiti
"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class StanzaDB(Base):
    __tablename__ = "stanze"                               # il nome della tabella in PostgreSQL

    id: Mapped[int] = mapped_column(primary_key=True)      # id SERIAL PRIMARY KEY
    nome: Mapped[str]                                      # nome TEXT NOT NULL
    piano: Mapped[int]                                     # piano INTEGER NOT NULL
    segreta: Mapped[bool]                                  # segreta BOOLEAN NOT NULL


class TelecameraDB(Base):
    __tablename__ = "telecamere"

    id: Mapped[int] = mapped_column(primary_key=True)
    stanza_id: Mapped[int] = mapped_column(ForeignKey("stanze.id"))   # REFERENCES stanze(id)
    modello: Mapped[str]
    accesa: Mapped[bool]


class GuardiaDB(Base):
    __tablename__ = "guardie"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    stanza_id: Mapped[int] = mapped_column(ForeignKey("stanze.id"))
    turno: Mapped[str]
    anni_servizio: Mapped[int]


class OspiteDB(Base):
    __tablename__ = "ospiti"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    professione: Mapped[str]
