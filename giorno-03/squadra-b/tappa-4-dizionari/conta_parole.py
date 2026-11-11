"""HOGWARTS · Tappa 4 · Numero 1 · Le recensioni della locanda

La storia:  Madama Rosmerta vuole sapere quali parole tornano più spesso nelle recensioni dei Tre Manici di Scopa.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_conta_parole.py -v     (tutto verde = finito)
"""


def conta_parole(frase: str) -> dict[str, int]:
    """Conta quante volte compare ogni parola, senza distinguere maiuscole e minuscole.

    conta_parole("Il gufo e il gatto")  ->  {"il": 2, "gufo": 1, "e": 1, "gatto": 1}
    conta_parole("")                    ->  {}
    """

    conteggio = {}

    parole = frase.lower().split()

    for parola in parole:
        if parola in conteggio:
            conteggio[parola] += 1
        else:
            conteggio[parola] = 1
    return conteggio
        
        

# Questo blocco parte solo se lanciate il file: python conta_parole.py
if __name__ == "__main__":
    print(conta_parole("Il gufo e il gatto"))
