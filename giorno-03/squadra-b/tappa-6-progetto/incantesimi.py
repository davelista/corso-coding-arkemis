"""HOGWARTS · Tappa 6 · Numero 2 · Il libro degli incantesimi

La storia:  Ogni incantesimo è una funzione: riceve i punti del bersaglio e restituisce quelli che gli restano. Expelliarmus è già scritto, gli altri li scrivi tu.

Cosa fai:   al posto di ogni pass scrivi il codice delle funzioni qui sotto.
Come provi: pytest test_incantesimi.py -v     (tutto verde = finito)
"""


# Un incantesimo è una funzione: riceve i punti del bersaglio
# e restituisce (return) i punti che gli restano. Mai sotto zero.
# Il primo è già scritto: guardalo, poi scrivi gli altri tre.


def expelliarmus(punti: int) -> int:
    """Disarma il bersaglio: gli toglie 10 punti.

    expelliarmus(50)  ->  40
    expelliarmus(5)   ->  0
    """
    punti = punti - 10
    if punti < 0:
        punti = 0
    return punti


def stupeficium(punti: int) -> int:
    """Stordisce il bersaglio: gli toglie 20 punti. Mai sotto zero.

    stupeficium(50)  ->  30
    stupeficium(15)  ->  0
    """
    punti = punti - 20
    if punti < 0:
        punti = 0
    return punti


def petrificus_totalus(punti: int) -> int:
    """Pietrifica il bersaglio: gli toglie 30 punti. Mai sotto zero.

    petrificus_totalus(50)  ->  20
    petrificus_totalus(20)  ->  0
    """
    punti = punti - 30
    if punti < 0:
        punti = 0
    return punti


def lancia(incantesimo: str, punti: int) -> int:
    """Lancia l'incantesimo con questo nome e restituisce i punti che restano al bersaglio.

    lancia("expelliarmus", 50)        ->  40
    lancia("petrificus totalus", 50)  ->  20    nel CSV c'è lo spazio, nel nome della funzione il _
    lancia("serpensortia", 50)        ->  50    incantesimo che il libro non conosce: fa cilecca
    """
    punti_restanti = 0
    if incantesimo == "expelliarmus":
        punti_restanti = expelliarmus(punti)
    elif incantesimo == "stupeficium":
        punti_restanti = stupeficium(punti)
    elif incantesimo == "petrificus totalus":
        punti_restanti = petrificus_totalus(punti)
    else :
        punti_restanti = punti
    return punti_restanti


# Questo blocco parte solo se lanciate il file: python incantesimi.py
if __name__ == "__main__":
    print(lancia("stupeficium", 50))
