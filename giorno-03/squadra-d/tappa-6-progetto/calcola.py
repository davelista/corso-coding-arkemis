"""HOGWARTS · Tappa 6 · Numero 2 · I totali per categoria

La storia:  Arrivano le spese lette dal compagno: le sommi per categoria (treno, dolci, pozioni…).

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_calcola.py -v     (tutto verde = finito)
"""


def totali_per_categoria(spese: list[dict]) -> dict[str, float]:
    """Somma gli importi per categoria.

    spese = [
        {"data": "2026-09-01", "persona": "Harry", "categoria": "treno", "importo": 24.5},
        {"data": "2026-09-01", "persona": "Ron", "categoria": "dolci", "importo": 18.0},
        {"data": "2026-12-20", "persona": "Ron", "categoria": "treno", "importo": 24.5},
    ]
    totali_per_categoria(spese)  ->  {"treno": 49.0, "dolci": 18.0}
    """
    pass  # al posto di pass: il vostro codice


# Questo blocco parte solo se lanciate il file: python calcola.py
if __name__ == "__main__":
    prova = [{"data": "2026-09-01", "persona": "Harry", "categoria": "treno", "importo": 24.5}]
    print(totali_per_categoria(prova))
