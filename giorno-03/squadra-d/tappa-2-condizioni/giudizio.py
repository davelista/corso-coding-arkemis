"""HOGWARTS · Tappa 2 · Numero 1 · I voti di Piton

La storia:  Piton dà un voto da 1 a 10 a ogni pozione. La McGranitt vuole i giudizi, non i numeri.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_giudizio.py -v     (tutto verde = finito)
"""


def giudizio(voto: int) -> str:
    """Trasforma un voto in giudizio.

    da 1 a 5   ->  "insufficiente"
    6          ->  "sufficiente"
    7 e 8      ->  "buono"
    9 e 10     ->  "ottimo"
    altrimenti ->  "voto non valido"   (per esempio 0 oppure 11)
    """
    if voto == 1 or voto <= 5:
        print('insufficente')

    elif voto == 6:
        print('sufficente')

    elif voto == 7 or voto == 8:
        print('buono')

    elif voto == 9 or voto == 10:
            print('ottimo')

    else:
        print('Voto non valido')

# Questo blocco parte solo se lanciate il file: python giudizio.py
if __name__ == "__main__":
    print(giudizio(7))
