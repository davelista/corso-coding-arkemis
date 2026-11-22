# Il bazar di Agrabah · HTML, CSS e JavaScript

Stamattina costruite una pagina sola, un pezzo alla volta: il bazar di Agrabah. Ogni esercizio ne aggiunge un pezzo, e a fine mattina la pagina è intera.

Le consegne sono nelle slide, una per esercizio. Qui trovate quello che serve tenere sottomano.

## Dove si lavora

In questa cartella, `giorno-11/bazar/`. I file li create voi:

| File | Da quando | Cosa c'è |
|---|---|---|
| `index.html` | esercizio 1 | La struttura della pagina |
| `style.css` | esercizio 4 | L'aspetto |
| `app.js` | esercizio 9 | Il comportamento |

Fino all'esercizio 8 la pagina si apre con un doppio clic su `index.html`. Dopo ogni modifica: salvate, e ricaricate la pagina nel browser.

Dall'esercizio 9 serve un server. Dal terminale, **dentro la cartella `bazar`**:

```bash
python3 -m http.server 5500
```

Poi aprite `http://localhost:5500`. Su Windows il comando è `python`, oppure `py`. Per fermarlo: Ctrl+C.

## I sei tesori del bazar

| id | Nome | Valore, in monete | Maledetto? |
|---|---|---|---|
| 1 | Lampada a olio | 3 | no |
| 2 | Tappeto volante | 800 | no |
| 3 | Rubino della scimmia | 1200 | sì |
| 4 | Scarabeo d'oro | 450 | no |
| 5 | Clessidra rossa | 600 | sì |
| 6 | Flauto del mercante | 40 | no |

Sono gli stessi tesori dell'API del gruppo backend: oggi li scrivete a mano, giovedì arrivano da lì.

## I colori

| Cosa | Codice |
|---|---|
| Sabbia, lo sfondo | `#F4E3C1` |
| Blu notte, il testo e i bordi | `#1B1B3A` |
| Rosso, per i maledetti | `#B3261E` |

## Gli strumenti del browser

- **F12** apre DevTools. Su Mac: Option + Command + I.
- **Elements:** l'albero della pagina. Un clic su un elemento, e a destra vedete le regole CSS che valgono per lui.
- **Console:** qui si scrive JavaScript una riga alla volta, e qui compaiono gli errori, in rosso, con il file e la riga.

## Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| Cambio il file, ma la pagina è uguale | Avete salvato? Poi ricaricate la pagina. E controllate di aver aperto il file giusto |
| Il CSS non fa niente | Nel `head` c'è `<link rel="stylesheet" href="style.css">`? Il nome del file è proprio quello? |
| Una regola non vince | In Elements → Styles la vedete barrata: più in basso nel file ce n'è un'altra che arriva dopo |
| Lo script non parte | La pagina va aperta da `localhost:5500`, non con il doppio clic. E F12 va aperto lì |
| Pagina bianca dopo aver toccato `app.js` | F12, scheda Console: l'errore, in rosso, dice il file e la riga |
