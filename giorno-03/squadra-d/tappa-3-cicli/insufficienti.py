"""HOGWARTS · Tappa 3 · Numero 2 · Ripetizioni da Hermione

La storia:  Hermione dà ripetizioni di Trasfigurazione a chi ha preso meno di 6. Servono quei voti.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_insufficienti.py -v     (tutto verde = finito)
"""


def insufficienti(voti: list[int]) -> list[int]:
    """Restituisce una lista nuova con i soli voti sotto il 6, nello stesso ordine.

    insufficienti([7, 4, 6, 5, 9])  ->  [4, 5]
    insufficienti([6, 7])           ->  []
    """
    insufficenze = []

    for voto in voti:
        if voto < 6:
            insufficenze.append(voto)

    return insufficenze

# Questo blocco parte solo se lanciate il file: python insufficienti.py
if __name__ == "__main__":
    print(insufficienti([7, 4, 6, 5, 9]))
