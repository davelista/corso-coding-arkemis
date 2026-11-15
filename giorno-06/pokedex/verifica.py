"""
Il Pokédex del professor Oak: controlla le risposte in risposte.txt.

    python3 verifica.py        controlla tutte le risposte
    python3 verifica.py 5      controlla solo la 5, e se è sbagliata ti dà un suggerimento

Non va su internet: le richieste a pokeapi.co le fate voi, con il browser o con curl.
"""
import hashlib
import re
import sys
from pathlib import Path

FILE = Path(__file__).resolve().parent / "risposte.txt"
DOMANDE = 11

# Un'impronta per ogni risposta giusta: così la risposta non si legge da qui.
ATTESI = {
    1: "2d4c3888cd98b2a3",
    2: "d92b90fa687b0dfa",
    3: "8add0d90718b8164",
    4: "00f0fc8fdcac6d8c",
    5: "a587cb872eb148f7",
    6: "366b5013e32ecc5d",
    7: "af2c6b34199322f0",
    8: "ee8ef5a53631ce46",
    9: "06c1b51bf3dfe5b5",
    10: "ddf75f6be8a736b6",
    11: "6591f735ceabdeb4",
}

SUGGERIMENTI = {
    1: "Aprite https://pokeapi.co/api/v2/pokemon/pikachu e cercate \"types\": è una lista, dentro ogni elemento c'è \"type\" e dentro ancora \"name\".",
    2: "Al posto del nome, nel percorso si può mettere il numero: /pokemon/133.",
    3: "Il campo è \"weight\" in /pokemon/snorlax. Un ettogrammo è un decimo di chilo: dividete per 10.",
    4: "In /pokemon/bulbasaur cercate \"abilities\": ogni abilità ha \"is_hidden\". Quella con true è la nascosta.",
    5: "Il codice di stato non è nel JSON: sta nella prima riga della risposta. curl -i https://pokeapi.co/api/v2/pokemon/missingno",
    6: "curl -i https://pokeapi.co/api/v2/pokemonn/pikachu e guardate la prima riga. Non è lo stesso codice della domanda 5.",
    7: "curl -i https://pokeapi.co/api/v2/pokemon/pikachu: gli header sono le righe tra il codice di stato e il JSON.",
    8: "limit dice quanti risultati volete, offset quanti saltarne. La posizione 1 ha offset 0: la 151 ha offset 150. Provate /pokemon?limit=1&offset=150",
    9: "In /pokemon/pikachu cercate \"species\" e aprite il suo \"url\". Lì dentro c'è \"evolves_from_species\".",
    10: "Posizione 94 vuol dire offset 93: /pokemon?limit=1&offset=93. Seguite l'url del risultato e guardate \"types\". Sono due: scriveteli separati da una virgola.",
    11: "Da /pokemon-species/eevee aprite l'url di \"evolution_chain\". Dentro \"chain\" c'è \"evolves_to\": è una lista. Quanti elementi ha?",
}

ESEMPIO = """# Il Pokédex del professor Oak · le vostre risposte
# Una risposta per riga, dopo il numero e i due punti. Esempio:   1: bulbasaur
"""


def normalizza(n: int, testo: str) -> str:
    t = testo.strip().strip("\"'`«»").strip().lower()
    t = re.sub(r"\s+", " ", t)
    if n in (5, 6):
        codice = re.search(r"\b[1-5]\d\d\b", t)
        t = codice.group() if codice else t
    if n in (3, 11):
        numero = re.search(r"\d+(?:[.,]\d+)?", t)
        t = numero.group().replace(",", ".") if numero else t
        if t.endswith(".0"):
            t = t[:-2]
    if n == 7:
        t = t.split(";")[0].strip()
        t = re.sub(r"^content-type\s*:\s*", "", t)
    if n == 10:
        parti = [p for p in re.split(r"[,;/\s]+|\be\b|\band\b", t) if p]
        t = ",".join(sorted(set(parti)))
    return t


def impronta(n: int, testo: str) -> str:
    return hashlib.sha256(f"pokedex-oak-{n}-{testo}".encode()).hexdigest()[:16]


def leggi_risposte() -> dict[int, str]:
    if not FILE.exists():
        FILE.write_text(ESEMPIO + "".join(f"{n}:\n" for n in range(1, DOMANDE + 1)), encoding="utf-8")
        print("Non c'era risposte.txt: l'ho creato io, vuoto. Scrivete lì le risposte.\n")
    risposte = {}
    for riga in FILE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*(\d+)\s*[:.)-]\s*(.*)$", riga)
        if m and not riga.lstrip().startswith("#"):
            risposte[int(m.group(1))] = m.group(2).strip()
    return risposte


def controlla(n: int, risposta: str, dettagli: bool) -> bool:
    if not risposta:
        print(f"⏭️  Domanda {n}: ancora vuota")
        return False
    if impronta(n, normalizza(n, risposta)) == ATTESI[n]:
        print(f"✅ Domanda {n}: giusto! Il dato torna nel Pokédex.")
        return True
    print(f"❌ Domanda {n}: «{risposta}» non torna")
    if dettagli:
        print("   Suggerimento: " + SUGGERIMENTI[n])
    return False


def main() -> None:
    risposte = leggi_risposte()
    scelte = [int(x) for x in sys.argv[1:] if x.isdigit() and 1 <= int(x) <= DOMANDE] or list(range(1, DOMANDE + 1))
    dettagli = len(sys.argv) > 1
    giuste = sum(controlla(n, risposte.get(n, ""), dettagli) for n in scelte)
    if len(scelte) > 1:
        print(f"\n{giuste} su {len(scelte)}: il Pokédex ricorda {giuste} dati su {len(scelte)}.")
        if giuste == DOMANDE:
            print("Pokédex completo! E adesso sapete chi si è mangiato i dati. 👻")
        elif giuste < len(scelte):
            print("Per un suggerimento su una domanda: python3 verifica.py 5")


if __name__ == "__main__":
    main()
