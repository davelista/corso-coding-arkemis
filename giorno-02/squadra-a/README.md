# Squadra A · Registro voti

`voti.py` legge un file CSV (`studente,materia,voto`) e calcola le medie, trova chi è insufficiente e il migliore della classe.
Funziona, ma è scritto male. Il vostro compito: renderlo professionale **senza cambiare quello che stampa**.

## Come si lancia

```bash
python voti.py esempio.csv
```

## I test

```bash
pytest -v test_voti.py
```

I test lanciano `voti.py` su alcuni file di prova e confrontano quello che stampa, riga per riga.
Se cambiate anche solo uno spazio o un decimale, diventano rossi.

## Le regole del laboratorio

- Non modificate `test_voti.py` e non rinominate `voti.py`. Potete creare altri file (moduli).
- L'output deve restare identico. Per segnalare una riga scartata usate stderr: `print("...", file=sys.stderr)`.
- Trovate un bug? Non correggetelo: segnalatelo con un commento `# BUG: ...` e scrivetelo nella descrizione della PR.
- Una regola alla volta, un commit per regola, `pytest` verde prima di ogni commit.

## Input di prova

`esempio.csv` serve per il test del collega: la squadra che leggerà il vostro codice
dovrà prevedere cosa stampa `python voti.py esempio.csv` senza eseguirlo.
