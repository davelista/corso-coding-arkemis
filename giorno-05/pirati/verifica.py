"""
Controlla le tue query sul diario di bordo dei pirati.

    python3 verifica.py        controlla tutti gli esercizi
    python3 verifica.py 5      controlla solo l'esercizio 5, e ti mostra cosa ha risposto il database

Le query vanno nei file della cartella risposte/: una query per file.
Il programma non cambia niente nel database: legge e basta.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CARTELLA = Path(__file__).resolve().parent / "risposte"
DATABASE = os.environ.get("PIRATI_DB", "pirati")

# Per ogni esercizio: quante righe e colonne, se conta l'ordine,
# e un'impronta del risultato giusto (così la risposta giusta non si legge da qui).
ATTESI = json.loads(r'''{"1":{"righe":4,"colonne":2,"ordine":true,"insieme":"536b79bb29e55edd","sequenza":"cbb31af936baf5cd"},"2":{"righe":5,"colonne":3,"ordine":true,"insieme":"295fe98389388469","sequenza":"e49e63ab74719bf0"},"3":{"righe":1,"colonne":1,"ordine":false,"insieme":"72cb573c0f06ed22","sequenza":"-"},"4":{"righe":2,"colonne":2,"ordine":false,"insieme":"be8625c26119cb8e","sequenza":"-"},"5":{"righe":4,"colonne":4,"ordine":false,"insieme":"0b1428ca6a80c620","sequenza":"-"},"6":{"righe":3,"colonne":2,"ordine":false,"insieme":"18ee44d93ec4102f","sequenza":"-"},"7":{"righe":7,"colonne":2,"ordine":true,"insieme":"895abb0f25e10e07","sequenza":"d3175fe50af36e2e"},"8":{"righe":3,"colonne":3,"ordine":false,"insieme":"ff27017ccd50d40f","sequenza":"-"},"9":{"righe":1,"colonne":3,"ordine":false,"insieme":"b96f6bfa4d12453b","sequenza":"-"},"10":{"righe":2,"colonne":2,"ordine":false,"insieme":"1edecb4374c7952d","sequenza":"-"}}''')

SUGGERIMENTI = {
    1: "WHERE bandiera = 'pirata', poi ORDER BY nome.",
    2: "WHERE bottino > 5000, poi ORDER BY bottino DESC: DESC vuol dire dal più grande.",
    3: "Ti chiede «quante»: serve un numero solo, con COUNT(*). Il porto mancante si cerca con IS NULL, non con = NULL.",
    4: "Due condizioni insieme: WHERE ... AND .... Attenzione: «più di 30» vuol dire > 30, e 30 non è più di 30.",
    5: "Arrembaggi e navi insieme: JOIN navi n ON n.id = a.nave_id. Poi WHERE a.esito = 'fallito'.",
    6: "Un numero per ogni esito: GROUP BY esito, e COUNT(*) nel SELECT.",
    7: "JOIN tra arrembaggi e navi, WHERE esito = 'riuscito', GROUP BY il nome della nave, SUM(bottino), poi ORDER BY dal più ricco.",
    8: "Come il 7, ma conti invece di sommare. I gruppi si filtrano con HAVING COUNT(*) >= 2, non con WHERE.",
    9: "JOIN tra arrembaggi e navi, ORDER BY bottino DESC, e tieni solo la prima riga con LIMIT 1.",
    10: "Senza LEFT JOIN: prendi le navi il cui id NON è tra i nave_id degli arrembaggi. Cerca NOT IN o NOT EXISTS.",
}

ERRORI = [
    (r"syntax error at or near \"([^\"\n]*)\"", "Errore di scrittura vicino a «{0}». Controlla virgole, apici e l'ordine: SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY, LIMIT."),
    (r"syntax error at end of input", "La query finisce a metà: manca un pezzo alla fine."),
    (r"column \"([^\"]+)\" does not exist", "La colonna «{0}» non esiste. Se è un testo, va tra apici: '{0}'. Se è una colonna, controlla il nome con \\d nome_tabella in psql."),
    (r"relation \"([^\"]+)\" does not exist", "La tabella «{0}» non esiste. In psql, \\dt ti mostra i nomi giusti: navi, arrembaggi."),
    (r"must appear in the GROUP BY clause", "Se nel SELECT c'è COUNT o SUM, ogni altra colonna del SELECT va scritta anche nel GROUP BY."),
    (r"aggregate functions are not allowed in WHERE", "COUNT e SUM non vanno nel WHERE: per filtrare i gruppi si usa HAVING."),
    (r"missing FROM-clause entry for table \"([^\"]+)\"", "Usi «{0}.» ma nel FROM o nel JOIN non c'è una tabella con quel nome o con quel soprannome."),
    (r"column reference \"([^\"]+)\" is ambiguous", "La colonna «{0}» c'è in tutte e due le tabelle: scrivi da quale, per esempio n.{0} oppure a.{0}."),
    (r"read-only transaction", "Qui si legge e basta: niente INSERT, UPDATE o DELETE."),
    (r"database \"[^\"]+\" does not exist", "Il database pirati non c'è ancora. Dalla cartella pirati: createdb pirati, poi psql -d pirati -f pirati.sql"),
    (r"role \"[^\"]+\" does not exist", "PostgreSQL non conosce il tuo utente: rifai il passo «utente» della guida del giorno 1."),
    (r"Connection refused|could not connect|No such file or directory", "PostgreSQL è spento. WSL: sudo service postgresql start · Mac: brew services start postgresql@16"),
]


def impronta(righe):
    return hashlib.sha256(json.dumps(righe, ensure_ascii=False).encode()).hexdigest()[:16]


def normalizza(righe):
    # L'ordine delle colonne non conta: in ogni riga metto i valori in ordine.
    return [sorted(r) for r in righe]


def togli_commenti(testo):
    return re.sub(r"--[^\n]*", "", testo).strip()


def quante_query(testo):
    senza_testi = re.sub(r"'[^']*'", "''", testo)
    return len([p for p in senza_testi.split(";") if p.strip()])


def esegui(query):
    comando = ["psql", "-X", "-q", "-A", "-t", "-F", "\x1f", "-v", "ON_ERROR_STOP=1", "-d", DATABASE]
    ingresso = "BEGIN READ ONLY;\n" + query + "\n;\nROLLBACK;\n"
    ambiente = dict(os.environ, PGDATESTYLE="ISO", PGCLIENTENCODING="UTF8")
    p = subprocess.run(comando, input=ingresso, capture_output=True, text=True, timeout=20, env=ambiente)
    if p.returncode != 0:
        return None, p.stderr
    return [r.split("\x1f") for r in p.stdout.splitlines() if r != ""], ""


def spiega_errore(stderr):
    messaggio = re.sub(r"^psql:<stdin>:\d+: ", "", stderr.strip(), flags=re.M)
    print("   Il database risponde:")
    for riga in messaggio.splitlines()[:4]:
        print("     " + riga)
    for schema, spiegazione in ERRORI:
        m = re.search(schema, stderr)
        if m:
            print("   Vuol dire: " + spiegazione.format(*m.groups()))
            break


def quante(n, una, tante):
    return f"{n} {una if n == 1 else tante}"


def mostra(righe):
    print("   Hai ottenuto:")
    if not righe:
        print("     (nessuna riga)")
    for r in righe[:10]:
        print("     " + " | ".join(v if v != "" else "NULL" for v in r))
    if len(righe) > 10:
        print(f"     ... e altre {len(righe) - 10} righe")


def controlla(n, dettagli):
    file = CARTELLA / f"es{n:02d}.sql"
    if not file.exists():
        print(f"⏭️  Esercizio {n}: non trovo risposte/{file.name}")
        return False
    testo = file.read_text(encoding="utf-8")
    pulito = togli_commenti(testo)
    if not pulito:
        print(f"⏭️  Esercizio {n}: ancora vuoto")
        return False
    if quante_query(pulito) > 1:
        print(f"❌ Esercizio {n}: nel file ci sono più query. Lasciane una sola.")
        return False

    righe, errore = esegui(testo)
    if righe is None:
        print(f"❌ Esercizio {n}: la query dà errore")
        spiega_errore(errore)
        return False

    a = ATTESI[str(n)]
    giusto = impronta(sorted(normalizza(righe))) == a["insieme"]
    in_ordine = (not a["ordine"]) or impronta(normalizza(righe)) == a["sequenza"]
    nota = "" if pulito.endswith(";") else "  (ricordati il ; alla fine)"

    if giusto and in_ordine and a["ordine"] and not re.search(r"order\s+by", pulito, re.I):
        print(f"🟡 Esercizio {n}: i valori sono giusti, ma manca ORDER BY.")
        print("   Senza ORDER BY il database non promette nessun ordine: oggi va bene per caso.")
        return False
    if giusto and in_ordine and n == 10 and re.search(r"left\s+(outer\s+)?join", pulito, re.I):
        print(f"🟡 Esercizio {n}: risultato giusto, ma l'esercizio chiede un modo senza LEFT JOIN.")
        print("   Prova con NOT IN oppure NOT EXISTS.")
        return False
    if giusto and in_ordine:
        print(f"✅ Esercizio {n}: giusto!{nota}")
        if dettagli:
            mostra(righe)
        return True

    print(f"❌ Esercizio {n}: non ancora")
    colonne = len(righe[0]) if righe else 0
    if giusto:
        print("   Le righe sono quelle giuste, ma in ordine sbagliato. Controlla ORDER BY: ASC dal più piccolo, DESC dal più grande.")
    elif righe and colonne != a["colonne"]:
        print(f"   {quante(a['colonne'], 'colonna', 'colonne')} attese, tu ne hai {colonne}. Rileggi quali colonne chiede l'esercizio.")
    elif len(righe) != a["righe"]:
        print(f"   {quante(a['righe'], 'riga', 'righe')} attese, tu ne hai {len(righe)}.")
        if len(righe) > a["righe"]:
            print("   Troppe righe: forse manca una condizione nel WHERE.")
        else:
            print("   Poche righe: forse il WHERE è troppo stretto.")
    else:
        print(f"   Righe e colonne sono quante servono ({a['righe']} × {a['colonne']}), ma i valori no.")
    print("   Suggerimento: " + SUGGERIMENTI[n])
    if dettagli:
        mostra(righe)
    return False


def main():
    if not shutil.which("psql"):
        print("Non trovo psql. Su Windows lancia questo programma dal terminale di Ubuntu (WSL), non da PowerShell.")
        sys.exit(1)
    scelti = [int(x) for x in sys.argv[1:] if x.isdigit() and 1 <= int(x) <= 10] or list(range(1, 11))
    dettagli = len(sys.argv) > 1
    giusti = sum(controlla(n, dettagli) for n in scelti)
    if len(scelti) > 1:
        print(f"\n{giusti} su {len(scelti)} giusti.")
        if giusti < len(scelti):
            print("Per vedere cosa risponde il database a un esercizio: python3 verifica.py 5")


if __name__ == "__main__":
    main()
