# Il colpo · villa Dumarais

Parigi, la sera del gala. Nella villa del banchiere Gaston Dumarais c'è una festa, e nel caveau, sotto terra, c'è la **collana della Regina**. Stanotte la vuole un ladro gentiluomo che firma i suoi colpi con un nome solo: **Arsène Lupin**. Voi siete la sua banda.

Il vostro informatore è riuscito a copiare i dati della sicurezza della villa: le stanze, le telecamere, le guardie, la lista degli ospiti. Il problema è che sono un mucchio di dati, e stanotte non c'è tempo di leggerli a mano. Serve un'**API**: si chiede, si risponde.

L'API la scrivete voi, un livello alla volta. Le prime quattro richieste vi danno **le quattro cifre della combinazione**. Le altre tre preparano il terreno: ci si mette in lista, si sposta chi c'è davanti al caveau, si spengono le telecamere. Poi si prova la cassaforte.

## I file

| File | Cosa c'è | Si tocca? |
|---|---|---|
| `villa.py` | Gli stampi (le classi) e i dati della villa | No, si legge |
| `cassaforte.py` | La cassaforte: `POST /cassaforte/apri` | No |
| `main.py` | La vostra API: due esempi già fatti, poi un livello alla volta | **Sì, solo questo** |
| `test_colpo.py` | I test di ogni livello | No |

## Prima di tutto

Dalla cartella `giorno-07`, con il venv acceso (vedi il README del giorno):

```bash
cd colpo
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

In un **secondo terminale**, sempre con il venv acceso e dentro `colpo`:

```bash
pytest -v -k livello_1
```

## Come si gioca

1. **Leggete il livello** qui sotto e in `main.py`. Ogni livello aggiunge **una cosa sola** rispetto a quello prima.
2. **Scrivete il codice** in `main.py`, nel posto del livello.
3. **Lanciate il test del livello**: `pytest -v -k livello_1` (con il numero giusto). Rosso? Leggete il messaggio, è scritto per voi. Ancora non è chiaro? Breakpoint nella rotta, triangolo verde, la richiesta da `/docs`, e guardate le variabili.
4. **Verde?** Andate su `/docs`, fate la richiesta con **Try it out** → **Execute**, e rispondete alla **domanda del livello**. Segnate la cifra.
5. Commit e push, poi si cambia chi scrive.

**Attenzione:** con `fastapi dev`, a ogni salvataggio di `main.py` il server si riavvia (con il debugger invece si riavvia a mano: il bottone verde ↻ Restart), e la villa torna com'era all'inizio. Le richieste del piano (livelli 5, 6, 7 e la cassaforte) vanno fatte **tutte di fila, quando avete finito di scrivere il codice**.

## Le regole del gruppo

1. **Una tastiera sola, a turno.** Chi scrive condivide lo schermo, gli altri leggono e decidono. Si cambia a ogni livello. Parte chi si sente meno sicuro.
2. **Un livello alla volta, in ordine.** Non si passa al livello dopo con il test rosso.
3. **Bloccati da 10 minuti?** Aprite l'aiutino del livello (qui sotto). Ancora bloccati? Scrivete nel canale delle domande: il livello, il messaggio del test, cosa avete provato.
4. **La combinazione non si dice alle altre squadre.** Gli aiuti sì, a voce.

### I branch, come ieri

```bash
# chi crea il branch (a, b, c… è la lettera del gruppo)
git switch -c colpo-a
git push -u origin colpo-a

# gli altri del gruppo
git pull
git switch colpo-a
```

A ogni livello verde: `git pull`, poi `git add main.py`, `git commit -m "Livello 1: le stanze senza quelle segrete"`, `git push`.

---

## Livello 0 · Le spie (con il debugger)

Prima di scrivere codice, si impara a guardare dentro il server mentre risponde.

**Cosa fare:** seguite [`../DEBUG.md`](../DEBUG.md): il `launch.json` lo scrivete voi. Poi un breakpoint sulla prima riga di `leggi_ospite`, il **triangolo verde** di Run and Debug, e da `/docs` la richiesta `GET /ospiti/5`. VS Code si ferma.

**La domanda:** nel pannello Variables, dopo uno **↷ Step Over**: chi è l'ospite numero 5, e che mestiere fa? Poi, nella Debug Console: `len(telecamere)`. Quante telecamere ci sono nella villa?

Niente test, niente cifre: questo livello serve a voi, e lo fa ognuno sul suo computer. Da qui in poi, **ogni volta che un test è rosso e non capite perché, prima di chiedere: un breakpoint.**

## Livello 1 · GET, la lista

**Cosa fare:** `GET /stanze` risponde con la lista delle stanze, **tranne quelle segrete**. La funzione c'è già: manca l'`if` dentro il `for`.

**La cosa nuova:** un `if` dentro la rotta. L'esempio da guardare è `lista_ospiti`. **Questo livello lo facciamo insieme.**

**La domanda:** quante stanze vede un ospite qualunque sulla piantina? Quel numero è **la prima cifra**.

<details><summary>Aiutino</summary>

`stanza` è un oggetto `Stanza`: i suoi dati si leggono con il punto. `stanza.segreta` vale `True` o `False`. «Se non è segreta, aggiungila»: `if not stanza.segreta:` e poi `visibili.append(stanza)`.

</details>

## Livello 2 · GET, uno solo

**Cosa fare:** `GET /stanze/{stanza_id}` risponde con la stanza, **anche se è segreta**. Se l'id non c'è: 404 `"Stanza non trovata"`.

**La cosa nuova:** niente di nuovo! È `leggi_ospite`, con le stanze al posto degli ospiti.

**La domanda:** il caveau non è sulla piantina. Chiedete le stanze una per una, da 1 in su, finché il server risponde 404: qual è l'**id della stanza segreta che sta sotto terra** (piano -1)? È **la seconda cifra**.

<details><summary>Aiutino</summary>

Tre righe: prendete la stanza dal dizionario con `stanze.get(stanza_id)`; se è `None`, `raise HTTPException(...)`; altrimenti `return`. Togliete la riga con il 501.

</details>

## Livello 3 · GET con un filtro

**Cosa fare:** `GET /telecamere` risponde con tutte le telecamere. `GET /telecamere?stanza_id=4` solo con quelle della stanza 4. Se in una stanza non ci sono telecamere, la risposta è una lista vuota `[]` (non un 404: la richiesta è giusta, solo che non c'è niente).

**La cosa nuova:** scrivete voi il decoratore e la riga del `def`. E il filtro arriva dopo il `?`: è un argomento della funzione che **non** sta nel percorso, con il valore di partenza `None`.

**La domanda:** quante telecamere sono montate nel caveau, accese o spente? È **la terza cifra**.

<details><summary>Aiutino</summary>

```python
@app.get("/telecamere")
def lista_telecamere(stanza_id: int | None = None) -> list[Telecamera]:
```

Dentro: come al livello 1, un `for` e un `if`. Ma prima chiedetevi: se `stanza_id` è `None`, cosa devo restituire?

</details>

## Livello 4 · GET, chi c'è in una stanza

**Cosa fare:** `GET /stanze/{stanza_id}/guardie` risponde con le guardie che stanno davanti a quella stanza. Se la stanza non c'è: 404 `"Stanza non trovata"`.

**La cosa nuova:** due cose che sapete già, insieme. Il controllo del livello 2, poi il filtro del livello 3 (sulle guardie, con `guardia.stanza_id`). È la JOIN di venerdì, fatta in Python.

**La domanda:** quante guardie ci sono davanti al caveau? È **la quarta cifra**. Segnatevi anche **i loro id**: servono al livello 6.

<details><summary>Aiutino</summary>

Per il 404 non serve riscrivere niente: potete chiamare la funzione del livello 2, `leggi_stanza(stanza_id)`. Se la stanza non c'è, l'eccezione parte da lì.

</details>

---

**Avete le quattro cifre?** Non provate ancora la cassaforte: prima va preparato il terreno.

## Livello 5 · POST, crea

**Cosa fare:** `POST /ospiti`, con il corpo `{"nome": "...", "professione": "..."}`, aggiunge un ospite. Risponde **201** con l'ospite nuovo, id compreso.

**La cosa nuova:** il corpo della richiesta. Arriva come `OspiteNuovo` (senza id): voi create un `Ospite` (con l'id) e lo mettete nel dizionario.

**Il piano:** Lupin entra come **Paul Sernine**, collezionista. Perché proprio quel nome? Mettete in fila le lettere di *Arsène Lupin*.

<details><summary>Aiutino</summary>

```python
@app.post("/ospiti", status_code=status.HTTP_201_CREATED)
def nuovo_ospite(dati: OspiteNuovo) -> Ospite:
```

Dentro: `ospite = Ospite(id=prossimo_id(ospiti), nome=dati.nome, professione=dati.professione)`, poi `ospiti[ospite.id] = ospite`, poi `return ospite`.

</details>

## Livello 6 · PUT, sostituisce

**Cosa fare:** `PUT /guardie/{guardia_id}`, con il corpo di una `GuardiaNuova` (tutti i campi, senza id), **sostituisce** la guardia. Risponde 200 con la guardia aggiornata, oppure 404 `"Guardia non trovata"`.

**La cosa nuova:** un id nel percorso **e** un corpo, nella stessa richiesta.

**Il piano:** il vostro informatore ha falsificato l'ordine di servizio. Spostate **tutte** le guardie del caveau in cantina (la stanza 9). Con la PUT si rimanda **tutta** la guardia: nome, turno e anni di servizio uguali a prima, cambia solo `stanza_id`.

<details><summary>Aiutino</summary>

1. Controllate che la guardia esista (come al livello 2, ma sulle guardie).
2. Create la guardia nuova, con l'id del percorso e i dati del corpo:
   ```python
   guardia = Guardia(id=guardia_id, nome=dati.nome, stanza_id=dati.stanza_id,
                     turno=dati.turno, anni_servizio=dati.anni_servizio)
   ```
   Chi vuole può usare la scorciatoia delle slide, `Guardia(id=guardia_id, **dati.model_dump())`: fa la stessa cosa.
3. Rimettetela nel dizionario allo stesso id, e restituitela.

</details>

## Livello 7 · DELETE, cancella

**Cosa fare:** `DELETE /telecamere/{telecamera_id}` toglie la telecamera. Risponde **204, senza corpo**. Se non c'è: 404 `"Telecamera non trovata"`.

**La cosa nuova:** il 204 e `del`.

**Il piano:** spegnete le telecamere **accese** del caveau. Quali sono? Ve l'ha detto il livello 3.

<details><summary>Aiutino</summary>

`@app.delete("/telecamere/{telecamera_id}", status_code=status.HTTP_204_NO_CONTENT)`. Dentro: se l'id non è nel dizionario (`if telecamera_id not in telecamere:`), il 404; altrimenti `del telecamere[telecamera_id]`. Niente `return`.

</details>

---

## Il finale · la cassaforte

Tutte le richieste del piano, di fila, **senza salvare `main.py` in mezzo**: la POST di Paul Sernine, le PUT delle guardie, le DELETE delle telecamere. Poi, da `/docs`:

`POST /cassaforte/apri` con `{"combinazione": "...."}`

Se manca qualcosa, la cassaforte risponde 403 e vi dice cosa. Quando si apre: screenshot nel canale del corso, commit «Colpo riuscito» e push.

## Se finite prima · extra

1. **409:** `POST /ospiti` con un nome già in lista risponde 409 `"Nome già in lista"`.
2. **Due filtri:** `GET /telecamere?stanza_id=3&accesa=true`, solo le telecamere accese.
3. **Una lista nuova:** `GET /guardie`, e `GET /guardie?turno=sera`.

I test: `pytest -v -k extra`.

## Bonus · PATCH

Al livello 6, per spostare una guardia avete dovuto rimandare **tutti** i suoi dati, anche quelli che non cambiavano. È così che funziona la PUT: **sostituisce**.

La PATCH invece **modifica**: si manda solo il campo che cambia. `PATCH /guardie/3` con `{"stanza_id": 9}`.

In `villa.py` c'è già lo stampo giusto, `GuardiaModifica`: tutti i campi facoltativi. Due strumenti di Pydantic:

- `dati.model_dump(exclude_unset=True)` dà solo i campi che il client ha mandato davvero;
- `guardia.model_copy(update=...)` fa una copia della guardia, con quei campi cambiati.

Test: `pytest -v -k bonus`.

## Quando un test è rosso

| Il test dice | Vuol dire |
|---|---|
| `501` | Non avete ancora tolto la riga del «da fare» |
| `404` invece di 200 | La rotta non esiste: controllate il percorso nel decoratore. Oppure esiste, ma non trova l'oggetto |
| `405` | La rotta esiste, ma non con quel verbo: `@app.get` al posto di `@app.put`? |
| `200` invece di 404 | Manca il controllo: l'oggetto che non esiste |
| `200` invece di 201 o 204 | Manca `status_code=...` nel decoratore |
| `422` | Pydantic ha rifiutato i dati: leggete il dettaglio, dice quale campo non va |
| `AttributeError: 'dict' object has no attribute…` | State usando un dizionario come un oggetto, o il contrario: gli oggetti si leggono con il punto, `stanza.nome` |
