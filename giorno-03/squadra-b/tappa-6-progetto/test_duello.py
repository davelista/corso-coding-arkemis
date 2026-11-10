"""Il test di squadra: diventa verde solo quando i tre pezzi sono tutti sul branch della squadra."""

import subprocess
import sys
from pathlib import Path

CARTELLA = Path(__file__).parent

ATTESO = """Turno 1: Draco lancia stupeficium su Harry, che resta con 30 punti
Turno 2: Harry lancia expelliarmus su Draco, che resta con 40 punti
Turno 3: Draco lancia serpensortia su Harry, che resta con 30 punti
Turno 4: Harry lancia stupeficium su Draco, che resta con 20 punti
Turno 5: Draco lancia expelliarmus su Harry, che resta con 20 punti
Turno 6: Harry lancia petrificus totalus su Draco, che resta con 0 punti

CLUB DEI DUELLANTI
Draco: 0 punti
Harry: 20 punti
VINCE: Harry
"""


def test_il_duello_completo():
    risultato = subprocess.run(
        [sys.executable, "duello.py", "duello.csv"],
        cwd=CARTELLA,
        capture_output=True,
        text=True,
    )
    assert risultato.stdout == ATTESO
