"""HOGWARTS · Tappa 5 · Numero 2 · Il conto da Mielandia

La storia:  Il conto dei dolci si divide in parti uguali. Ma se qualcuno scrive zero maghi, il programma non deve esplodere.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_dividi_conto.py -v     (tutto verde = finito)
"""


def dividi_conto(totale: float, persone: int) -> float:
    """Divide il conto tra le persone, arrotondando a 2 decimali con round().

    dividi_conto(100, 4)  ->  25.0
    dividi_conto(100, 3)  ->  33.33
    dividi_conto(50, 0)   ->  ValueError   (sollevatelo voi, prima di dividere)
    """
    
def dividi_conto(totale: float, persone: int) -> float:
    """Divide il conto tra le persone, arrotondando a 2 decimali con round().

    dividi_conto(100, 4)  ->  25.0
    dividi_conto(100, 3)  ->  33.33
    dividi_conto(50, 0)   ->  ValueError   (sollevatelo voi, prima di dividere)
    """
    if persone <= 0:
        raise ValueError("Serve almeno una persona")
    risultato = totale / persone
    return round(risultato, 2)


# Questo blocco parte solo se lanciate il file: python dividi_conto.py
if __name__ == "__main__":
    print(dividi_conto(100, 3))
