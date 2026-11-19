# Il magazzino di Wonka · la chiave

Il magazzino della fabbrica non lo usa una persona: lo usa il **programma del fornitore di cacao**, che chiede quanto cacao c'è. Un programma non fa il login: mostra una **chiave** (API Key) in un header, a ogni richiesta.

```
X-API-Key: 9f2c4e7a1b6d0e83c5a2f4b7d9e1c3a5
```

Il **controllore** lo scriviamo insieme, dal vivo: la funzione che sta davanti alla porta, legge l'header e decide se si entra. La rotta lo chiede con `Depends`.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `main.py` | La chiave dal `.env`, il dizionario `MAGAZZINO`, il controllore da scrivere | **Sì, solo questo** |
| `test_main.py` | I test (usano una loro chiave, non la vostra) | No |
| `.env.example` | Il modello del file `.env`, con una chiave finta | No |

## Una volta sola

Dalla cartella `giorno-10`, con il venv acceso:

```bash
cd chiave
python3 -c "import secrets; print('CHIAVE_MAGAZZINO=' + secrets.token_hex(16))" > .env
cat .env
```

Vedete `CHIAVE_MAGAZZINO=` seguito da 32 caratteri a caso? È la vostra chiave. Non si manda in chat, non va su GitHub (il `.env` è nel `.gitignore`).

Poi il server:

```bash
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

In un secondo terminale, con il venv acceso, dentro `chiave`: `pytest -v`.

## Cosa scriviamo

**Il controllore, in italiano:**

1. Arriva una richiesta: leggo l'header `X-API-Key` (il valore finisce in `chiave`, oppure `None`)
2. Manca? 401 `"Manca la chiave"`
3. È diversa da `CHIAVE_MAGAZZINO`? 401 `"Chiave sbagliata"`
4. È giusta: `return FORNITORE`, e la rotta parte

Poi `GET /magazzino` lo chiede nel def, con `fornitore: str = Depends(controlla_chiave)`, e risponde `{"fornitore": fornitore, "magazzino": MAGAZZINO}`.

## La prova

`pytest -v`: quattro verdi. Poi in Postman e su /docs.

### La chiave in Postman

1. Collezione nuova, «Giorno 10». Nelle variabili della collezione: `baseUrl` = `http://127.0.0.1:8000` e `chiave` = la vostra (quella dopo `CHIAVE_MAGAZZINO=`, da `cat .env`).
2. `GET {{baseUrl}}/magazzino` → scheda **Authorization** → Auth Type **API Key**:
   - Key: `X-API-Key`
   - Value: `{{chiave}}`
   - Add to: **Header**
3. **Send**: 200. Con **No Auth**: 401.

### La chiave su /docs

Sulla rotta, **Try it out**: c'è un campo `X-API-Key`. Scriveteci la chiave e **Execute**.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `RuntimeError: Manca CHIAVE_MAGAZZINO` | Manca il file `.env` nella cartella `chiave`: rifate il comando della chiave |
| 401 anche con la chiave giusta | In Postman, Key deve essere `X-API-Key` (con i trattini) e Add to **Header**. Nel codice: c'è `return FORNITORE` alla fine? |
| 200 anche senza chiave | Il controllore c'è, ma la rotta non lo chiede: manca `fornitore: str = Depends(controlla_chiave)` nel def |
| `NameError: controlla_chiave` | La funzione è scritta sotto la rotta che la usa: deve stare sopra |
| Il server non parte, o 401 strani, con `Depends(controlla_chiave())` | Senza parentesi: `Depends(controlla_chiave)`. La funzione la chiama FastAPI |
