"""HOGWARTS · Tappa 1 · Numero 3 · La cassa del Ghirigoro

La storia:  Al Ghirigoro, la libreria di Diagon Alley, la cassa stampa una riga per ogni acquisto, in galeoni. La scrivete voi.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_riga_acquisto.py -v     (tutto verde = finito)
"""


def riga_acquisto(prodotto: str, prezzo: float, quantita: int) -> str:
    """Restituisce la riga dell'acquisto: prodotto in minuscolo, quantità e totale in galeoni con 2 decimali.

    riga_acquisto("piuma", 1.2, 3)       ->  "piuma x3: 3.60 galeoni"
    riga_acquisto("Pergamena", 2.5, 2)   ->  "pergamena x2: 5.00 galeoni"
    """
    pass  # al posto di pass: il vostro codice, che finisce con un return


# Questo blocco parte solo se lanciate il file: python riga_acquisto.py
if __name__ == "__main__":
    print(riga_acquisto("piuma", 1.2, 3))
