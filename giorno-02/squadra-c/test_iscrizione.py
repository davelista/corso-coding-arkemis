"""Test di iscrizione.py.

Ogni test scrive un file CSV di prova, lancia il programma e confronta
quello che stampa con l'output atteso, riga per riga.
Non modificate questo file: se un test diventa rosso, avete cambiato
il comportamento del programma.
"""
import subprocess
import sys
from pathlib import Path

PROGRAMMA = Path(__file__).parent / "iscrizione.py"


def esegui(tmp_path, righe_csv, *argomenti):
    """Scrive il CSV in una cartella temporanea, lancia il programma e restituisce l'output."""
    file_dati = tmp_path / "utenti.csv"
    file_dati.write_text(righe_csv, encoding="utf-8")
    risultato = subprocess.run(
        [sys.executable, str(PROGRAMMA), str(file_dati), *argomenti],
        capture_output=True,
        encoding="utf-8",
    )
    assert risultato.returncode == 0, risultato.stderr
    return risultato.stdout


def test_utenti_validi(tmp_path):
    dati = (
        'username,email,password\n'
        'mario_rossi,mario@example.com,girasole42\n'
        'lucia,lucia.b@mail.it,montagna2026\n'
    )
    atteso = (
        'riga 2 mario_rossi: OK\n'
        'riga 3 lucia: OK\n'
        'Iscritti: 2 su 2\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_errori_username(tmp_path):
    dati = (
        'username,email,password\n'
        'al,al@mail.it,password12\n'
        'questo_nome_e_lunghissimo,q@mail.it,password12\n'
        'anna-b,anna@mail.it,password12\n'
    )
    atteso = (
        'riga 2 al: username troppo corto\n'
        'riga 3 questo_nome_e_lunghissimo: username troppo lungo\n'
        'riga 4 anna-b: username con caratteri non ammessi\n'
        'Iscritti: 0 su 3\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_errori_email(tmp_path):
    dati = (
        'username,email,password\n'
        'piero,pieromail.it,password12\n'
        'paola,paola@mail,password12\n'
        'franco,franco@@mail.it,password12\n'
    )
    atteso = (
        'riga 2 piero: email non valida\n'
        'riga 3 paola: email non valida\n'
        'riga 4 franco: email non valida\n'
        'Iscritti: 0 su 3\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_errori_password(tmp_path):
    dati = (
        'username,email,password\n'
        'sara,sara@mail.it,corta1\n'
        'rita,rita@mail.it,lunghissima\n'
        'tommaso,tommaso@mail.it,tommaso123\n'
    )
    atteso = (
        'riga 2 sara: password troppo corta\n'
        'riga 3 rita: password senza numeri\n'
        'riga 4 tommaso: password contiene lo username\n'
        'Iscritti: 0 su 3\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_piu_errori_nella_stessa_riga(tmp_path):
    dati = (
        'username,email,password\n'
        'al,al.it,abc\n'
    )
    atteso = (
        'riga 2 al: username troppo corto; email non valida; password troppo corta; password senza numeri\n'
        'Iscritti: 0 su 1\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_username_gia_usato_e_righe_non_valide(tmp_path):
    dati = (
        'username,email,password\n'
        'Giulia,giulia@mail.it,sole12345\n'
        'riga,con,troppi,campi\n'
        'GIULIA,giulia2@mail.it,luna12345\n'
        'solo_due,campi\n'
    )
    atteso = (
        'riga 2 Giulia: OK\n'
        'riga 4 GIULIA: username già usato\n'
        'Iscritti: 1 su 2\n'
    )
    assert esegui(tmp_path, dati) == atteso
