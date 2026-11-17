"""VILLA DUMARAIS · i dati della sicurezza, copiati dal vostro informatore.

QUESTO FILE NON SI TOCCA. Si legge, però: qui ci sono gli stampi (le classi)
e i dati (gli oggetti fatti con gli stampi).

Ogni dizionario va da un id a un oggetto:
    stanze[4]           -> l'oggetto Stanza con id 4
    stanze[4].nome      -> "Biblioteca"
    stanze[4].segreta   -> False
"""
from typing import Literal

from pydantic import BaseModel, Field


# ------------------------------------------------------------ gli stampi
class Stanza(BaseModel):
    id: int
    nome: str
    piano: int            # 0 = piano terra, 1 = primo piano, -1 = sotto terra
    segreta: bool = False  # le stanze segrete non sono sulla piantina degli ospiti


class Telecamera(BaseModel):
    id: int
    stanza_id: int        # in quale stanza è montata
    modello: str
    accesa: bool


class GuardiaNuova(BaseModel):
    """Una guardia, senza id: è quello che si manda con la PUT."""
    nome: str = Field(min_length=1)
    stanza_id: int        # davanti a quale stanza sta
    turno: Literal["sera", "notte"]
    anni_servizio: int = Field(ge=0)


class Guardia(GuardiaNuova):
    """Una guardia, con l'id: è quello che il server restituisce."""
    id: int


class GuardiaModifica(BaseModel):
    """BONUS (PATCH): tutti i campi sono facoltativi, si manda solo quello che cambia."""
    nome: str | None = None
    stanza_id: int | None = None
    turno: Literal["sera", "notte"] | None = None
    anni_servizio: int | None = Field(default=None, ge=0)


class OspiteNuovo(BaseModel):
    """Un ospite, senza id: è quello che si manda con la POST."""
    nome: str = Field(min_length=1)
    professione: str = Field(min_length=1)


class Ospite(OspiteNuovo):
    """Un ospite, con l'id."""
    id: int


# ------------------------------------------------------------ i dati
stanze: dict[int, Stanza] = {}
telecamere: dict[int, Telecamera] = {}
guardie: dict[int, Guardia] = {}
ospiti: dict[int, Ospite] = {}


def prossimo_id(dizionario: dict) -> int:
    """L'id da dare al prossimo oggetto: il più grande che c'è, più uno."""
    return max(dizionario, default=0) + 1


def ricarica() -> None:
    """Rimette la villa com'era all'inizio della serata (la usano i test)."""
    stanze.clear()
    for id, nome, piano, segreta in [
        (1, "Ingresso", 0, False),
        (2, "Salone delle feste", 0, False),
        (3, "Caveau", -1, True),
        (4, "Biblioteca", 1, False),
        (5, "Studio di Gaston Dumarais", 1, False),
        (6, "Galleria dei ritratti", 1, False),
        (7, "Giardino d'inverno", 0, False),
        (8, "Cucine", -1, False),
        (9, "Cantina dei vini", -1, False),
        (10, "Passaggio dietro la libreria", 1, True),
    ]:
        stanze[id] = Stanza(id=id, nome=nome, piano=piano, segreta=segreta)

    telecamere.clear()
    for id, stanza_id, modello, accesa in [
        (1, 1, "Argus 2", True),
        (2, 1, "Argus 2", True),
        (3, 2, "Vigil HD", True),
        (4, 3, "Argus 3", True),
        (5, 6, "Vigil HD", True),
        (6, 6, "Argus 2", False),
        (7, 3, "Argus 3", False),
        (8, 5, "Vigil HD", True),
        (9, 3, "Argus 3", True),
        (10, 7, "Argus 2", False),
        (11, 8, "Argus 2", True),
        (12, 3, "Argus 3", False),
        (13, 3, "Vigil HD", True),
        (14, 4, "Argus 2", True),
    ]:
        telecamere[id] = Telecamera(id=id, stanza_id=stanza_id, modello=modello, accesa=accesa)

    guardie.clear()
    for id, nome, stanza_id, turno, anni in [
        (1, "Mathis Lefèvre", 1, "sera", 12),
        (2, "Claire Dubois", 2, "sera", 3),
        (3, "Karim Haddad", 3, "notte", 20),
        (4, "Léa Martin", 6, "notte", 5),
        (5, "Gabriel Roux", 3, "notte", 7),
        (6, "Inès Fontaine", 5, "sera", 9),
        (7, "Hugo Bernard", 9, "notte", 1),
        (8, "Chloé Garnier", 1, "notte", 15),
        (9, "Antoine Mercier", 7, "sera", 4),
    ]:
        guardie[id] = Guardia(id=id, nome=nome, stanza_id=stanza_id, turno=turno, anni_servizio=anni)

    ospiti.clear()
    for id, nome, professione in [
        (1, "Gaston Dumarais", "padrone di casa"),
        (2, "Hélène Dumarais", "padrona di casa"),
        (3, "Mathilde Dumarais", "figlia dei padroni di casa"),
        (4, "Isabelle Moreau", "gallerista"),
        (5, "Contessa di Cagliostro", "collezionista di gioielli"),
        (6, "Victor Hautefeuille", "notaio"),
        (7, "Sophie Lenoir", "giornalista"),
        (8, "Ispettore Ganimard", "polizia"),
    ]:
        ospiti[id] = Ospite(id=id, nome=nome, professione=professione)


ricarica()
