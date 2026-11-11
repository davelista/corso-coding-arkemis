"""HOGWARTS · Tappa 6 · Numero 3 · Chi vince?

La storia:  Alla fine del duello Allock annuncia i punti di ognuno e il vincitore. Il testo dell'annuncio lo prepari tu.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_annuncio.py -v     (tutto verde = finito)
"""

TITOLO = "CLUB DEI DUELLANTI"


def annuncia(punti: dict[str, int]) -> str:
    righe = TITOLO

    for mago in sorted(punti):
      righe = righe + "\n" + mago + ": " + str(punti[mago]) + " punti"

    punti_massimi = max(punti.values())
    vincitore = ""
    pareggio = False
    for mago in punti:
        if punti[mago] == punti_massimi:
            if vincitore == "":
               vincitore = mago
            else:
                pareggio = True

    if pareggio:
        righe = righe + "\nPAREGGIO"
    else:
        righe = righe + "\nVINCE: " + vincitore

    return righe
    
    """Prepara l'annuncio: titolo, i punti di ogni mago in ordine alfabetico, chi vince.

    annuncia({"Harry": 20, "Draco": 0})  ->  il testo qui sotto, righe unite da "\n"

    CLUB DEI DUELLANTI
    Draco: 0 punti
    Harry: 20 punti
    VINCE: Harry

    Vince chi ha più punti. Se i primi hanno gli stessi punti, l'ultima riga è PAREGGIO.
    Restituisce il testo (return), non lo stampa: la print la fa duello.py.
    """
    


# Questo blocco parte solo se lanciate il file: python annuncio.py
if __name__ == "__main__":
    print(annuncia({"Harry": 20, "Draco": 0}))
