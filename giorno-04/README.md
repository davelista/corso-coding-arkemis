# Giorno 4 · Il debugger, gli errori e i dati

| Quando | Cartella | Cosa |
|---|---|---|
| Mattina | [`DEBUG.md`](DEBUG.md) e `squadra-…/prova-debug/` | Il debugger di VS Code, passo per passo |
| Mattina | [`ERRORI.md`](ERRORI.md) | Leggere un traceback, gli errori più comuni, `try/except` |
| Mattina | `squadra-a` … `squadra-e` | **Dove è stato nascosto l'Anello?** Un'indagine a Gran Burrone, a squadre |
| Pomeriggio | `negozio/` | SQL: il database degli esempi |
| Pomeriggio | [`BIGINO-SQL.md`](BIGINO-SQL.md) | Tutto SQL in una pagina: SELECT, WHERE, JOIN (con i disegni), GROUP BY, gli errori |
| Giorno 5 | [`../giorno-05`](../giorno-05/README.md) | Il giallo del vagone fantasma, gli esercizi dei pirati e il vostro progetto |

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

### Le regole

1. **Si tocca solo `indagine.py`.** `dati.py`, `test_indagine.py` e `verifica.py` no. Se li modificate per sbaglio: `git restore nome-del-file`.
2. **Una tastiera sola, a turno.** Chi è alla tastiera condivide lo schermo e scrive; si cambia a ogni tappa, l'ordine è in `squadra.md`. Parte chi si sente meno sicuro: chi è più forte detta, non scrive.
3. **Prima si legge, poi si tocca.** Sopra la riga sbagliata, un commento: che errore è, su che riga, cosa pensate che non vada.
4. **Una tappa alla volta, in ordine.** Si corregge il minimo, di solito una riga sola.
5. **Tappa verde, poi commit e push.** `pytest -v -k tappa_N`. Nel messaggio: il tipo di errore e la causa.
6. **A inizio tappa, tutti e tre: `git pull`.** Push diretto sul branch della squadra, niente pull request.
7. **Bloccati da 15 minuti sulla stessa tappa?** Scrivete nel canale delle domande: la tappa, l'ultima riga del traceback, cosa avete provato.
8. **Quando `verifica.py` dice ESATTO:** il luogo in `squadra.md`, commit «Caso chiuso» e push. Alle altre squadre si danno solo aiuti a voce: **il luogo non si dice**.

Orari: 11:20 – 13:00, pausa 12:10 – 12:20. Qui sotto, ogni regola spiegata per bene.

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
git pull                     # prima di tutto: il lavoro di chi c'era prima
# correggete, poi:
pytest -v -k tappa_2
git add indagine.py
git commit -m "Tappa 2: KeyError, la chiave si chiama chi"
git push
```

Nel messaggio del commit scrivete **il tipo di errore e la causa**: alla fine la storia dei commit è il riassunto di tutti gli errori di oggi.
Oggi si fa push direttamente sul branch della squadra, niente pull request. Se il push viene rifiutato, avete dimenticato `git pull`: fatelo e riprovate.
Chi non è alla tastiera, a inizio tappa fa solo `git pull`, così ha il codice aggiornato anche sul suo computer.

### Se finite prima

1. Scrivete una funzione nuova, `dove_era(nome, ora)`: dove si trovava una persona a una certa ora. `dove_era("Pipino", "01:30")` → `"Camera di Merry e Pipino"`. Scrivete prima il test.
2. Aiutate un'altra squadra, solo a voce: la tastiera resta loro.
