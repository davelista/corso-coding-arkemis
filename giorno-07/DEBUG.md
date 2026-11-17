# Il debugger su FastAPI

Al giorno 4 il debugger fermava uno script. Oggi ferma un server: VS Code accende l'API, voi fate una richiesta da `/docs`, e il server si blocca sulla riga che avete scelto, con la richiesta ancora in mano. Lì potete guardare tutto: l'id che è arrivato, il dizionario, l'oggetto che state per restituire.

La configurazione la scrivete voi, una volta sola: poi vale per tutta la giornata.

## 0 · Cosa fa davvero `fastapi dev`

Quando scrivete `fastapi dev main.py`, in realtà accendete un altro programma, **uvicorn**, il server:

```bash
uvicorn main:app --reload
```

| Pezzo | Cosa vuol dire |
|---|---|
| `uvicorn` | Il server: resta acceso, riceve le richieste e le passa alla vostra app |
| `main:app` | Nel file `main.py`, la variabile `app`, quella di `app = FastAPI(...)` |
| `--reload` | Si riaccende da solo a ogni salvataggio |

Con il debugger cambia una cosa sola: **uvicorn non lo accende il terminale, lo accende VS Code**, con il triangolo verde. Per questo serve un file che gli dica come: il `launch.json`.

## 1 · VS Code nella cartella giusta

Dal terminale (su Windows: Ubuntu, WSL), con il venv acceso:

```bash
cd ~/corso-coding-arkemis/giorno-07
code .
```

VS Code si apre sulla cartella `giorno-07`. In basso a destra deve comparire la versione di Python **del venv** (`.venv`). Se non c'è, o è un'altra: **Ctrl+Shift+P** (su Mac **Cmd+Shift+P**) → «Python: Select Interpreter» → quello con `.venv`.

## 2 · Il file launch.json

### Cinque clic

1. Nella barra a sinistra: **Run and Debug** (l'icona del triangolo con l'insetto, oppure **Ctrl+Shift+D**).
2. Cliccate **create a launch.json file** (il link blu: c'è solo quando il file non esiste ancora).
3. Scegliete **Python Debugger**.
4. Scegliete **FastAPI**.
5. Vi chiede il percorso dell'applicazione: scrivete `main.py` e premete Invio.

VS Code crea la cartella `.vscode` e dentro il file `launch.json`, più o meno così:

```json
{
    "name": "Python Debugger: FastAPI",
    "type": "debugpy",
    "request": "launch",
    "module": "uvicorn",
    "args": ["main:app", "--reload"],
    "jinja": true
}
```

### Il file, riga per riga

| Riga | Vuol dire |
|---|---|
| `"name"` | Il nome che vedete nel menu di Run and Debug. Lo scegliete voi |
| `"type": "debugpy"` | Il debugger di Python, quello del giorno 4 |
| `"request": "launch"` | VS Code accende il programma lui (non si attacca a uno già acceso) |
| `"module": "uvicorn"` | Il programma da accendere: uvicorn, il server |
| `"args": [ … ]` | Tutto quello che scrivereste **dopo** `uvicorn` nel terminale, **un pezzo per stringa** |
| `"jinja": true` | Serve per le pagine HTML: oggi non conta, lasciatelo |

Solo due righe sono davvero nostre: `name` e `args`.

### args è la riga di comando, a pezzi

Nel terminale scrivereste:

```bash
uvicorn main:app --app-dir colpo
```

Nel `launch.json` diventa: `"module": "uvicorn"`, e il resto, pezzo per pezzo, in `args`:

```json
"args": ["main:app", "--app-dir", "colpo"]
```

| Pezzo | Vuol dire |
|---|---|
| `main` | Il file `main.py`, senza `.py` |
| `app` | La variabile `app = FastAPI(...)` dentro `main.py` |
| `--app-dir colpo` | La cartella dove sta `main.py`, insieme a `villa.py` e `cassaforte.py` che importa |

### I due ritocchi

| Ritocco | Perché |
|---|---|
| **aggiungete** `"--app-dir", "colpo"` | Avete aperto VS Code in `giorno-07`, ma `main.py` sta in `colpo`. Senza, uvicorn non lo trova: «No module named main» |
| **togliete** `"--reload"` | Con `--reload` uvicorn accende un secondo processo che riparte a ogni salvataggio, e il debugger a volte lo perde: i breakpoint non si fermano. Senza, dopo una modifica: il bottone verde **↻ Restart** |

E cambiate il nome in `"Il colpo"`. Alla fine il file deve essere così:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Il colpo",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": ["main:app", "--app-dir", "colpo"],
            "jinja": true
        }
    ]
}
```

Salvate (**Ctrl+S**). Da qui in poi il server non si accende più con `fastapi dev`, ma con il **triangolo verde** di Run and Debug.

## 3 · Il primo stop

| | Cosa fate | Cosa vedete |
|---|---|---|
| 1 | **Ctrl+C** sul terminale dove gira `fastapi dev` | Il server di prima si spegne: la porta 8000 è libera |
| 2 | In `colpo/main.py`, clic a sinistra del numero di riga, sulla prima riga dentro `leggi_ospite` | Un **pallino rosso**: il breakpoint |
| 3 | Il **triangolo verde** in alto in Run and Debug, con «Il colpo» scelto nel menu (oppure F5) | La barra in basso diventa **arancione**, e in alto compare la barra dei bottoni |
| 4 | Nel browser: **http://127.0.0.1:8000/docs** → `GET /ospiti/{ospite_id}` → Try it out → `5` → **Execute** | Il browser resta ad aspettare. È giusto |
| 5 | Guardate VS Code | La riga del pallino è **gialla**. In Variables: `ospite_id = 5` |
| 6 | **↷ Step Over** (F10), poi **▶ Continue** (F5) | Compare `ospite` in Variables; poi la risposta arriva a `/docs` |

Da qui si usa la **barra dei bottoni** che è comparsa in alto in VS Code. Passate il mouse su un bottone: compare il nome. Ogni bottone ha anche un tasto: fanno la stessa cosa, usate quello che vi viene più comodo. (Su Mac i tasti F spesso vanno premuti insieme a **fn**: con i bottoni non ci si pensa.)

| Bottone | Nome | Tasto | Cosa fa |
|---|---|---|---|
| ▶ (blu) | **Continue** | F5 | Va avanti fino al prossimo breakpoint, o fino alla fine: il browser riceve la risposta |
| ↷ (freccia che scavalca un punto) | **Step Over** | F10 | Esegue la riga e si ferma su quella dopo |
| ↓ (freccia verso un punto) | **Step Into** | F11 | Entra dentro la funzione chiamata su quella riga |
| ↑ (freccia che esce da un punto) | **Step Out** | Shift+F11 | Finisce la funzione in cui siete e torna a chi l'ha chiamata |
| ↻ (verde) | **Restart** | Ctrl+Shift+F5 (Mac: Cmd+Shift+F5) | Spegne e riaccende il server: da usare dopo ogni modifica |
| ■ (rosso) | **Stop** | Shift+F5 | Spegne il server |

Per **accendere** il debugger, invece, c'è il **triangolo verde** in alto nel pannello Run and Debug, accanto al menu con il nome della configurazione (oppure F5).

E a sinistra, mentre è fermo:

| Pannello | Cosa ci trovate |
|---|---|
| **Variables** | Tutte le variabili di quel momento: `ospite_id`, e dopo una riga `ospite`. Cliccate la freccina per aprire un oggetto e vederne i dati |
| **Watch** | Un'espressione che volete tenere d'occhio a ogni passo, per esempio `len(risultato)` |
| **Call Stack** | Chi ha chiamato chi. In cima c'è la vostra funzione, sotto tutto il lavoro di FastAPI |
| **Debug Console** (in basso) | Scrivete Python e vedete subito il risultato, con le variabili di quel momento: `ospiti[5].nome`, `len(telecamere)` |

## 4 · Le altre cartelle

Ogni cartella di oggi ha il suo `main.py`. Per ognuna, una configurazione in più nello stesso file: copiate il blocco tra `{` e `}`, mettete una virgola tra i due blocchi, cambiate `name` e la cartella dopo `--app-dir`.

```json
        {
            "name": "La talpa",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": ["main:app", "--app-dir", "talpa"],
            "jinja": true
        }
```

Lo stesso per `banda` e per `villa-db`. In Run and Debug, in alto, un menu vi fa scegliere quale accendere. Uno alla volta: la porta è sempre la 8000.

## Se qualcosa non va

| Succede | Cosa fare |
|---|---|
| `Address already in use` | C'è ancora `fastapi dev` acceso in un terminale, o un altro debugger: spegnetelo |
| `No module named uvicorn` o `fastapi` | VS Code usa il Python sbagliato: Select Interpreter → `.venv` |
| `No module named 'villa'` (o `main`) | Manca `"--app-dir", "colpo"` negli `args`, o la cartella è scritta male |
| Il pallino è vuoto, grigio | Il breakpoint è in un file che il debugger non ha avviato: controllate di aver scelto la configurazione giusta |
| `/docs` gira all'infinito | Siete fermi su un breakpoint: guardate VS Code e premete ▶ Continue |
| Ho corretto il codice ma risponde come prima | Senza `--reload` il server non si riavvia da solo: il bottone verde ↻ Restart |
