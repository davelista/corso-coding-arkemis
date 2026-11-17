"""LA TALPA · qualcuno nella banda ha sabotato il conto del bottino.

Il programma non dà nessun errore: risponde sempre 200. Ma i numeri sono sbagliati.
Tre bug silenziosi, uno per rotta. Si trovano con il debugger, non a occhio.

Avvio con il debugger: vedi DEBUG.md (configurazione «La talpa»), poi F5.
Test:  pytest -v
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="La talpa")


class Pezzo(BaseModel):
    id: int
    nome: str
    valore: int     # in franchi
    stanza: str


refurtiva = [
    Pezzo(id=1, nome="Collana della Regina", valore=500000, stanza="Caveau"),
    Pezzo(id=2, nome="Spilla di smeraldi", valore=42000, stanza="Studio"),
    Pezzo(id=3, nome="Orologio d'oro", valore=8000, stanza="Studio"),
    Pezzo(id=4, nome="Quadro fiammingo", valore=120000, stanza="Galleria"),
    Pezzo(id=5, nome="Tabacchiera d'argento", valore=3000, stanza="Salone"),
]

# La parte di ognuno, in percentuale
quote = {"Lupin": 30, "Grognard": 25, "Victoire": 25, "Le Ballu": 20}


@app.get("/bottino/totale")
def totale() -> dict:
    somma = 0
    for i in range(1, len(refurtiva)):
        somma = somma + refurtiva[i].valore
    return {"totale": somma}


@app.get("/bottino/quota/{nome}")
def quota(nome: str) -> dict:
    if nome not in quote:
        raise HTTPException(status_code=404, detail="Complice non trovato")
    tot = totale()["totale"]
    parte = tot * quote[nome] // 10
    return {"nome": nome, "parte": parte}


@app.get("/refurtiva")
def lista_refurtiva(stanza: str | None = None) -> list[Pezzo]:
    if stanza is None:
        return refurtiva
    risultato = []
    for pezzo in refurtiva:
        if pezzo.stanza == stanza:
            risultato = [pezzo]
    return risultato
