"""Palestra · esercizi individuali, per chi finisce prima.

Si fanno in ordine, uno alla volta: pytest -v vi dice a che punto siete.
Niente AI: il bigino (giorno-03/BIGINO.md) e docs.python.org bastano.
"""


def pari_o_dispari(numero: int) -> str:
    """pari_o_dispari(4) -> "pari"     pari_o_dispari(7) -> "dispari"

    Suggerimento: numero % 2 è il resto della divisione per 2.
    """
    if numero % 2 == 0:
        return "pari"
    else:
        return "dispari"


def inverti(parola: str) -> str:
    """inverti("ciao") -> "oaic" """
    reversed_word = ""
    for i in range(len(parola) -1, -1, -1):
        reversed_word += parola[i]
    return reversed_word


def conto_alla_rovescia(partenza: int) -> list[int]:
    """Con un ciclo while.   conto_alla_rovescia(3) -> [3, 2, 1]     conto_alla_rovescia(0) -> []"""
    alla_rovescia = []
    while partenza > 0:
        alla_rovescia.append(partenza)
        partenza -= 1
    return alla_rovescia


def tabellina(numero: int) -> list[int]:
    """I primi 10 multipli, con range().   tabellina(3) -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]"""
    tabellina = list(range(numero, (numero * 10) + 1, numero))
    return tabellina


def conta_vocali(testo: str) -> int:
    """Conta a, e, i, o, u, maiuscole comprese.   conta_vocali("Ciao Anna") -> 5"""
    testo_minuscolo = testo.lower()
    vocali = ["a", "e", "i", "o", "u"]
    counter = 0
    for lettera in testo_minuscolo:
        if lettera in vocali:
            counter += 1
    return counter



def media(numeri: list[float]) -> float:
    """media([6, 7, 8]) -> 7.0     media([]) -> 0.0   (niente divisione per zero)"""
    if not numeri:
        return 0.0
    media = sum(numeri) / len(numeri)
    return media


def parola_piu_lunga(frase: str) -> str:
    """A parità vince la prima.   parola_piu_lunga("il gatto mangia") -> "mangia" """
    parole = frase.split()
    parola_piu_lunga = ""
    for parola in parole:
        if len(parola) > len(parola_piu_lunga):
            parola_piu_lunga = parola
    return parola_piu_lunga


def palindromo(frase: str) -> bool:
    """Si legge uguale nei due sensi, senza contare spazi e maiuscole.

    palindromo("Anna") -> True
    palindromo("I topi non avevano nipoti") -> True
    palindromo("Python") -> False
    """
    check_frase = frase.strip().replace(" ", "").lower()
    reversed_frase = check_frase[::-1]
    return check_frase == reversed_frase
    


def pizza_pasta(numero: int) -> str:
    """Multiplo di 3 -> "pizza", di 5 -> "pasta", di tutti e due -> "pizzapasta", altrimenti il numero come testo.

    pizza_pasta(9) -> "pizza"   pizza_pasta(10) -> "pasta"   pizza_pasta(15) -> "pizzapasta"   pizza_pasta(7) -> "7"
    """
    if numero % 3 == 0 and numero % 5 == 0:
        return "pizzapasta"
    elif numero % 3 == 0:
        return "pizza"
    elif numero % 5 == 0:
        return "pasta"
    else:
        return str(numero)


def dopo_le_vendite(magazzino: dict[str, int], vendite: list[str]) -> dict[str, int]:
    """Ogni elemento di vendite è un pezzo venduto: toglietelo dal magazzino.
    Restituite un dizionario nuovo, senza modificare quello ricevuto.

    dopo_le_vendite({"penna": 5, "zaino": 2}, ["penna", "penna", "zaino"]) -> {"penna": 3, "zaino": 1}
    """
    magazzino_aggiornato = magazzino.copy()
    for pezzo in vendite:
            magazzino_aggiornato[pezzo] -= 1
    return magazzino_aggiornato
