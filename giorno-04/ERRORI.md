# Leggere gli errori

Un errore non è Python che si arrabbia: è Python che vi dice **cosa** è andato storto e **dove**. Basta sapere in che ordine leggerlo.

## 1. Il traceback si legge dal basso

```text
Traceback (most recent call last):
  File "/home/anna/corso-coding-arkemis/giorno-04/squadra-a/prova-debug/gandalf.py", line 12, in <module>
    print(nome, "porta", zaini[nome], "lembas")
                         ~~~~~^^^^^^
KeyError: 'Gandalf'
```

| Ordine | Cosa leggete | Qui |
|---|---|---|
| 1 | **L'ultima riga**: il tipo di errore e il messaggio | `KeyError: 'Gandalf'`: nel dizionario non c'è la chiave `'Gandalf'` |
| 2 | **La riga sopra**: il codice che si è rotto, con i segni `^^^` sotto il pezzo colpevole | `zaini[nome]` |
| 3 | **Ancora sopra**: il file e il numero di riga | `gandalf.py`, riga 12 |

Se il traceback è lungo, ci sono più blocchi `File ..., line ...`: è la strada che Python ha fatto, una funzione dentro l'altra. **Cercate il blocco più in basso che è un vostro file**: i file con `site-packages` o `lib/python` nel percorso sono di Python, e quasi mai sono loro a sbagliare.

## 2. Gli errori che vedrete di più

Python ha un catalogo di errori già pronti, ognuno con un nome che dice cosa è successo. Non dovete inventarli: dovete riconoscerli.

| Errore | Vuol dire | Esempio | Dove guardare |
|---|---|---|---|
| `SyntaxError` / `IndentationError` | Python non riesce nemmeno a leggere il codice | `if x == 1` senza i due punti, un rientro sbagliato | La riga indicata, o **quella prima** |
| `NameError` | Usate un nome che non esiste | `pirnt("ciao")`, una variabile scritta male | Maiuscole, minuscole, errori di battitura. Spesso Python suggerisce: *Did you mean…?* |
| `TypeError` | Un'operazione tra tipi che non vanno d'accordo | `"anni: " + 30`, `[1, 2] + "tre"` | Di che tipo sono le due cose? `type(x)` nella Debug Console |
| `KeyError` | In un dizionario non c'è quella chiave | `zaini["Gandalf"]` | Le chiavi vere del dizionario: `list(d)` |
| `IndexError` | In una lista non c'è quella posizione | `nomi[10]` su una lista di 5 | Quanto è lunga la lista: `len(nomi)`. Si conta da 0 |
| `AttributeError` | Quel tipo di oggetto non ha quel metodo | `lista.add(x)`: le liste hanno `append` | Di che tipo è l'oggetto, e quali metodi ha |
| `ValueError` | Il tipo è giusto, il valore no | `int("sette")`, `a, b = [1, 2, 3]` | Il valore che è arrivato davvero: stampatelo o guardatelo nel debugger |
| `ZeroDivisionError` | Divisione per zero | `totale / 0` | Da dove arriva quello zero |

**Ricetta**: leggete il tipo di errore → andate alla riga → mettete lì un breakpoint → guardate le variabili in VARIABLES. Nove volte su dieci il valore che vedete non è quello che pensavate.

## 3. Correggere o gestire?

Davanti a un errore la domanda è una sola: **è un mio sbaglio, o è una cosa che può succedere davvero?**

| | È un bug | È una situazione prevista |
|---|---|---|
| Esempi | Nome scritto male, chiave sbagliata, `.add` su una lista | L'utente scrive «sette» invece di 7, un file che manca, un dato sporco |
| Cosa fate | **Correggete il codice.** Niente `try/except` | **Gestite l'errore** con `try/except` |

Un `try/except` messo per nascondere un bug non lo sistema: lo rende invisibile.

## 4. `try/except`: gestire un errore previsto

```python
try:
    voto = int(testo)              # proviamo
except ValueError:                 # se int() fallisce proprio con ValueError…
    print("Non è un numero", file=sys.stderr)
    voto = None                    # …facciamo questo, e il programma va avanti
```

- **Sempre il nome dell'errore** dopo `except`. Un `except:` da solo cattura tutto, anche i vostri bug.
- Dentro `try` mettete **solo le righe che possono fallire**, non mezza funzione.
- Dentro un ciclo, `continue` vuol dire «salta questo giro e passa al prossimo».

## 5. `raise`: l'errore lo sollevate voi

Quando una vostra funzione riceve un valore che non ha senso, non deve tirare a indovinare: deve fermarsi e dirlo.

```python
def dividi_conto(totale, persone):
    if persone <= 0:
        raise ValueError(f"Persone non valide: {persone}")
    return totale / persone
```

- `raise` ferma la funzione, come `return`, ma con un errore.
- Il messaggio è per chi leggerà il traceback: scrivete **cosa** non va e **che valore** è arrivato.
- Nei test: `with pytest.raises(ValueError):` vuol dire «qui mi aspetto proprio questo errore».

### `raise` dentro la funzione, `try` fuori

L'errore più comune: scrivere il `try/except` dentro la funzione. Il `try` va **dove chiamate** la funzione:

```python
try:
    quota = dividi_conto(30, 0)
except ValueError as errore:
    print("Non si può dividere:", errore)
    quota = None
```

1. Python entra nel `try` e chiama `dividi_conto(30, 0)`.
2. Dentro la funzione `persone` vale 0: parte il `raise`, e il `return` non viene mai eseguito.
3. Python salta all'`except`: `errore` contiene il messaggio. Stampa `Non si può dividere: Persone non valide: 0`.
4. Il programma continua, senza traceback rosso.

Con `dividi_conto(30, 3)` non c'è nessun `raise`: `quota` vale `10.0` e l'`except` viene saltato.

Chi **scrive** la funzione decide quando è un errore (`raise`). Chi la **usa** decide cosa fare se succede (`try/except`). È la tappa 7: `minuti()` fa `raise`, `soste()` la chiama dentro un `try`.

Si può anche trasformare un errore di Python in uno vostro, più chiaro:

```python
try:
    numero = int(testo)
except ValueError:
    raise ValueError(f"Non è un numero: {testo!r}")
```

`{testo!r}` mostra il testo con gli apici intorno: così si vedono anche gli spazi.
