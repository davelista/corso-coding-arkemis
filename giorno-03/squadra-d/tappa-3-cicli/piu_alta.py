"""HOGWARTS · Tappa 3 · Numero 3 · Il Lago Nero a gennaio

La storia:  Hagrid misura la temperatura del Lago Nero ogni mattina. Qual è stata la più alta? A gennaio sono tutte sotto zero.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_piu_alta.py -v     (tutto verde = finito)
"""


def piu_alta(temperature: list[float]) -> float:
    """Restituisce la temperatura più alta della lista (che non è mai vuota). Senza usare max().

    piu_alta([18.5, 22.0, 19.5])   ->  22.0
    piu_alta([-3.0, -1.5, -7.0])   ->  -1.5     (attenzione: d'inverno sono tutte sotto zero)
    """
    pass  # al posto di pass: il vostro codice


# Questo blocco parte solo se lanciate il file: python piu_alta.py
if __name__ == "__main__":
    print(piu_alta([18.5, 22.0, 19.5]))
