"""Test di carrello.py.

Ogni test scrive un file CSV di prova, lancia il programma e confronta
quello che stampa con l'output atteso, riga per riga.
Non modificate questo file: se un test diventa rosso, avete cambiato
il comportamento del programma.
"""
import subprocess
import sys
from pathlib import Path

PROGRAMMA = Path(__file__).parent / "carrello.py"


def esegui(tmp_path, righe_csv, *argomenti):
    """Scrive il CSV in una cartella temporanea, lancia il programma e restituisce l'output."""
    file_dati = tmp_path / "carrello.csv"
    file_dati.write_text(righe_csv, encoding="utf-8")
    risultato = subprocess.run(
        [sys.executable, str(PROGRAMMA), str(file_dati), *argomenti],
        capture_output=True,
        encoding="utf-8",
    )
    assert risultato.returncode == 0, risultato.stderr
    return risultato.stdout


def test_senza_codice(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'quaderno,2.50,2\n'
        'penna,1.20,3\n'
        'zaino,24.90,1\n'
    )
    atteso = (
        'CARRELLO\n'
        'quaderno x2: 5.00\n'
        'penna x3: 3.24 (-10%)\n'
        'zaino x1: 24.90\n'
        'Subtotale: 33.14\n'
        'Spedizione: 4.90\n'
        'Totale: 38.04\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_codice_benvenuto(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'quaderno,2.50,2\n'
        'penna,1.20,3\n'
        'zaino,24.90,1\n'
    )
    atteso = (
        'CARRELLO\n'
        'quaderno x2: 5.00\n'
        'penna x3: 3.24 (-10%)\n'
        'zaino x1: 24.90\n'
        'Subtotale: 33.14\n'
        'Codice BENVENUTO: -5.00\n'
        'Spedizione: 4.90\n'
        'Totale: 33.04\n'
    )
    assert esegui(tmp_path, dati, 'BENVENUTO') == atteso


def test_benvenuto_sotto_la_soglia(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'gomma,0.80,2\n'
        'matita,0.50,4\n'
    )
    atteso = (
        'CARRELLO\n'
        'gomma x2: 1.60\n'
        'matita x4: 1.80 (-10%)\n'
        'Subtotale: 3.40\n'
        'Codice BENVENUTO: serve una spesa di almeno 30.00\n'
        'Spedizione: 4.90\n'
        'Totale: 8.30\n'
    )
    assert esegui(tmp_path, dati, 'BENVENUTO') == atteso


def test_sconto10_e_spedizione_gratis(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'cuffie,59.90,1\n'
        'cavo,6.00,3\n'
    )
    atteso = (
        'CARRELLO\n'
        'cuffie x1: 59.90\n'
        'cavo x3: 16.20 (-10%)\n'
        'Subtotale: 76.10\n'
        'Codice SCONTO10: -7.61\n'
        'Spedizione: 0.00\n'
        'Totale: 68.49\n'
    )
    assert esegui(tmp_path, dati, 'SCONTO10') == atteso


def test_sconto10_sotto_la_soglia(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'astuccio,8.00,1\n'
        'colla,1.50,2\n'
    )
    atteso = (
        'CARRELLO\n'
        'astuccio x1: 8.00\n'
        'colla x2: 3.00\n'
        'Subtotale: 11.00\n'
        'Codice SCONTO10: serve una spesa di almeno 40.00\n'
        'Spedizione: 4.90\n'
        'Totale: 15.90\n'
    )
    assert esegui(tmp_path, dati, 'SCONTO10') == atteso


def test_codice_sconosciuto_e_righe_non_valide(tmp_path):
    dati = (
        'prodotto,prezzo,quantita\n'
        'libro,abc,1\n'
        'righello,1.50\n'
        'astuccio,8.00,1\n'
    )
    atteso = (
        'CARRELLO\n'
        'astuccio x1: 8.00\n'
        'Subtotale: 8.00\n'
        'Codice ESTATE sconosciuto\n'
        'Spedizione: 4.90\n'
        'Totale: 12.90\n'
    )
    assert esegui(tmp_path, dati, 'ESTATE') == atteso
