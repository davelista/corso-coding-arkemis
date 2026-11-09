"""Test di voti.py.

Ogni test scrive un file CSV di prova, lancia il programma e confronta
quello che stampa con l'output atteso, riga per riga.
Non modificate questo file: se un test diventa rosso, avete cambiato
il comportamento del programma.
"""
import subprocess
import sys
from pathlib import Path

PROGRAMMA = Path(__file__).parent / "voti.py"


def esegui(tmp_path, righe_csv, *argomenti):
    """Scrive il CSV in una cartella temporanea, lancia il programma e restituisce l'output."""
    file_dati = tmp_path / "voti.csv"
    file_dati.write_text(righe_csv, encoding="utf-8")
    risultato = subprocess.run(
        [sys.executable, str(PROGRAMMA), str(file_dati), *argomenti],
        capture_output=True,
        encoding="utf-8",
    )
    assert risultato.returncode == 0, risultato.stderr
    return risultato.stdout


def test_medie_e_migliore(tmp_path):
    dati = (
        'studente,materia,voto\n'
        'anna,matematica,8\n'
        'anna,storia,7.5\n'
        'bruno,matematica,6\n'
        'bruno,storia,6.5\n'
        'carla,matematica,9\n'
        'carla,storia,8\n'
        'carla,inglese,10\n'
    )
    atteso = (
        'MEDIE\n'
        'anna: 7.75 (2 voti)\n'
        'bruno: 6.25 (2 voti)\n'
        'carla: 9.0 (3 voti)\n'
        'INSUFFICIENTI\n'
        'nessuno\n'
        'MIGLIORE\n'
        'carla 9.0\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_insufficienti(tmp_path):
    dati = (
        'studente,materia,voto\n'
        'dario,matematica,5\n'
        'dario,storia,4\n'
        'elena,matematica,6\n'
        'elena,storia,5\n'
        'franco,inglese,7\n'
    )
    atteso = (
        'MEDIE\n'
        'dario: 4.5 (2 voti)\n'
        'elena: 5.5 (2 voti)\n'
        'franco: 7.0 (1 voti)\n'
        'INSUFFICIENTI\n'
        '- dario 4.5\n'
        '- elena 5.5\n'
        'MIGLIORE\n'
        'franco 7.0\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_voti_non_validi_ignorati(tmp_path):
    dati = (
        'studente,materia,voto\n'
        'gino,matematica,8\n'
        'gino,storia,assente\n'
        'gino,inglese,11\n'
        'gino,arte,0\n'
        'gino,musica,6\n'
    )
    atteso = (
        'MEDIE\n'
        'gino: 7.0 (2 voti)\n'
        'INSUFFICIENTI\n'
        'nessuno\n'
        'MIGLIORE\n'
        'gino 7.0\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_media_lista_vuota(tmp_path):
    dati = (
        'studente,materia,voto\n'
        'luca,storia,assente\n'
        'luca,matematica,12\n'
        'marta,storia,7\n'
    )
    atteso = (
        'MEDIE\n'
        'luca: n.d.\n'
        'marta: 7.0 (1 voti)\n'
        'INSUFFICIENTI\n'
        'nessuno\n'
        'MIGLIORE\n'
        'marta 7.0\n'
    )
    assert esegui(tmp_path, dati) == atteso


def test_pareggio_vince_ordine_alfabetico(tmp_path):
    dati = (
        'studente,materia,voto\n'
        'nadia,storia,8\n'
        'anna,storia,8\n'
        'zeno,storia,3\n'
    )
    atteso = (
        'MEDIE\n'
        'anna: 8.0 (1 voti)\n'
        'nadia: 8.0 (1 voti)\n'
        'zeno: 3.0 (1 voti)\n'
        'INSUFFICIENTI\n'
        '- zeno 3.0\n'
        'MIGLIORE\n'
        'anna 8.0\n'
    )
    assert esegui(tmp_path, dati) == atteso
