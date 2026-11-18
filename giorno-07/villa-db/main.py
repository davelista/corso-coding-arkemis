"""LA VILLA NEL DATABASE · le stesse rotte del colpo, ma i dati stanno nel database villa.

Avvio (dalla cartella villa-db, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_1

Si tocca SOLO questo file.
"""
from typing import Literal

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

from database import connetti

app = FastAPI(title="La villa, su PostgreSQL")


# Gli stampi: gli stessi di colpo/villa.py
class OspiteNuovo(BaseModel):
    nome: str = Field(min_length=1)
    professione: str = Field(min_length=1)


class Ospite(OspiteNuovo):
    id: int


class GuardiaNuova(BaseModel):
    nome: str = Field(min_length=1)
    stanza_id: int
    turno: Literal["sera", "notte"]
    anni_servizio: int = Field(ge=0)


class Guardia(GuardiaNuova):
    id: int


# ============================================================ L'ESEMPIO (già fatto)
@app.get("/ospiti")
def lista_ospiti() -> list[Ospite]:
    with connetti() as conn:
        righe = conn.execute("SELECT * FROM ospiti ORDER BY id").fetchall()
    # righe è una lista di dizionari. FastAPI li controlla con lo stampo Ospite e li manda come JSON.
    return righe


# ============================================================ LIVELLO 1 · SELECT con WHERE
# GET /ospiti/{ospite_id} -> 200 e l'ospite, oppure 404 "Ospite non trovato"
#
# La query ha un buco, %s, e il valore si passa a parte, in una tupla:
#     conn.execute("SELECT * FROM ospiti WHERE id = %s", (ospite_id,))
# .fetchone() dà una riga sola (un dizionario), oppure None se non c'è.
# MAI la f-string dentro la query: f"... WHERE id = {ospite_id}" (vedi le slide: Bobby Tables).

@app.get("/ospiti/{ospite_id}")
def leggi_ospite(ospite_id: int) -> Ospite:
    # TODO: al posto di questa riga, il vostro codice.
    with connetti() as conn:
        ospite = conn.execute("SELECT * FROM ospiti WHERE id = %s", (ospite_id,)).fetchone()
    if ospite is None:
        raise HTTPException(status_code=404, detail='Ospite non trovato')
    
    return ospite


# ============================================================ LIVELLO 2 · INSERT
# POST /ospiti, con il corpo di un OspiteNuovo -> 201 e l'ospite salvato, con l'id che gli dà il database
#
#     INSERT INTO ospiti (nome, professione)
#     VALUES (%s, %s)
#     RETURNING *
#
# RETURNING * fa restituire all'INSERT la riga appena creata: con .fetchone() la prendete.
# Due buchi, due valori nella tupla, nello stesso ordine: (dati.nome, dati.professione)



# ============================================================ LIVELLO 3 · DELETE
# DELETE /ospiti/{ospite_id} -> 204 senza corpo, oppure 404 "Ospite non trovato"
#
#     DELETE FROM ospiti WHERE id = %s RETURNING id
#
# Se l'ospite non c'era, RETURNING non restituisce niente: .fetchone() è None.



# ============================================================ LIVELLO 4 · UPDATE
# PUT /guardie/{guardia_id}, con il corpo di una GuardiaNuova -> 200 e la guardia aggiornata, oppure 404
# "Guardia non trovata"
#
#     UPDATE guardie
#     SET nome = %s, stanza_id = %s, turno = %s, anni_servizio = %s
#     WHERE id = %s
#     RETURNING *
#
# Cinque buchi: l'ultimo è l'id.



# ============================================================ EXTRA: nel README
