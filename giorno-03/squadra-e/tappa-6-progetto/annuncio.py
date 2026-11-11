"""HOGWARTS · Tappa 6 · Numero 3 · Chi vince?

La storia:  Alla fine del duello Allock annuncia i punti di ognuno e il vincitore. Il testo dell'annuncio lo prepari tu.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_annuncio.py -v     (tutto verde = finito)
"""

TITOLO = "CLUB DEI DUELLANTI"


def annuncia(punti: dict[str, int]) -> str:
    """Prepara l'annuncio: titolo, i punti di ogni mago in ordine alfabetico, chi vince.

    annuncia({"Harry": 20, "Draco": 0})  ->  il testo qui sotto, righe unite da "\n"

    CLUB DEI DUELLANTI
    Draco: 0 punti
    Harry: 20 punti
    VINCE: Harry

    Vince chi ha più punti. Se i primi hanno gli stessi punti, l'ultima riga è PAREGGIO.
    Restituisce il testo (return), non lo stampa: la print la fa duello.py.
    """
    # creo la lista che conterrà gli elementi dell'annuncio
    annuncio = []
    
    # aggiungo il titolo
    annuncio.append(TITOLO)

    # aggiungo i punteggi di ogni mago in ordine alfabetico
    for mago in sorted(punti):
        annuncio.append(f"{mago}: {punti[mago]} punti")
    
    # verifico qual è il punteggio più alto o se c'è pareggio
    punteggio_max = 0
    vincitore = ""
    pareggio = False

    for mago, punteggio in punti.items():
        if punteggio > punteggio_max:
            punteggio_max = punteggio
            vincitore = mago
            pareggio = False
        elif punteggio == punteggio_max:
            pareggio = True

    if pareggio:
        annuncio.append("PAREGGIO")
    else:
        annuncio.append(f"VINCE: {vincitore}")

    # formatto il contenuto dell'annuncio suddiviso per righe
    return "\n".join(annuncio)


# Questo blocco parte solo se lanciate il file: python annuncio.py
if __name__ == "__main__":
    print(annuncia({"Harry": 20, "Draco": 0}))
