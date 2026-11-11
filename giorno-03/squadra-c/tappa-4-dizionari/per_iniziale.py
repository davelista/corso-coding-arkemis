"""HOGWARTS · Tappa 4 · Numero 3 · La lista per il tavolo

La storia:  Per la prenotazione Madama Rosmerta vuole i nomi divisi per iniziale.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_per_iniziale.py -v     (tutto verde = finito)
"""


def per_iniziale(nomi: list[str]) -> dict[str, list[str]]:
    """Raggruppa i nomi per iniziale. La chiave è l'iniziale maiuscola,
    il valore la lista dei nomi, scritti come sono e nell'ordine in cui arrivano.

    per_iniziale(["Harry", "Ron", "hermione"])  ->  {"H": ["Harry", "hermione"], "R": ["Ron"]}
    per_iniziale([])                           ->  {}
    """
    risultato = {}
    for nome in nomi:
        if nome:  
            iniziale = nome[0].upper()
            if iniziale not in risultato:
                risultato[iniziale] = []
            risultato[iniziale].append(nome)
    return risultato


# Questo blocco parte solo se lanciate il file: python per_iniziale.py
if __name__ == "__main__":
    print(per_iniziale(["Harry", "Ron", "hermione"]))
