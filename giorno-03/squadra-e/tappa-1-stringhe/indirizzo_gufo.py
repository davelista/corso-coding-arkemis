def indirizzo_gufo(nome: str, cognome: str) -> str:
    """Restituisce l'indirizzo gufo: nome.cognome@hogwarts.it, tutto minuscolo e senza spazi.

    indirizzo_gufo("Mario", "Rossi")          ->  "mario.rossi@hogwarts.it"
    indirizzo_gufo("ANNA", "Bianchi")         ->  "anna.bianchi@hogwarts.it"
    indirizzo_gufo("Anna Maria", "De Luca")   ->  "annamaria.deluca@hogwarts.it"
    """
    nome_pulito = nome.lower().replace(" ", "")
    cognome_pulito = cognome.lower().replace(" ", "")
    return f"{nome_pulito}.{cognome_pulito}@hogwarts.it"