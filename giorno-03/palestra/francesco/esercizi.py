"""Palestra · esercizi individuali, per chi finisce prima.

Si fanno in ordine, uno alla volta: pytest -v vi dice a che punto siete.
Niente AI: il bigino (giorno-03/BIGINO.md) e docs.python.org bastano.
"""


def pari_o_dispari(numero: int) -> str:
    """pari_o_dispari(4) -> "pari"     pari_o_dispari(7) -> "dispari"

    Suggerimento: numero % 2 è il resto della divisione per 2.
    """
    if numero%2 == 0:
        return "pari"
    return "dispari"


def inverti(parola: str) -> str:
    """inverti("ciao") -> "oaic" """
    caratteri = []
    parola_invertita = ""
    for c in parola:
        caratteri.append(c)
    caratteri.reverse()

    for c in caratteri:
        parola_invertita += c

    return parola_invertita


def conto_alla_rovescia(partenza: int) -> list[int]:
    """Con un ciclo while.   conto_alla_rovescia(3) -> [3, 2, 1]     conto_alla_rovescia(0) -> []"""
    timer = []
    while(partenza != 0):
        timer.append(partenza)
        partenza -= 1
        
    return timer

def tabellina(numero: int) -> list[int]:
    """I primi 10 multipli, con range().   tabellina(3) -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]"""
    risultato = []
    for i in range(1,11):
        risultato.append(numero*i)
    return risultato



def conta_vocali(testo: str) -> int:
    """Conta a, e, i, o, u, maiuscole comprese.   conta_vocali("Ciao Anna") -> 5"""
    testo_pulito = testo.lower()
    count = 0
    for c in testo_pulito:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            count += 1
    return count


def media(numeri: list[float]) -> float:
    """media([6, 7, 8]) -> 7.0     media([]) -> 0.0   (niente divisione per zero)"""
    sum = 0
    for n in numeri:
        if n == 0:
            continue
        sum += n
    if len(numeri) > 0:
        return sum/len(numeri) 
    return 0.0

def parola_piu_lunga(frase: str) -> str:
    """A parità vince la prima.   parola_piu_lunga("il gatto mangia") -> "mangia" """
    parole = frase.split(" ")
    massimo = 0
    for parola in parole:
        if len(parola) > massimo:
            massimo = len(parola)
            p = parola
    return p

def palindromo(frase: str) -> bool:
    """Si legge uguale nei due sensi, senza contare spazi e maiuscole.

    palindromo("Anna") -> True
    palindromo("I topi non avevano nipoti") -> True
    palindromo("Python") -> False
    """
    if inverti(frase).lower().replace(" ", "") == frase.lower().replace(" ", ""):
        return True
    return False


def pizza_pasta(numero: int) -> str:
    """Multiplo di 3 -> "pizza", di 5 -> "pasta", di tutti e due -> "pizzapasta", altrimenti il numero come testo.

    pizza_pasta(9) -> "pizza"   pizza_pasta(10) -> "pasta"   pizza_pasta(15) -> "pizzapasta"   pizza_pasta(7) -> "7"
    """
    if numero%3 == 0 and numero%5 == 0:
        return "pizzapasta"
    elif numero%3 == 0:
        return "pizza"
    elif numero%5 == 0:
        return "pasta"
    else:
        return str(numero)
        


def dopo_le_vendite(magazzino: dict[str, int], vendite: list[str]) -> dict[str, int]:
    """Ogni elemento di vendite è un pezzo venduto: toglietelo dal magazzino.
    Restituite un dizionario nuovo, senza modificare quello ricevuto.

    dopo_le_vendite({"penna": 5, "zaino": 2}, ["penna", "penna", "zaino"]) -> {"penna": 3, "zaino": 1}
    """
    new_magazzino = dict(magazzino)
    for m in new_magazzino:
        for v in vendite:
            if m == v:
                if new_magazzino[m] == 0:
                    continue
                new_magazzino[m] -= 1
    
    return new_magazzino
if __name__ == "__main__":
    print(dopo_le_vendite({"penna": 5, "zaino": 2}, ["penna", "penna", "zaino"]))