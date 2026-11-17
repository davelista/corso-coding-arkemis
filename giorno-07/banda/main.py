"""LA BANDA · il registro dei complici di Lupin, in un dizionario.

Avvio (dalla cartella banda, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test (in un secondo terminale):
    pytest -v

Si tocca SOLO questo file, dalla riga «TOCCA A VOI» in giù.
"""
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="La banda di Lupin")


class CompliceNuovo(BaseModel):
    """Quello che il client manda: tutto tranne l'id."""
    nome: str = Field(min_length=1)
    specialita: str = Field(min_length=1)
    quota: int = Field(ge=0, le=100)   # la sua parte del bottino, in percentuale


class Complice(CompliceNuovo):
    """Quello che il server restituisce: con l'id."""
    id: int


# Il registro: un dizionario da id a complice.
banda: dict[int, Complice] = {}


def prossimo_id() -> int:
    return max(banda, default=0) + 1


def ricarica() -> None:
    """Rimette la banda com'era (la usano i test)."""
    banda.clear()
    for id, nome, specialita, quota in [
        (1, "Grognard", "scasso", 25),
        (2, "Victoire", "informazioni", 25),
        (3, "Le Ballu", "fuga", 20),
    ]:
        banda[id] = Complice(id=id, nome=nome, specialita=specialita, quota=quota)


ricarica()


# ============================================================ GLI ESEMPI (già fatti)
@app.get("/complici")
def lista_complici() -> list[Complice]:
    return list(banda.values())


@app.get("/complici/{complice_id}")
def leggi_complice(complice_id: int) -> Complice:
    complice = banda.get(complice_id)
    if complice is None:
        raise HTTPException(status_code=404, detail="Complice non trovato")
    return complice


# ============================================================ TOCCA A VOI
# 1 · POST /complici, con il corpo di un CompliceNuovo
#       -> 201 e il nuovo complice, con l'id: prossimo_id()
#
# 2 · PUT /complici/{complice_id}, con il corpo di un CompliceNuovo
#       -> 200 e il complice aggiornato (stesso id)
#       -> 404 "Complice non trovato" se l'id non c'è
#
# 3 · DELETE /complici/{complice_id}
#       -> 204 senza corpo
#       -> 404 "Complice non trovato" se l'id non c'è
