"""Il test di squadra: diventa verde solo quando i tre pezzi sono tutti su main."""

import subprocess
import sys
from pathlib import Path

CARTELLA = Path(__file__).parent

ATTESO = """SPESE DELL'ANNO A HOGWARTS
dolci: 51.50
pozioni: 15.00
treno: 49.00
TOTALE: 115.50
"""


def test_il_programma_completo():
    risultato = subprocess.run(
        [sys.executable, "report.py", "spese.csv"],
        cwd=CARTELLA,
        capture_output=True,
        text=True,
    )
    assert risultato.stdout == ATTESO
