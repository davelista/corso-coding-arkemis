"""LA CASSAFORTE DI VILLA DUMARAIS · QUESTO FILE NON SI TOCCA.

È già collegata alla vostra API (in main.py c'è app.include_router).
Si prova da /docs: POST /cassaforte/apri, con il corpo
    {"combinazione": "1234"}

Prima di guardare la combinazione, la cassaforte controlla che il piano sia andato a buon fine:
la lista degli ospiti, le guardie davanti al caveau, le telecamere del caveau.
Se qualcosa non va, risponde 403 e vi dice cosa.
"""
import hashlib

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

import villa

router = APIRouter(tags=["cassaforte"])

# La combinazione non è scritta qui: c'è solo la sua «impronta».
IMPRONTA = "8d4d5f84282458002dd74b12fcc9749adecf0bdfc194cef7bc5f4540a2e3377d"


class Tentativo(BaseModel):
    combinazione: str


def _id_del_caveau() -> int:
    for stanza in villa.stanze.values():
        if stanza.nome == "Caveau":
            return stanza.id
    raise HTTPException(status_code=500, detail="Il caveau è sparito dalla villa")


@router.post("/cassaforte/apri")
def apri_cassaforte(tentativo: Tentativo) -> dict:
    caveau = _id_del_caveau()

    sulla_lista = [o for o in villa.ospiti.values() if o.nome.strip().lower() == "paul sernine"]
    if not sulla_lista:
        raise HTTPException(
            status_code=403,
            detail="Al cancello il maggiordomo cerca Paul Sernine sulla lista degli ospiti. Non c'è: Lupin resta fuori.",
        )

    davanti = [g.nome for g in villa.guardie.values() if g.stanza_id == caveau]
    if davanti:
        raise HTTPException(
            status_code=403,
            detail=f"Davanti al caveau c'è ancora qualcuno: {', '.join(davanti)}.",
        )

    accese = [str(t.id) for t in villa.telecamere.values() if t.stanza_id == caveau and t.accesa]
    if accese:
        raise HTTPException(
            status_code=403,
            detail=f"Nel caveau ci sono ancora telecamere accese (id {', '.join(accese)}).",
        )

    prova = hashlib.sha256(f"cassaforte-dumarais:{tentativo.combinazione.strip()}".encode()).hexdigest()
    if prova != IMPRONTA:
        raise HTTPException(status_code=403, detail="Clic. Clic. Niente: la combinazione è sbagliata.")

    return {
        "messaggio": "La porta del caveau si apre senza un rumore. La collana della Regina è vostra.",
        "biglietto": "Al suo posto resta solo un biglietto da visita: «Arsène Lupin».",
    }
