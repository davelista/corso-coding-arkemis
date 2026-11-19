# La fabbrica di cioccolato · il biglietto d'oro

Dopo anni di cancelli chiusi, Willy Wonka riapre la fabbrica. Ma non a tutti: entra solo chi ha il **biglietto d'oro**.

Voi siete gli Umpa Lumpa del reparto informatico, e i cancelli li costruite voi, come un'API:

1. **Registrazione.** Il bambino dà username, nome e password. La password **non** si salva: si salva la sua impronta.
2. **Il biglietto d'oro.** Al login il bambino dimostra chi è (username e password, una volta sola) e riceve un biglietto: un **token JWT** firmato da Wonka.
3. **Le sale.** Da lì in poi il bambino non ridà più la password: mostra il biglietto a ogni porta.

Il nome delle sale lo vedono tutti. Quello che c'è dentro, solo chi ha il biglietto.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `database.py` | Come stamattina: `engine`, `Base`, `get_db` (database `wonka`) | No |
| `modelli.py` | Le tabelle viste da Python: `BambinoDB` e `SalaDB` | No, si legge |
| `sicurezza.py` | Le password (`calcola_hash`, `password_giusta`), il biglietto (`crea_biglietto`), il controllore (`bambino_corrente`) | No, si legge |
| `main.py` | L'API: gli stampi, `GET /sale` già fatta, i livelli, il finale | **Sì, solo questo** |
| `test_wonka.py` | I test, sul database `wonka_test` | No |
| `wonka.sql` | Le tabelle e le cinque sale | No |
| `.env.example` | Il modello del file `.env`, con una chiave finta | No |

## Una volta sola

Dalla cartella `giorno-09`, con il venv acceso. Un comando alla volta.

```bash
cd wonka
createdb wonka
psql -d wonka -f wonka.sql
createdb wonka_test
```

Poi **la chiave segreta**, quella con cui Wonka firma i biglietti. Va nel file `.env`, che non finisce mai su GitHub (è nel `.gitignore`):

```bash
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))" > .env
cat .env
```

Vedete `SECRET_KEY=` seguito da 64 caratteri a caso? È la vostra chiave. Non si copia, non si manda in chat.

Poi il server:

```bash
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

In un secondo terminale, con il venv acceso, dentro `wonka`: `pytest -v -k livello_1`.

## I livelli

| Livello | Rotta | La cosa nuova | Risponde |
|---|---|---|---|
| 1 | `POST /bambini` | `calcola_hash`: si salva l'impronta | 201 e il Bambino, senza password |
| 2 | `POST /login` | cercare per username, `password_giusta`, `crea_biglietto` | 200 e il biglietto, oppure 401 |
| 3 | `GET /me` | `Depends(bambino_corrente)`: la rotta protetta | 200 e il Bambino, oppure 401 |
| 4 | `GET /sale/{sala_id}` | niente di nuovo: livello 1 di stamattina + livello 3 | 200 e la Sala, 401, oppure 404 |

**Obbligatori: 1, 2 e 3. Il 4 e il finale se c'è tempo.**

## Come si gioca

Come al colpo: **una tastiera sola, a turno.** Chi scrive condivide lo schermo, gli altri leggono e decidono. Si cambia a ogni livello.

Per ogni livello:

1. Scrivete il codice in `main.py`, nel posto del livello.
2. `pytest -v -k livello_N`: verde? Se è rosso, leggete il messaggio: è scritto per voi.
3. Provate la rotta **in Postman** e salvate la richiesta nella collezione «Giorno 09».

### Il login in Postman

1. `POST {{baseUrl}}/login`
2. **Body** → **raw** → **JSON**: `{"username": "charlie", "password": "cioccolato"}`, come ogni altro corpo.
3. **Scripts** → **Post-response** → questa riga, che salva il biglietto in una variabile della collezione:

   ```javascript
   pm.collectionVariables.set("biglietto", pm.response.json().access_token);
   ```

4. **Send**. Poi, nelle richieste protette: **Authorization** → **Bearer Token** → `{{biglietto}}`.

Il biglietto dura 30 minuti. Dopo: 401, e si rifà il login.

### Il login da /docs

1. `POST /login` → **Try it out**, username e password → **Execute**.
2. Copiate il valore di `access_token` (senza virgolette).
3. In alto, **Authorize** (il lucchetto): incollatelo e confermate.
4. Da qui in poi `/docs` lo manda in ogni richiesta: provate `GET /me`.

## Il finale · la ricetta

Con il biglietto, visitate le cinque sale (`GET /sale/1` … `GET /sale/5`). In ogni sala c'è un ingrediente. **La prima lettera di ogni ingrediente, in ordine di sala, è la parola segreta.**

Poi: `POST /ricetta` con il corpo `{"parola": "....."}` e il biglietto. Se la parola è giusta, la ricetta è vostra.

La parola in `main.py` non la trovate: Wonka ha salvato solo la sua impronta. Proprio come le password.

## Se finite prima · extra

1. **Username già preso:** `POST /bambini` con uno username che c'è già → 409 `"Username già preso"`. Il database dice di no (`UNIQUE`): `IntegrityError` al `db.commit()`, poi `db.rollback()` e il 409. Come l'extra di stamattina.
2. **Cambiare il proprio nome:** `PUT /me` con il corpo `{"nome": "..."}` → 200 e il Bambino aggiornato. Solo con il biglietto: il bambino da cambiare è quello del biglietto, non un id nel percorso. Serve uno stampo nuovo, `CambioNome`, con il solo campo `nome`.
3. **Dentro il biglietto:** copiate il vostro biglietto su **jwt.io** e guardate il payload. Cosa c'è scritto in `sub`? E in `exp`? (Un biglietto di prova, mai uno vero.)

I test: `pytest -v -k extra`.

## Se qualcosa non va

| Messaggio | Cosa fare |
|---|---|
| `RuntimeError: Manca SECRET_KEY` | Manca il file `.env` nella cartella `wonka`: rifate il comando della chiave |
| `database "wonka" does not exist` | `createdb wonka`, poi `psql -d wonka -f wonka.sql` |
| `database "wonka_test" does not exist` | `createdb wonka_test` |
| `/login` risponde 422 | Nel corpo manca `username` o `password`, oppure in Postman il Body non è raw → JSON |
| `/me` risponde 401 in Postman | Manca il biglietto: Authorization → Bearer Token → `{{biglietto}}`. Oppure è scaduto: rifate il login |
| `{{biglietto}}` resta rosso in Postman | La variabile non c'è: lo script del login non è partito. Controllate Scripts → Post-response, poi rifate il login |
| Il server non parte: `Invalid args for response field` | Nel `->` della rotta c'è `BambinoDB` (la tabella): deve esserci lo stampo `Bambino` |
| `500` al login | Guardate il terminale del server. Spesso: `bambino.password` invece di `bambino.password_hash` |
