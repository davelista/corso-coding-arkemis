"""HOGWARTS · Tappa 1 · Numero 1 · Le iniziali sui bauli

La storia:  Sull'Hogwarts Express i bauli sono tutti uguali: su ognuno vanno le iniziali del proprietario, H.P. per Harry Potter.

Cosa fai:   al posto di pass scrivi il codice della funzione qui sotto.
Come provi: pytest test_iniziali.py -v     (tutto verde = finito)
"""


def iniziali(nome: str, cognome: str) -> str:
    """Restituisce le iniziali di nome e cognome: maiuscole, ognuna con il punto.

    iniziali("Mario", "Rossi")    ->  "M.R."
    iniziali("anna", "verdi")     ->  "A.V."
    iniziali("  luca ", " neri")  ->  "L.N."   (gli spazi ai lati non contano)
    """
   
    inizialeNome = nome.replace(" ", "")
    inizialeCognome = cognome.replace(" ", "")
    return f'{inizialeNome[0].upper()}.{inizialeCognome[0].upper()}.'
# Questo blocco parte solo se lanciate il file: python iniziali.py
if __name__ == "__main__":
    print(iniziali("Mario", "Rossi")) 
    