"""Test di magazzino.py.

Ogni test scrive un file CSV di prova, lancia il programma e confronta
quello che stampa con l'output atteso, riga per riga.
Non modificate questo file: se un test diventa rosso, avete cambiato
il comportamento del programma.
"""
import subprocess
import sys
from pathlib import Path

PROGRAMMA = Path(__file__).parent / "magazzino.py"


def esegui(tmp_path, righe_csv, *argomenti):
    """Scrive il CSV in una cartella temporanea, lancia il programma e restituisce l'output."""
    file_dati = tmp_path / "magazzino.csv"
    file_dati.write_text(righe_csv, encoding="utf-8")
    risultato = subprocess.run(
        [sys.executable, str(PROGRAMMA), str(file_dati), *argomenti],
        capture_output=True,
        encoding="utf-8",
    )
    assert risultato.returncode == 0, risultato.stderr
    return risultato.stdout


def test_riordini_e_urgenze(tmp_path):
    dati = (
        'codice,prodotto,scorta,soglia,consumo_giornaliero\n'
        'P01,Viti M4,40,100,20\n'
        'P02,Bulloni M6,300,150,25\n'
        'P03,Rondelle,90,100,10\n'
        'P09,Cavi,30,50,10\n'
    )
    atteso = (
        'DA RIORDINARE\n'
        '- P01 Viti M4: scorta 40, soglia 100, ordina 160 (URGENTE: 2 giorni)\n'
        '- P03 Rondelle: scorta 90, soglia 100, ordina 110 (9 giorni)\n'
        '- P09 Cavi: scorta 30, soglia 50, ordina 70 (3 giorni)\n'
        'SCORTA SUFFICIENTE: 1 prodotti\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_ordine_arrotondato_al_lotto(tmp_path):
    dati = (
        'codice,prodotto,scorta,soglia,consumo_giornaliero\n'
        'P04,Tasselli,33,50,4\n'
    )
    atteso = (
        'DA RIORDINARE\n'
        '- P04 Tasselli: scorta 33, soglia 50, ordina 70 (8 giorni)\n'
        'SCORTA SUFFICIENTE: 0 prodotti\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_niente_da_riordinare(tmp_path):
    dati = (
        'codice,prodotto,scorta,soglia,consumo_giornaliero\n'
        'P02,Bulloni M6,300,150,25\n'
        'P07,Nastro,50,50,5\n'
    )
    atteso = (
        'DA RIORDINARE\n'
        'niente\n'
        'SCORTA SUFFICIENTE: 2 prodotti\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_righe_non_valide_ignorate(tmp_path):
    dati = (
        'codice,prodotto,scorta,soglia,consumo_giornaliero\n'
        'P05,Chiodi,tanti,50,5\n'
        'P06,Colla\n'
        'P08,Guanti,12,40,6\n'
    )
    atteso = (
        'DA RIORDINARE\n'
        '- P08 Guanti: scorta 12, soglia 40, ordina 70 (URGENTE: 2 giorni)\n'
        'SCORTA SUFFICIENTE: 0 prodotti\n'
    )
    assert esegui(tmp_path, dati) == atteso
