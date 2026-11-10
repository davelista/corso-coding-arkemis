"""Test di meteo.py.

Ogni test scrive un file CSV di prova, lancia il programma e confronta
quello che stampa con l'output atteso, riga per riga.
Non modificate questo file: se un test diventa rosso, avete cambiato
il comportamento del programma.
"""
import subprocess
import sys
from pathlib import Path

PROGRAMMA = Path(__file__).parent / "meteo.py"


def esegui(tmp_path, righe_csv, *argomenti):
    """Scrive il CSV in una cartella temporanea, lancia il programma e restituisce l'output."""
    file_dati = tmp_path / "meteo.csv"
    file_dati.write_text(righe_csv, encoding="utf-8")
    risultato = subprocess.run(
        [sys.executable, str(PROGRAMMA), str(file_dati), *argomenti],
        capture_output=True,
        encoding="utf-8",
    )
    assert risultato.returncode == 0, risultato.stderr
    return risultato.stdout


def test_una_citta(tmp_path):
    dati = (
        'data,citta,minima,massima\n'
        '2026-01-10,Milano,-2.0,6.5\n'
        '2026-01-11,Milano,0.5,8.0\n'
        '2026-01-12,Milano,-3.5,4.0\n'
        '2026-01-13,Milano,-3.5,5.0\n'
    )
    atteso = (
        'MILANO\n'
        '  minima: -3.5 il 2026-01-12\n'
        '  massima: 8.0 il 2026-01-11\n'
        '  escursione media: 8.0\n'
        'GIORNATE ANOMALE\n'
        'nessuna\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_citta_in_ordine_e_anomalie(tmp_path):
    dati = (
        'data,citta,minima,massima\n'
        '2026-07-12,Torino,12.0,29.0\n'
        '2026-07-12,Palermo,24.0,38.5\n'
        '2026-07-12,Roma,20.0,30.0\n'
        '2026-07-11,Roma,19.0,31.0\n'
    )
    atteso = (
        'PALERMO\n'
        '  minima: 24.0 il 2026-07-12\n'
        '  massima: 38.5 il 2026-07-12\n'
        '  escursione media: 14.5\n'
        'ROMA\n'
        '  minima: 19.0 il 2026-07-11\n'
        '  massima: 31.0 il 2026-07-11\n'
        '  escursione media: 11.0\n'
        'TORINO\n'
        '  minima: 12.0 il 2026-07-12\n'
        '  massima: 29.0 il 2026-07-12\n'
        '  escursione media: 17.0\n'
        'GIORNATE ANOMALE\n'
        '- 2026-07-12 Palermo: min 24.0, max 38.5\n'
        '- 2026-07-12 Torino: min 12.0, max 29.0\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_dati_non_validi_ignorati(tmp_path):
    dati = (
        'data,citta,minima,massima\n'
        '2026-02-01,Napoli,n/d,12.0\n'
        '2026-02-02,Napoli,8.0,5.0\n'
        '2026-02-03,Napoli,6.0,13.0\n'
        '2026-02-04,Napoli\n'
    )
    atteso = (
        'NAPOLI\n'
        '  minima: 6.0 il 2026-02-03\n'
        '  massima: 13.0 il 2026-02-03\n'
        '  escursione media: 7.0\n'
        'GIORNATE ANOMALE\n'
        'nessuna\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_soglie_esatte(tmp_path):
    dati = (
        'data,citta,minima,massima\n'
        '2026-08-01,Bari,19.0,34.0\n'
        '2026-08-02,Bari,20.0,35.0\n'
        '2026-08-03,Bari,10.0,25.0\n'
    )
    atteso = (
        'BARI\n'
        '  minima: 10.0 il 2026-08-03\n'
        '  massima: 35.0 il 2026-08-02\n'
        '  escursione media: 15.0\n'
        'GIORNATE ANOMALE\n'
        '- 2026-08-02 Bari: min 20.0, max 35.0\n'
    )
    assert esegui(tmp_path, dati) == atteso
