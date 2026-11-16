# L'API della flotta

Port Royal, 1732. La Compagnia delle Indie si è stancata del diario di bordo di carta: vuole sapere **in ogni momento** dove sono le navi, chi le comanda e quanti cannoni hanno. Ha chiesto un'API. Il lavoro è vostro.

Venerdì il diario l'avete interrogato con SQL. Oggi le stesse navi stanno **in memoria**, in un dizionario Python. Domani, nella stessa API, il dizionario lascia il posto al database `pirati`, e le vostre query finiscono dentro le rotte.

## Prima di tutto

Dalla cartella `giorno-06`, con il venv acceso (vedi il README del giorno):

```bash
cd flotta
fastapi dev main.py      # poi aprite http://127.0.0.1:8000/docs
```

In un **secondo terminale**, sempre con il venv acceso:

```bash
cd ~/corso-coding-arkemis/giorno-06/flotta
pytest -v
```

All'inizio molti test sono rossi: è giusto così. Ognuno diventa verde quando la rotta che controlla funziona.

## Com'è fatta l'API

| Verbo e percorso | Cosa fa | Risponde | Stato |
|---|---|---|---|
| `GET /navi` | Tutta la flotta | 200 e una lista | ✅ già fatta |
| `GET /navi/{id}` | Una nave | 200, oppure 404 `"Nave non trovata"` | ✅ già fatta |
| `POST /navi` | Una nave nuova | 201 con la nave e il suo id | ✅ già fatta |
| `PUT /navi/{id}` | Cambia una nave | 200 con la nave aggiornata, oppure 404 | ⬜ **obbligatorio** |
| `DELETE /navi/{id}` | Affonda una nave | 204 senza corpo, oppure 404 | ⬜ **obbligatorio** |

Una nave è fatta così (sono le colonne della tabella `navi` di venerdì):

```json
{
  "id": 1,
  "nome": "Perla Nera",
  "capitano": "Jack Sparrow",
  "bandiera": "pirata",
  "cannoni": 32,
  "porto_base": "Tortuga"
}
```

`bandiera` può essere solo `pirata`, `Marina`, `Compagnia delle Indie` o `mercantile`. `porto_base` può essere `null`: l'Olandese Volante non torna mai in porto.

## Il laboratorio · a gruppi

I test in `test_main.py` sono già scritti: **non si toccano**. Si lavora su `main.py` finché diventano verdi.

**Obbligatorio**
1. `PUT /navi/{nave_id}`: sostituisce la nave con i dati nuovi, risponde 200 con la nave aggiornata, 404 `"Nave non trovata"` se non esiste.
2. `DELETE /navi/{nave_id}`: risponde 204 senza corpo, 404 `"Nave non trovata"` se non esiste.

**Extra**
3. `POST` con un nome già usato: 409 `"Nome già usato"`. Anche nella `PUT`, se il nome è di un'**altra** nave. Il proprio nome, invece, si può tenere.
4. `GET /navi?bandiera=Marina`: solo le navi con quella bandiera.
5. `GET /navi?min_cannoni=40`: solo le navi con almeno quei cannoni. E i due filtri insieme.

Chi scrive cambia a ogni test che diventa verde. Ogni test verde, un commit sul branch del gruppo.

## Quando un test è rosso

| Il test dice | Vuol dire |
|---|---|
| `405` invece di 200 o 204 | La rotta esiste, ma non con quel verbo: manca la funzione con `@app.put` o `@app.delete` |
| `404` invece di 200 | La funzione c'è, ma non trova la nave: controllate l'id e il dizionario `flotta` |
| `200` invece di 404 | Manca il controllo: la nave che non esiste va cercata con `trova` |
| `422` | Pydantic ha rifiutato i dati: leggete il dettaglio nella risposta, dice quale campo non va |

E provate tutto anche da `/docs`: **Try it out**, poi **Execute**. Quello che vedete lì è esattamente quello che vede il test.
