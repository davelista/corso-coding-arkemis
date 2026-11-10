"""HOGWARTS · Tappa 3 · Numero 1 · La cassa delle Cioccorane

La storia:  Ognuno segna quanto ha messo nella cassa comune. Pix si diverte a scrivere numeri negativi: quelli non contano.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_totale.py -v     (tutto verde = finito)
"""


def totale(prezzi: list[float]) -> float:
    """Somma i prezzi, ignorando quelli negativi (sono errori di cassa). Senza usare sum().

    totale([10, 20, 5.5])    ->  35.5
    totale([10, -3, 2.5])    ->  12.5
    totale([])               ->  0
    """
    pass  # al posto di pass: il vostro codice


# Questo blocco parte solo se lanciate il file: python totale.py
if __name__ == "__main__":
    print(totale([10, -3, 2.5]))
