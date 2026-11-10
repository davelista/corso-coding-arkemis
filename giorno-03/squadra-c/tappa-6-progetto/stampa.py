"""HOGWARTS · Tappa 6 · Numero 3 · Il report di fine anno

La storia:  Arrivano i totali dal compagno: li trasformi nel testo del report, pronto da appendere in sala comune.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_stampa.py -v     (tutto verde = finito)
"""


def formatta_report(totali: dict[str, float]) -> str:
    """Prepara il testo del report: titolo, una riga per categoria in ordine alfabetico, totale.

    formatta_report({"treno": 49.0, "dolci": 51.5})  ->  il testo qui sotto, righe unite da "\n"

    SPESE DELL'ANNO A HOGWARTS
    dolci: 51.50
    treno: 49.00
    TOTALE: 100.50

    Restituisce il testo (return), non lo stampa: la print la fa report.py.
    """
    pass  # al posto di pass: il vostro codice


# Questo blocco parte solo se lanciate il file: python stampa.py
if __name__ == "__main__":
    print(formatta_report({"treno": 49.0, "dolci": 51.5}))
