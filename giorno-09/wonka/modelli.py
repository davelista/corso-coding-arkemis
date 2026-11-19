"""Le tabelle della fabbrica, viste da Python. QUESTO FILE NON SI TOCCA: si legge."""
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class BambinoDB(Base):
    __tablename__ = "bambini"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)    # UNIQUE: due bambini con lo stesso username? No
    nome: Mapped[str]
    password_hash: Mapped[str]                            # l'impronta, mai la password


class SalaDB(Base):
    __tablename__ = "sale"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    descrizione: Mapped[str]
    ingrediente: Mapped[str]
