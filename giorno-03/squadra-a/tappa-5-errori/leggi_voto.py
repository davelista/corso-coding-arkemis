"""HOGWARTS · Tappa 5 · Numero 1 · La pergamena dei voti

La storia:  I voti arrivano su una pergamena incantata, e qualcuno scrive «sette» al posto di 7.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_leggi_voto.py -v     (tutto verde = finito)
"""


def leggi_voto(testo: str) -> int:
    """Trasforma un testo in un voto intero da 1 a 10.

    leggi_voto("7")      ->  7
    leggi_voto(" 10 ")   ->  10           (gli spazi ai lati non contano)
    leggi_voto("sette")  ->  ValueError   (non è un numero)
    leggi_voto("11")     ->  ValueError   (fuori scala: sollevatelo voi con raise)
    """

    max_voto = 10
    min_voto = 0
    try:
        voto = int(testo)
    except ValueError:
        print("non è un numero")

    voto = int(testo)

    if voto > max_voto or voto <= min_voto:
        raise ValueError("Fuori scala")
    
    return voto

    

# Questo blocco parte solo se lanciate il file: python leggi_voto.py
if __name__ == "__main__":
    print(leggi_voto(" 7 "))
