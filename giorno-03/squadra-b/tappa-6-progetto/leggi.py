"""HOGWARTS · Tappa 6 · Numero 1 · Le mosse del duello

La storia:  Le mosse di Harry e Draco sono scritte in duello.csv. Il tuo pezzo le legge e le passa ai compagni.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_leggi.py -v     (tutto verde = finito)
"""



def leggi_mosse(percorso: str) -> list[dict]:
    """Legge il CSV del duello e restituisce una lista di mosse, una per riga.

    - La prima riga è l'intestazione (turno,mago,bersaglio,incantesimo): si salta.
    - Le righe vuote si saltano.
    - Il turno diventa un int.

    Ogni mossa è un dizionario fatto così:
    {"turno": 1, "mago": "Draco", "bersaglio": "Harry", "incantesimo": "stupeficium"}
    """
    duello = open(percorso).read().splitlines()
    mosse = []

    for riga in duello[1:]:
        colonne = riga.split(",")

        mossa = {
            "turno" : int(colonne[0]),
            "mago" : colonne[1],
            "bersaglio" : colonne[2],
            "incantesimo" : colonne[3]
        }
        
        mosse.append(mossa)
    return mosse

    
    

# Questo blocco parte solo se lanciate il file: python leggi.py
if __name__ == "__main__":
    print(leggi_mosse("duello.csv"))
