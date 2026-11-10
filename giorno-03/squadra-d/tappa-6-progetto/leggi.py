"""HOGWARTS · Tappa 6 · Numero 1 · Leggere il registro delle spese

La storia:  Tutte le spese dell'anno sono in spese.csv. Il tuo pezzo le legge e le passa al compagno.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_leggi.py -v     (tutto verde = finito)
"""


def leggi_spese(percorso: str) -> list[dict]:
    """Legge il CSV delle spese e restituisce una lista di dizionari, uno per riga.

    - La prima riga è l'intestazione (data,persona,categoria,importo): si salta.
    - Le righe vuote si saltano.
    - L'importo diventa un float.

    Ogni dizionario è fatto così:
    {"data": "2026-09-01", "persona": "Harry", "categoria": "treno", "importo": 24.5}
    """
    pass  # al posto di pass: il vostro codice


# Questo blocco parte solo se lanciate il file: python leggi.py
if __name__ == "__main__":
    print(leggi_spese("spese.csv"))
