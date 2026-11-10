"""Tappa 6 · Il programma completo. Non si modifica.

Funziona quando i tre pezzi (leggi.py, calcola.py, stampa.py) sono tutti su main:
    python report.py spese.csv
"""

import sys

from calcola import totali_per_categoria
from leggi import leggi_spese
from stampa import formatta_report


def main() -> None:
    if len(sys.argv) != 2:
        print("Uso: python report.py spese.csv", file=sys.stderr)
        sys.exit(1)
    spese = leggi_spese(sys.argv[1])
    totali = totali_per_categoria(spese)
    print(formatta_report(totali))


if __name__ == "__main__":
    main()
