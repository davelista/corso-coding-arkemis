# La lampada di Agrabah

> **Da zero.** `main.py` e `sicurezza.py` sono vuoti: import, stampi, rotte e funzioni li scrivete voi. Le avete già scritte tutte, con altri nomi, tra giovedì e venerdì: riaprire il vostro codice va benissimo. Copiarlo senza rileggerlo no: qui i nomi sono diversi.

Agrabah è una città con quattro porte, e ogni porta si apre in un modo diverso.

1. **Il bazar.** I tesori sono in vetrina: chiunque li guarda, senza mostrare niente a nessuno.
2. **La Caverna.** Per mettere, cambiare o togliere un tesoro serve la **chiave della Caverna**, in un header.
3. **La lampada.** Vi registrate, fate login, e la lampada vi dà un **token**. Da lì in poi mostrate quello.
4. **I desideri.** Ogni padrone esprime e vede solo i suoi. E sono tre, non uno di più.

Voi costruite le porte, come un'API. Un livello alla volta.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `agrabah.sql` | Le tre tabelle (`tesori`, `padroni`, `desideri`) e sei tesori già nel bazar | No |
| `database.py` | Come nella villa: `engine`, `Base`, `get_db`, sul database `agrabah` | No |
| `modelli.py` | `TesoroDB` è già scritto, da esempio. `PadroneDB` e `DesiderioDB` li scrivete voi | **Sì** |
| `sicurezza.py` | Vuoto. La chiave, le password, il token, il controllore: tutto vostro | **Sì** |
| `main.py` | Solo `app = FastAPI()`. Gli stampi e le rotte li scrivete voi | **Sì** |
| `test_agrabah.py` | I test dei livelli, sul database `agrabah_test` | No |
| `.env.example` | Il modello del file `.env`: `SECRET_KEY` e `CHIAVE_CAVERNA` | No |

## Livello 0 · Una volta sola

Dalla cartella `giorno-11`. Un comando alla volta.

```bash
python3 --version            # deve dire 3.12 o più
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd agrabah
createdb agrabah
psql -d agrabah -f agrabah.sql
createdb agrabah_test
```

Poi **le due chiavi**: quella della Caverna, e quella con cui si firmano i token. Vanno nel file `.env`, che non finisce mai su GitHub (è nel `.gitignore`):

```bash
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32)); print('CHIAVE_CAVERNA=' + secrets.token_hex(16))" > .env
cat .env
```

Vedete due righe, `SECRET_KEY=` e `CHIAVE_CAVERNA=`, ognuna seguita da caratteri a caso? Sono le vostre chiavi. Non si copiano, non si mandano in chat.

Poi il server:

```bash
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

**La prima rotta:** `GET /` risponde `{"citta": "Agrabah"}`. Scrivetela in `main.py`. In un secondo terminale, con il venv acceso, dentro `agrabah`:

```bash
pytest -v -k livello_0
```

Verde? La città c'è: si parte dal bazar.

## Da dove ripartire

| Vi serve | L'avete fatto in | Quando |
|---|---|---|
| Le rotte sul database: `select`, `db.get`, `add`, `commit` | `giorno-09/villa-orm/main.py` | giovedì |
| Il controllore delle chiavi, con `Header` e `Depends` | `giorno-10/chiave/main.py` | venerdì |
| Le password: `calcola_hash`, `password_giusta` | `giorno-10/insieme/password.py` | venerdì |
| Creare il token, e leggerlo | `giorno-10/insieme/biglietto.py` | venerdì |
| Il controllore del token, con `Depends` | `giorno-10/wonka-fondente/sicurezza.py` | venerdì |

## Come si gioca

- **Una tastiera sola, a turno.** Chi scrive condivide lo schermo, gli altri leggono e decidono. Si cambia a ogni livello.
- **Un livello è finito quando è verde:** `pytest -v -k livello_N`. Poi la stessa richiesta in Postman, salvata in una collezione «Agrabah».
- **Un test è rosso?** Leggete l'ultima riga del messaggio: è scritta per voi.
- **Bloccati da più di 10 minuti?** Prima questo README e il vostro codice di venerdì, poi il forum su Discord.
- **Davide passa due volte**, alle 10:35 e alle 11:30: tenete pronta una domanda a gruppo, quella che vi sblocca di più.

**Obiettivo: livello 4 verde entro le 12:35.** Il 5 e il 6 sono per chi corre.

## I livelli, in una pagina

| Livello | La storia | Cosa costruite | La prova |
|---|---|---|---|
| 0 | Arrivo ad Agrabah | Il setup, e `GET /` | `pytest -v -k livello_0` |
| 1 | Il bazar | Le cinque rotte dei tesori, con i filtri | `pytest -v -k livello_1` |
| 2 | La Caverna | `X-API-Key` su POST, PUT e DELETE | `pytest -v -k livello_2` |
| 3 | Chi sei? | `POST /padroni`: la registrazione, con l'impronta | `pytest -v -k livello_3` |
| **4** | **La lampada** | **`POST /login`, il token, `GET /me`** | `pytest -v -k livello_4` |
| 5 | Tre desideri | I desideri: solo i tuoi, al massimo tre | `pytest -v -k livello_5` |
| 6 | Le regole del Genio | Desideri vietati, e il ruolo genio | `pytest -v -k livello_6` |

## Livello 1 · Il bazar

Nel bazar i tesori sono in vetrina. Per ora chiunque può guardarli, aggiungerli, cambiarli e toglierli: le porte arrivano dopo.

| Rotta | Cosa fa | Se va bene | Se va male |
|---|---|---|---|
| `GET /tesori` | Tutti i tesori, in ordine di id. Due filtri facoltativi: `?valore_min=` e `?maledetto=` | 200 e la lista | |
| `GET /tesori/{tesoro_id}` | Un tesoro solo | 200 e il tesoro | 404 `"Tesoro non trovato"` |
| `POST /tesori` | Un tesoro nuovo. Corpo: `nome`, `valore`, `maledetto` | 201 e il tesoro, con l'id | 422: ci pensa Pydantic |
| `PUT /tesori/{tesoro_id}` | Cambia tutto il tesoro: stesso corpo della POST | 200 e il tesoro | 404 `"Tesoro non trovato"` |
| `DELETE /tesori/{tesoro_id}` | Toglie il tesoro dal bazar | 204, senza corpo | 404 `"Tesoro non trovato"` |

I dettagli, tutti:

- **Due stampi.** `TesoroNuovo`: `nome` (testo, non vuoto), `valore` (numero intero, da 0 in su), `maledetto` (vero o falso: se manca nel corpo, vale `False`). `Tesoro`: lo stesso, con in più `id`.
- **I filtri** sono query params, tutti e due facoltativi. `?valore_min=500`: solo i tesori che valgono 500 o più. `?maledetto=true`: solo i maledetti. `?maledetto=false`: solo quelli sicuri. Insieme: valgono tutti e due.
- **Attenti a `False`:** `maledetto=false` è un filtro vero. «Il filtro non c'è» è `None`.
- I test di questo livello mandano già l'header `X-API-Key`: per ora ignoratelo, serve al livello 2.

## Livello 2 · La Caverna

I tesori veri stanno nella Caverna delle Meraviglie, e la Caverna non fa entrare chiunque: guardare sì, toccare solo con la chiave.

| Rotta | Cosa cambia | Se va bene | Se va male |
|---|---|---|---|
| `POST /tesori` | Solo con l'header `X-API-Key` giusto | 201 e il tesoro | 401 `"Manca la chiave"` · 401 `"Chiave sbagliata"` |
| `PUT /tesori/{tesoro_id}` | Solo con la chiave | 200 e il tesoro | gli stessi due 401, poi il 404 |
| `DELETE /tesori/{tesoro_id}` | Solo con la chiave | 204 | gli stessi due 401, poi il 404 |
| `GET /tesori` · `GET /tesori/{tesoro_id}` | Niente: restano aperte a tutti | 200 | come al livello 1 |

I dettagli:

- La chiave giusta sta nel `.env`, alla riga `CHIAVE_CAVERNA`. In `sicurezza.py`: `load_dotenv`, poi `os.environ.get("CHIAVE_CAVERNA")`. **Mai scritta nel codice.**
- Il controllore si chiama `controlla_chiave`, è una funzione sola, sta in `sicurezza.py`, e si usa con `Depends` nelle tre rotte che scrivono.
- Se l'header non c'è: 401 `"Manca la chiave"`. Se c'è ma è diversa: 401 `"Chiave sbagliata"`.
- In Postman: scheda **Headers**, chiave `X-API-Key`, valore quello del vostro `.env`.

## Livello 3 · Chi sei?

La lampada non si dà a uno sconosciuto. Chi la vuole si registra: e della sua password, nel database, resta solo l'impronta.

| Rotta | Cosa fa | Se va bene | Se va male |
|---|---|---|---|
| `POST /padroni` | Registra un padrone. Corpo: `username`, `nome`, `password` | 201: `id`, `username`, `nome` | 409 `"Username già preso"` · 422: ci pensa Pydantic |

Da scrivere, nell'ordine:

1. **`modelli.py`:** `PadroneDB`, la tabella `padroni` vista da Python. Guardate le colonne in `agrabah.sql`, e `TesoroDB` come esempio. La colonna `ruolo` per ora lasciatela fuori.
2. **`sicurezza.py`:** `calcola_hash(password)` e `password_giusta(password, impronta)`, con `pwdlib`.
3. **`main.py`:** due stampi, poi la rotta.
   - `PadroneNuovo`: `username` (da 3 a 30 caratteri), `nome` (non vuoto), `password` (almeno 8 caratteri).
   - `Padrone`: `id`, `username`, `nome`. **Niente password, niente impronta. Mai.**
4. **Lo username doppio** lo rifiuta il database (`UNIQUE`): al `db.commit()` arriva `IntegrityError` (si importa da `sqlalchemy.exc`). Allora `db.rollback()`, e poi il 409.

## Livello 4 · La lampada

Con username e password, una volta sola, la lampada vi dà un token. Da lì in poi alle porte mostrate quello, non la password.

| Rotta | Cosa fa | Se va bene | Se va male |
|---|---|---|---|
| `POST /login` | Corpo in JSON: `username` e `password` | 200: `access_token`, e `token_type` che vale `"bearer"` | 401 `"Username o password sbagliati"` |
| `GET /me` | Chi sono? Solo con il token, nell'header `Authorization: Bearer …` | 200: `id`, `username`, `nome` | 401 `"Manca il token"` · 401 `"Token non valido"` |

I dettagli:

- In `sicurezza.py`: `crea_token(padrone_id)`. Dentro il token due cose: `"sub"`, l'id del padrone **scritto come testo**, e `"exp"`, adesso (in UTC) più 30 minuti. Si firma con la `SECRET_KEY` del `.env`, algoritmo `HS256`.
- In `sicurezza.py`: `padrone_corrente`, il controllore del token, da usare con `Depends`. Niente token: 401 `"Manca il token"`. Token falso, scaduto, o di un padrone che non c'è più: 401 `"Token non valido"`.
- Al login, username che non esiste e password sbagliata danno **lo stesso** 401: non si dice quale dei due.
- Due stampi nuovi: `Credenziali` (`username`, `password`) e `Token` (`access_token`, `token_type`).

### Il login in Postman

1. `POST {{baseUrl}}/login`, **Body** → **raw** → **JSON**: `{"username": "aladdin", "password": "tappeto-volante"}`
2. **Scripts** → **Post-response** → questa riga, che salva il token in una variabile della collezione:

   ```javascript
   pm.collectionVariables.set("token", pm.response.json().access_token);
   ```

3. **Send**. Poi, nelle richieste protette: **Authorization** → **Bearer Token** → `{{token}}`.

Il token dura 30 minuti. Dopo: 401, e si rifà il login.

## Livello 5 · Tre desideri (extra)

Tre desideri a testa, non uno di più. E ognuno vede solo i suoi: quelli degli altri, per lui, non esistono.

| Rotta | Cosa fa | Se va bene | Se va male |
|---|---|---|---|
| `POST /desideri` | Esprime un desiderio. Corpo: `testo` (almeno 3 caratteri) | 201: `id`, `testo`, `esaudito` che vale `false` | 403 `"Hai finito i desideri"`, al quarto · 401 |
| `GET /desideri` | I miei desideri: solo i miei, in ordine di id | 200 e la lista | 401 |
| `DELETE /desideri/{desiderio_id}` | Ritira un mio desiderio | 204 | 404 `"Desiderio non trovato"`, anche se è di un altro · 401 |

I dettagli:

- Prima serve `DesiderioDB` in `modelli.py`: gli indizi sono lì.
- **Di chi è il desiderio?** Non arriva dal corpo né dal percorso: è il padrone del token. `padrone_id` lo mettete voi.
- Due stampi: `DesiderioNuovo` (`testo`) e `Desiderio` (`id`, `testo`, `esaudito`).
- Tre a testa: i desideri degli altri non consumano i vostri.

## Livello 6 · Le regole del Genio (extra)

Anche il Genio ha le sue regole: non si chiedono altri desideri. E a esaudirli può essere solo lui.

| Rotta | Cosa fa | Se va bene | Se va male |
|---|---|---|---|
| `POST /desideri` | In più: se nel testo c'è la parola «desideri», il Genio rifiuta | come al livello 5 | 400 `"Il Genio non può: niente desideri in più"` |
| `PUT /desideri/{desiderio_id}/esaudito` | Segna il desiderio come esaudito. Solo chi ha il ruolo `"genio"` | 200: il desiderio, con `esaudito` che vale `true` | 403 `"Solo il Genio esaudisce"` · 404 `"Desiderio non trovato"` |

I dettagli:

- «desideri» conta maiuscolo o minuscolo: `"Mille DESIDERI"` è vietato quanto `"altri desideri"`.
- Serve la colonna `ruolo` in `PadroneDB`: `ruolo: Mapped[str] = mapped_column(default="padrone")`.
- Il Genio può esaudire i desideri di chiunque. La PUT non ha corpo.
- Il Genio si registra come tutti, poi lo promuovete con psql:

  ```bash
  psql -d agrabah -c "UPDATE padroni SET ruolo = 'genio' WHERE username = 'genio';"
  ```

## Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| `command not found: fastapi` oppure `No module named …` | Il venv è spento: `source .venv/bin/activate`, dalla cartella `giorno-11` |
| `database "agrabah" does not exist` | `createdb agrabah`, poi `psql -d agrabah -f agrabah.sql` |
| `database "agrabah_test" does not exist` | `createdb agrabah_test` |
| `connection refused` | PostgreSQL è spento. WSL: `sudo service postgresql start` · Mac: `brew services start postgresql@16` |
| `ImportError: cannot import name 'calcola_hash'` nei test | Il test cerca quella funzione in `sicurezza.py`: c'è? Ha proprio quel nome? |
| 401 anche con la chiave giusta | Il `.env` non viene letto: `load_dotenv` prima di `os.environ.get`, poi riavviate il server |
| `Invalid args for response field` | Nel `->` della rotta c'è la tabella (`TesoroDB`): ci va lo stampo (`Tesoro`) |
| `Address already in use` | C'è già un server acceso in un altro terminale: Ctrl+C lì, oppure `fastapi dev main.py --port 8001` |
| Postman va, il test è rosso | Leggete il messaggio del test: di solito è il codice di stato, o il testo di `detail` |
| Avete pasticciato i dati | `psql -d agrabah -f agrabah.sql` rimette i sei tesori, e toglie padroni e desideri |
