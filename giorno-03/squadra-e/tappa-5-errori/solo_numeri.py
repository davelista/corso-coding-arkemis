"""HOGWARTS · Tappa 5 · Numero 3 · La Penna Prendiappunti

La storia:  La Penna Prendiappunti trascrive gli scontrini, ma ogni tanto inventa. Teniamo solo gli importi che sono numeri.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_solo_numeri.py -v     (tutto verde = finito)
"""


def solo_numeri(valori: list[str]) -> list[float]:
    """Trasforma i testi in numeri con float(), saltando quelli che non sono numeri.

    Usate try/except ValueError dentro il ciclo.

    solo_numeri(["3", "ciao", "2.5", "", " 4 "])  ->  [3.0, 2.5, 4.0]
    """
    numeri = []

    for valore in valori:
        try:
            valore = float(valore)
            numeri.append(valore)
        except ValueError:
            pass

    return numeri

# Questo blocco parte solo se lanciate il file: python solo_numeri.py
if __name__ == "__main__":
    print(solo_numeri(["3", "ciao", "2.5", "", " 4 "]))
