# Giorno 4 · Il debugger, gli errori e i dati

| Quando | Cartella | Cosa |
|---|---|---|
| Mattina | [`DEBUG.md`](DEBUG.md) e `squadra-…/prova-debug/` | Il debugger di VS Code, passo per passo |
| Mattina | [`ERRORI.md`](ERRORI.md) | Leggere un traceback, gli errori più comuni, `try/except` |
| Mattina | `squadra-a` … `squadra-e` | **Dove è stato nascosto l'Anello?** Un'indagine a Gran Burrone, a squadre |
| Pomeriggio | `negozio/`, `giallo/` | SQL: il database degli esempi e il giallo del vagone fantasma |
| Più avanti | `progetto/` | Lo schema del vostro progetto |

## Una volta sola: il venv della squadra

Oggi il venv sta **dentro la cartella della vostra squadra**, e VS Code apre proprio quella cartella.
Così il debugger e i test trovano tutto da soli. Al posto di `a` mettete la lettera della vostra squadra.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
git switch squadra-a-anello
cd giorno-04/squadra-a
python3 -m venv .venv
source .venv/bin/activate
pip install -r ../requirements.txt
code .
```

`code .` apre VS Code in questa cartella (il punto vuol dire «qui»).
Se risponde «command not found»: aprite VS Code e fate **File → Open Folder** sulla cartella `giorno-04/squadra-a`.
Da qui in poi seguite [DEBUG.md](DEBUG.md).

Per SQL, il pomeriggio: tutto si lancia con `psql`, che avete installato il giorno 1. Se `createdb` risponde «role does not exist», rivedete il passo 5 della checklist del setup.

## L'indagine

La notte dopo il Consiglio di Elrond, l'Anello sparisce dal comodino di Frodo. Nessuno ha lasciato la valle: è ancora a Gran Burrone, nascosto da qualche parte. Le guardie elfiche hanno un registro di chi è entrato dove, e qualcuno ha scritto un programma per rimettere insieme gli indizi. Peccato che non funzioni.

Nella cartella della squadra ci sono quattro file:

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `dati.py` | Le prove: persone, testimonianze, il registro delle guardie | No |
| `indagine.py` | Il programma, diviso in 7 tappe. Ogni tappa ha un errore | **Sì, solo questo** |
| `test_indagine.py` | I test: verde = l'indizio di quella tappa è affidabile | No |
| `verifica.py` | Per dare la risposta: `python verifica.py "il luogo"` | No |

### Come si gioca

1. Lanciate `python indagine.py` (oppure **F5** in VS Code). Stampa gli indizi delle tappe che funzionano e si ferma alla prima con un errore.
2. **Prima di toccare il codice**, scrivete in un commento sopra la riga sbagliata: che errore è, su che riga, e cosa pensate che non vada.
3. Correggete **il minimo**: di solito una riga sola.
4. Provate la tappa: `pytest -v -k tappa_2` (con il numero giusto). Verde? Commit e push. Poi rilanciate: si fermerà alla tappa dopo.
5. Attenzione: **una tappa non dà nessun errore, ma mente**. Il programma va avanti tranquillo e il risultato è sbagliato. Lì serve il debugger.
6. La tappa 7 non è un errore da correggere: è codice da scrivere (`raise` e `try/except`).

Quando pensate di sapere dove è l'Anello: `python verifica.py "il luogo"`. Si può provare più volte.

### Chi sta alla tastiera

Uno condivide lo schermo e scrive, gli altri due leggono il traceback ad alta voce e decidono. A ogni tappa si cambia: chi sta alla tastiera in quale tappa è scritto in `squadra.md`.

### Il giro di Git, a ogni tappa (lo fa chi è alla tastiera)

```bash
git pull                     # prima di tutto: il lavoro di chi ha guidato prima
# correggete, poi:
pytest -v -k tappa_2
git add indagine.py
git commit -m "Tappa 2: KeyError, la chiave si chiama chi"
git push
```

Nel messaggio del commit scrivete **il tipo di errore e la causa**: alla fine la storia dei commit è il riassunto di tutti gli errori di oggi.
Oggi si fa push direttamente sul branch della squadra, niente pull request. Se il push viene rifiutato, avete dimenticato `git pull`: fatelo e riprovate.
Chi non guida, a inizio tappa fa solo `git pull`, così ha il codice aggiornato anche sul suo computer.

### Se finite prima

1. Scrivete una funzione nuova, `dove_era(nome, ora)`: dove si trovava una persona a una certa ora. `dove_era("Pipino", "01:30")` → `"Camera di Merry e Pipino"`. Scrivete prima il test.
2. Aiutate un'altra squadra, solo a voce: la tastiera resta loro.
