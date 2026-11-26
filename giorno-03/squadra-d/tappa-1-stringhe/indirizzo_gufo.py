"""HOGWARTS · Tappa 1 · Numero 2 · La posta via gufo

La storia:  Ogni studente riceve un indirizzo per i gufi: nome.cognome@hogwarts.it, tutto minuscolo e senza spazi.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_indirizzo_gufo.py -v     (tutto verde = finito)
"""


def indirizzo_gufo(nome: str, cognome: str) -> str:
    """Restituisce l'indirizzo gufo: nome.cognome@hogwarts.it, tutto minuscolo e senza spazi.

    indirizzo_gufo("Mario", "Rossi")          ->  "mario.rossi@hogwarts.it"
    indirizzo_gufo("ANNA", "Bianchi")         ->  "anna.bianchi@hogwarts.it"
    indirizzo_gufo("Anna Maria", "De Luca")   ->  "annamaria.deluca@hogwarts.it"
    """
    # pass  # al posto di pass: il vostro codice, che finisce con un return

    nome_studente = nome.lower().replace(" ", "")
    cognome_studente = cognome.lower().replace(" ", "")
    return f"{nome_studente}.{cognome_studente}@hogwarts.it"


# Questo blocco parte solo se lanciate il file: python indirizzo_gufo.py
if __name__ == "__main__":
    print(indirizzo_gufo("Anna Maria", "De Luca"))
