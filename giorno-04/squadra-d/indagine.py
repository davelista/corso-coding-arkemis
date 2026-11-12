"""GRAN BURRONE · Dove è stato nascosto l'Anello?

La storia:  la notte dopo il Consiglio di Elrond, l'Anello sparisce dal comodino di Frodo.
            Nessuno ha lasciato la valle: l'Anello è ancora a Gran Burrone, nascosto da qualche parte.
Cosa fai:   lanci il programma. Si ferma a una tappa con un errore: leggi il traceback,
            trovi la riga sbagliata, la correggi. Poi rilanci, e si ferma alla tappa dopo.
Attenzione: un errore può anche NON fermare il programma. Se arriva in fondo
            ma pytest ha ancora test rossi, un errore c'è ancora: è nella tappa rossa.
Come provi: python indagine.py           (gli indizi)
            pytest -v                    (verde = indizio affidabile)
            python verifica.py "luogo"   (quando pensate di saperlo)

Le regole: si corregge solo questo file. dati.py e i test non si toccano.
           Tappe 1-6: un errore solo per tappa, correggete il minimo indispensabile.
           Tappa 7: non c'è niente da correggere, c'è codice da scrivere.
"""

import sys

from dati import PERSONE, SPOSTAMENTI, TESTIMONIANZE


# ---------------------------------------------------------------- TAPPA 1
def presenti():
    """Chi ha dormito a Gran Burrone quella notte: i nomi, in ordine alfabetico.

    presenti()  ->  ["Aragorn", "Bilbo", "Boromir", ...]
    """
    # nameError: la variabile persone non è definita
    return sorted(PERSONE)


# ---------------------------------------------------------------- TAPPA 2
def cosa_dice(nome):
    """Il testo della testimonianza di una persona.

    cosa_dice("Gimli")    ->  "Ho dormito tutta la notte. ..."
    cosa_dice("Boromir")  ->  "Nessuna testimonianza"
    """
    for t in TESTIMONIANZE:
        # keyError: la varabiale scritta non esisteva
        if t["chi"] == nome:
            return t["testo"]
    return "Nessuna testimonianza"


# ---------------------------------------------------------------- TAPPA 3
def fumatori():
    """Chi fuma l'erba pipa, nell'ordine in cui compare in PERSONE.

    fumatori()  ->  ["Merry", "Pipino", "Bilbo", ...]
    """
    nomi = []
    for nome, info in PERSONE:
        if info["fuma"]:
            nomi.append(nome)
    return nomi


# ---------------------------------------------------------------- TAPPA 4
def della_razza(razza):
    """Chi è di una certa razza, nell'ordine in cui compare in PERSONE.

    della_razza("elfo")  ->  ["Legolas", "Elrond"]
    """
    nomi = []
    for nome in PERSONE:
        if PERSONE[nome]["razza"] == razza:
            nomi = nomi + nome
    return nomi


# ---------------------------------------------------------------- TAPPA 5
def percorso(nome):
    """I luoghi in cui è passata una persona, in ordine.

    percorso("Sam")  ->  ["Camera di Frodo", "Cucine", "Camera di Frodo"]
    """
    luoghi = []
    for passaggio in SPOSTAMENTI[nome]:
        luoghi.add(passaggio["luogo"])
    return luoghi


# ---------------------------------------------------------------- TAPPA 6
def entrati(luogo, dalle, alle):
    """Chi è entrato in un luogo da un'ora (compresa) a un'altra (esclusa).

    Le ore sono testi come "01:15". Si possono confrontare con < e >=
    perché hanno tutte la stessa forma: due cifre, due punti, due cifre.

    entrati("Cucine", "01:00", "02:00")  ->  ["Sam", "Pipino"]
    """
    for nome in SPOSTAMENTI:
        chi = []
        for passaggio in SPOSTAMENTI[nome]:
            if passaggio["luogo"] == luogo and dalle <= passaggio["ora"] < alle:
                chi.append(nome)
    return chi


# ---------------------------------------------------------------- TAPPA 7
def minuti(ora):
    """Trasforma un'ora in minuti dopo la mezzanotte.

    minuti("00:00")         ->  0
    minuti("01:40")         ->  100
    minuti("verso le due")  ->  ValueError, con un messaggio che inizia con "Ora non valida"
    minuti("25:00")         ->  ValueError, con un messaggio che inizia con "Ora non valida"
    minuti("01:75")         ->  ValueError, con un messaggio che inizia con "Ora non valida"

    Da scrivere voi: i controlli e il raise. Tre controlli:
        1. nell'ora c'è il ":"?
        2. le ore sono tra 0 e 23?
        3. i minuti sono tra 0 e 59?
    Se uno non va: raise ValueError(f"Ora non valida: {ora}")
    Nel messaggio mettete anche l'ora sbagliata: serve a chi legge l'avviso.
    """
    ore, mm = ora.split(":")
    return int(ore) * 60 + int(mm)


def soste(nome):
    """Quanti minuti una persona è rimasta in ogni luogo: {luogo: minuti}.

    La sosta in un luogo finisce quando la persona entra nel luogo dopo.
    Se un'ora del registro non si legge, stampa un avviso e salta quel passaggio.

    soste("Sam")  ->  {"Camera di Frodo": 75, "Cucine": 45}

    Da scrivere voi: il try/except intorno alle chiamate di minuti(...).
    Nell'except:
        print("Attenzione:", errore, file=sys.stderr)    (stderr: il canale degli avvisi)
        continue                                         (salta al giro dopo)
    """
    passaggi = SPOSTAMENTI[nome]
    risultato = {}
    for i in range(len(passaggi) - 1):
        luogo = passaggi[i]["luogo"]
        inizio = minuti(passaggi[i]["ora"])
        fine = minuti(passaggi[i + 1]["ora"])
        risultato[luogo] = fine - inizio
    return risultato


# ---------------------------------------------------------------- L'INDAGINE
def main():
    print("TAPPA 1 · Chi dormiva a Gran Burrone")
    print("   ", ", ".join(presenti()))

    print("\nTAPPA 2 · Le testimonianze")
    for nome in ["Frodo", "Sam", "Elrond"]:
        print(f"    {nome}: {cosa_dice(nome)}")

    print("\nTAPPA 3 · Chi fuma l'erba pipa")
    print("   ", ", ".join(fumatori()))

    print("\nTAPPA 4 · Chi è uno hobbit")
    print("   ", ", ".join(della_razza("hobbit")))

    print("\nTAPPA 5 · Il percorso degli hobbit che fumano")
    for nome in della_razza("hobbit"):
        if nome in fumatori():
            print(f"    {nome}: {' -> '.join(percorso(nome))}")

    print("\nTAPPA 6 · Chi è entrato da Frodo dopo che Sam è sceso in cucina")
    sospetti = entrati("Camera di Frodo", "01:15", "02:00")
    print("   ", ", ".join(sospetti) or "nessuno")

    print("\nTAPPA 7 · Quanto si sono fermati i sospetti, luogo per luogo")
    for nome in sospetti:
        for luogo, durata in soste(nome).items():
            print(f"    {nome}: {luogo}, {durata} minuti")

    print('\nPensate di saperlo? python verifica.py "il luogo"')


# Questo blocco parte solo se lanciate il file: python indagine.py
if __name__ == "__main__":
    main()
