# Il bazar, in React · Next.js e Tailwind

Il pomeriggio è una pagina sola da ricreare: il bazar di stamattina, ma fatto a componenti. Ogni esercizio costruisce un componente, il lab finale monta la pagina.

**La pagina da ricreare** è [`pagina-da-ricreare.html`](pagina-da-ricreare.html): apritela con un doppio clic e provatela. La lampada conta i desideri, il bottone nasconde i maledetti. È il vostro traguardo delle 17:10.

## Il progetto

Si crea **dentro `giorno-11/`**, con un comando solo:

```bash
node --version               # deve dire v22 o più
npx create-next-app@latest bazar-next --js --tailwind --no-eslint --app
cd bazar-next
npm run dev                  # poi aprite http://localhost:3000
```

Se `create-next-app` fa altre domande: Invio, cioè la risposta già scelta.

| File o cartella | Cosa c'è | Si tocca? |
|---|---|---|
| `app/page.js` | La pagina: quello che si vede su `localhost:3000` | Sì |
| `app/components/` | I vostri componenti. La cartella la create voi | Sì |
| `app/layout.js` | La cornice di tutte le pagine: `html` e `body` | Poco |
| `app/globals.css` | Il CSS di tutto il sito. La prima riga accende Tailwind: non si toglie | Poco |
| `node_modules/` | Le librerie scaricate. Mai nel repo: è già nel `.gitignore` | Mai |

## I componenti della pagina

| Componente | File | Cosa fa | Esercizio |
|---|---|---|---|
| `Home` | `app/page.js` | La pagina: mette insieme tutti gli altri | 1, poi il lab |
| `Insegna` | `app/components/Insegna.jsx` | Il titolo e il sottotitolo | 2 |
| `Piede` | `app/components/Piede.jsx` | La riga in fondo | 2 |
| `Tesoro` | `app/components/Tesoro.jsx` | Una scheda. Riceve `nome`, `valore`, `maledetto` | 3 |
| `Lampada` | `app/components/Lampada.jsx` | Il bottone dei tre desideri | 5 |

## I sei tesori

Per il lab: `app/dati.js`.

```javascript
export const tesoriIniziali = [
  { id: 1, nome: "Lampada a olio", valore: 3, maledetto: false },
  { id: 2, nome: "Tappeto volante", valore: 800, maledetto: false },
  { id: 3, nome: "Rubino della scimmia", valore: 1200, maledetto: true },
  { id: 4, nome: "Scarabeo d'oro", valore: 450, maledetto: false },
  { id: 5, nome: "Clessidra rossa", valore: 600, maledetto: true },
  { id: 6, nome: "Flauto del mercante", valore: 40, maledetto: false },
];
```

## Da sapere

- **Il titolo sembra testo normale?** È Tailwind, che azzera gli stili del browser. Si veste con le classi, dall'esercizio 4.
- **In JSX** si scrive `className`, non `class`. Ogni tag va chiuso: `<Insegna />`.
- **`"use client";`** va sulla prima riga dei file che usano lo stato o i clic.

## Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| Il bottone c'è, ma sembra testo | Tailwind azzera gli stili: dategli le classi (`bg-…`, `px-…`, `py-…`, `rounded`) |
| Un errore rosso, a tutto schermo | Leggetelo: dice il file e la riga. Corretto e salvato, sparisce da solo |
| `… needs useState … Client Component` | Manca `"use client";` sulla prima riga del file che usa lo stato |
| `Each child in a list should have a unique "key"` | Manca `key` nel `map`: `key={t.id}`, sul tag più esterno |
| `Too many re-renders` | `onClick={setNascosti(true)}` chiama subito: serve la freccia, `onClick={() => …}` |
| Clicco e non cambia niente | Lo stato si cambia solo con `set…`: mai `nascosti = true`, mai `tesori.push` |
| `Port 3000 is in use` | C'è già un server acceso in un altro terminale: Ctrl+C lì |
