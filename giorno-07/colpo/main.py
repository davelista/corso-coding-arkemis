"""IL COLPO · l'API della banda per la villa Dumarais.

Avvio (dalla cartella colpo, con il venv acceso):
    fastapi dev main.py          poi aprite http://127.0.0.1:8000/docs
Test di un livello (in un secondo terminale):
    pytest -v -k livello_1

Si tocca SOLO questo file. villa.py e cassaforte.py si leggono, ma non si cambiano.
"""
from fastapi import FastAPI, HTTPException, status

import cassaforte
from villa import (
    Guardia, GuardiaModifica, GuardiaNuova, Ospite, OspiteNuovo, Stanza, Telecamera,
    guardie, ospiti, prossimo_id, stanze, telecamere,
)

app = FastAPI(title="Il colpo · villa Dumarais")
app.include_router(cassaforte.router)   # la cassaforte: POST /cassaforte/apri


@app.get("/")
def home():
    return {"messaggio": "Il piano è pronto. La banda vi aspetta su /docs"}


# ============================================================ GLI ESEMPI (già fatti)
# Leggeteli bene: ogni livello è una piccola variazione di uno di questi.

@app.get("/ospiti")
def lista_ospiti() -> list[Ospite]:
    # ospiti è un dizionario: id -> oggetto Ospite.
    # .values() prende solo gli oggetti, list(...) li mette in una lista.
    return list(ospiti.values())


@app.get("/ospiti/{ospite_id}")
def leggi_ospite(ospite_id: int) -> Ospite:
    # {ospite_id} nel percorso diventa l'argomento ospite_id:  GET /ospiti/4  ->  ospite_id = 4
    ospite = ospiti.get(ospite_id)    # .get risponde None se l'id non c'è (le [] darebbero errore)
    if ospite is None:
        raise HTTPException(status_code=404, detail="Ospite non trovato")
    return ospite


# ============================================================ LIVELLO 1 · GET, la lista
# GET /stanze -> 200 e la lista delle stanze, MA SENZA quelle segrete (stanza.segreta è True).
# È come lista_ospiti, con un if in più.

@app.get("/stanze")
def lista_stanze() -> list[Stanza]:
    visibili = []
    for stanza in stanze.values():
        # TODO: aggiungete la stanza a visibili solo se NON è segreta
        pass
    return visibili


# ============================================================ LIVELLO 2 · GET, uno solo
# GET /stanze/{stanza_id} -> 200 e la stanza (anche se è segreta!)
#                         -> 404 "Stanza non trovata" se l'id non c'è
# È come leggi_ospite.

@app.get("/stanze/{stanza_id}")
def leggi_stanza(stanza_id: int) -> Stanza:
    # TODO: al posto di questa riga, il vostro codice.
    # (501 = «non ancora fatto»: è un codice di stato vero, si usa proprio così)
    raise HTTPException(status_code=501, detail="Livello 2: ancora da fare")


# ============================================================ LIVELLO 3 · GET con un filtro
# GET /telecamere               -> 200 e tutte le telecamere
# GET /telecamere?stanza_id=4   -> 200 e solo quelle della stanza 4
# Il filtro è facoltativo: nella funzione è un argomento con il valore di partenza None.
# Questa volta scrivete voi anche il decoratore @app.get(...) e la riga del def.



# ============================================================ LIVELLO 4 · GET, chi c'è in una stanza
# GET /stanze/{stanza_id}/guardie -> 200 e le guardie che stanno davanti a quella stanza
#                                 -> 404 "Stanza non trovata" se la stanza non c'è
# Due cose che sapete già, insieme: il controllo del livello 2 e il filtro del livello 3.



# ============================================================ LIVELLO 5 · POST, crea
# POST /ospiti, con il corpo {"nome": "...", "professione": "..."}
#   -> 201 e il nuovo ospite, con il suo id (prossimo_id(ospiti) vi dà quello giusto)
# Il corpo arriva come OspiteNuovo (senza id). Voi create un Ospite (con l'id) e lo mettete in ospiti.
# Codice 201: @app.post("/ospiti", status_code=status.HTTP_201_CREATED)



# ============================================================ LIVELLO 6 · PUT, sostituisce
# PUT /guardie/{guardia_id}, con il corpo di una GuardiaNuova (tutti i campi, senza id)
#   -> 200 e la guardia aggiornata
#   -> 404 "Guardia non trovata" se l'id non c'è



# ============================================================ LIVELLO 7 · DELETE, cancella
# DELETE /telecamere/{telecamera_id}
#   -> 204 senza corpo: @app.delete("...", status_code=status.HTTP_204_NO_CONTENT)
#   -> 404 "Telecamera non trovata" se l'id non c'è
# Per togliere una chiave da un dizionario: del telecamere[telecamera_id]



# ============================================================ EXTRA e BONUS: nel README
