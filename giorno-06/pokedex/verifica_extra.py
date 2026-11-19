"""
Il Pokédex del professor Oak · le domande bonus: controlla le risposte in risposte_extra.txt.

    python3 verifica_extra.py        controlla tutte le risposte bonus
    python3 verifica_extra.py 15     controlla solo la 15, e se è sbagliata ti dà un suggerimento

Non va su internet: le richieste a pokeapi.co le fate voi, con il browser o con curl.
La domanda 18 non si controlla: è da discutere insieme alla fine.
"""
import hashlib
import re
import sys
from pathlib import Path

FILE = Path(__file__).resolve().parent / "risposte_extra.txt"
DOMANDE = [12, 13, 14, 15, 16, 17, 19]

# Un'impronta per ogni risposta giusta: così la risposta non si legge da qui.
ATTESI = {
    12: "35340ddcc6b46aed",
    13: "da74ae96b4cd9de3",
    14: "e4b69e998fcfa022",
    15: "8306aaba598c89f9",
    16: "f5c84e4611cdbec6",
    17: "1460072aa04a0099",
    19: "4289c8b98a9f510d",
}

SUGGERIMENTI = {
    12: "Aprite /pokemon?limit=1: in cima alla risposta, prima di \"results\", c'è un campo che dice quanti sono in tutto.",
    13: "In /type/fire cercate \"damage_relations\" e dentro \"double_damage_to\": ogni elemento ha un \"name\". Sono quattro: scriveteli separati da una virgola.",
    14: "I dati di Pikachu come specie stanno in /pokemon-species/pikachu. Cercate \"habitat\" (dentro c'è \"name\") e \"capture_rate\". Scrivete i due valori separati da una virgola.",
    15: "In /move/thunderbolt cercate \"power\". Poi cercate \"names\": è una lista, ogni elemento ha un \"language\". Quello con \"it\" ha il nome italiano. Scrivete nome e potenza separati da una virgola.",
    16: "Aprite /pokemon?limit=20, copiate l'indirizzo che c'è in \"next\" e apritelo. Il primo elemento di \"results\" è la risposta.",
    17: "curl -i …/pokemon/Pikachu e curl -i …/pokemon/pika: guardate la prima riga di tutte e due. Scrivete i due codici, nell'ordine.",
    19: "curl -v …/pokemon/ditto: le righe che iniziano con > sono la richiesta che parte. Dopo la prima riga (GET …) ci sono gli header: scrivete i loro nomi, separati da una virgola.",
}

ESEMPIO = """# Il Pokédex del professor Oak · le domande bonus
# Una risposta per riga, dopo il numero e i due punti. Più valori? Separateli con una virgola.
# La 18 non c'è: è da discutere insieme alla fine.
"""

ITALIANO = {
    "coleottero": "bug", "acciaio": "steel", "erba": "grass", "ghiaccio": "ice",
    "foresta": "forest", "bosco": "forest",
}


def parole(t: str) -> list[str]:
    return [ITALIANO.get(p, p) for p in re.split(r"[,;/\s]+|\be\b|\band\b", t) if p]


def normalizza(n: int, testo: str) -> str:
    t = testo.strip().strip("\"'`«»").strip().lower()
    t = re.sub(r"\s+", " ", t)
    if n == 12:
        numero = re.search(r"\d[\d.]*", t)
        t = numero.group().replace(".", "") if numero else t
    if n in (13, 14, 15):
        t = ",".join(sorted(set(parole(t))))
    if n == 17:
        t = ",".join(re.findall(r"\b[1-5]\d\d\b", t))
    if n == 19:
        nomi = re.findall(r"\b(host|user-agent|accept)\b", t)
        t = ",".join(sorted(set(nomi)))
    return t


def impronta(n: int, testo: str) -> str:
    return hashlib.sha256(f"pokedex-extra-{n}-{testo}".encode()).hexdigest()[:16]


def leggi_risposte() -> dict[int, str]:
    if not FILE.exists():
        FILE.write_text(ESEMPIO + "".join(f"{n}:\n" for n in DOMANDE), encoding="utf-8")
        print("Non c'era risposte_extra.txt: l'ho creato io, vuoto. Scrivete lì le risposte.\n")
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
        print(f"✅ Domanda {n}: giusto!")
        return True
    print(f"❌ Domanda {n}: «{risposta}» non torna")
    if dettagli:
        print("   Suggerimento: " + SUGGERIMENTI[n])
    return False


def main() -> None:
    risposte = leggi_risposte()
    if "18" in sys.argv[1:]:
        print("La 18 non si controlla: guardate la colonna Tempo e tenete pronta la vostra ipotesi, ne parliamo insieme.")
    scelte = [int(x) for x in sys.argv[1:] if x.isdigit() and int(x) in DOMANDE] or DOMANDE
    dettagli = len(sys.argv) > 1
    giuste = sum(controlla(n, risposte.get(n, ""), dettagli) for n in scelte)
    if len(scelte) > 1:
        print(f"\n{giuste} su {len(scelte)} domande bonus.")
        if giuste == len(DOMANDE):
            print("Tutte giuste! Siete pronti per l'Indovina chi. 🎭")
        elif giuste < len(scelte):
            print("Per un suggerimento su una domanda: python3 verifica_extra.py 15")


if __name__ == "__main__":
    main()
