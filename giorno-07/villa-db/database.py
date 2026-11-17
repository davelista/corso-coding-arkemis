"""Il collegamento al database villa. QUESTO FILE NON SI TOCCA.

Da main.py si usa così:

    with connetti() as conn:
        righe = conn.execute("SELECT * FROM ospiti").fetchall()

Il with apre la connessione e, quando finisce, la chiude.
Se dentro è andato tutto bene fa il COMMIT (le modifiche restano),
se c'è stato un errore fa il ROLLBACK (le modifiche spariscono).
"""
import os

import psycopg
from psycopg.rows import dict_row

# Il nome del database. I test usano villa_test, così non toccano i vostri dati.
NOME_DB = os.environ.get("VILLA_DB", "villa")


def connetti() -> psycopg.Connection:
    # dict_row: ogni riga arriva come dizionario  {"id": 1, "nome": "Gaston Dumarais", ...}
    return psycopg.connect(dbname=NOME_DB, row_factory=dict_row)
