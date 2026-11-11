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
    with open(percorso) as file:
        righe = file.read().splitlines()

    mosse_list = []
    chiavi = righe[0].split(",")
    for riga in righe[1:]:
        mossa = {}
        if not riga.strip():
            continue
        riga_mossa = riga.split(",")        
        riga_mossa[0] = int(riga_mossa[0])
        # print(f"colonne: {enumerate(riga_mossa)}")
        # print(f"chiavi {chiavi}")
        for i,valore in enumerate(riga_mossa):
            # print(chiavi[i], valore)
            mossa[chiavi[i]] = valore    
        mosse_list.append(mossa)
        # print(mosse_list)

    return mosse_list
        


# Questo blocco parte solo se lanciate il file: python leggi.py
if __name__ == "__main__":
    print(leggi_mosse("duello.csv"))
