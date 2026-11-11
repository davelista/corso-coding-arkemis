"""Tappa 6 · Il duello completo. Non si modifica.

Funziona quando i tre pezzi (leggi.py, incantesimi.py, annuncio.py)
sono tutti sul branch della squadra:
    python duello.py duello.csv
"""

import sys

from annuncio import annuncia
from incantesimi import lancia
from leggi import leggi_mosse

PUNTI_INIZIALI = 50


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: python duello.py duello.csv", file=sys.stderr)
        sys.exit(1)
    mosse = leggi_mosse(sys.argv[1])
    punti = {}
    for mossa in mosse:
        mago = mossa["mago"]
        bersaglio = mossa["bersaglio"]
        for nome in (mago, bersaglio):
            if nome not in punti:
                punti[nome] = PUNTI_INIZIALI
        punti[bersaglio] = lancia(mossa["incantesimo"], punti[bersaglio])
        print(
            f"Turno {mossa['turno']}: {mago} lancia {mossa['incantesimo']} su {bersaglio}, "
            f"che resta con {punti[bersaglio]} punti"
        )
    print()
    print(annuncia(punti))


if __name__ == "__main__":
    main()
