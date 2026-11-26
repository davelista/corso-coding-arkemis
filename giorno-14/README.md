# Giorno 14 · React con Next.js: l'ombra di Peter Pan

Si riparte da capo con React, con calma. La mattina: cos'è un componente, com'è fatto un progetto Next.js, props e children. Il pomeriggio: la caccia all'ombra di Peter Pan, a gruppi.

| Quando | Cosa | Dove |
|---|---|---|
| 9:15 | Quiz: caccia al componente | AhaSlides |
| 10:00 | Esercizio 1: ritagliate la pagina dell'ombra | Mural, il mural della vostra squadra |
| 11:10 | Esercizio 2: accendete l'isola (`Header` e `Footer`) | `isola-next/` |
| 12:25 | Esercizio 3: tre luoghi e una pergamena (`CardLuogo` e `Pergamena`) | `isola-next/` |
| 14:00 | `components/index.js`, le liste con `map`, il `Bottone` | `isola-next/` |
| 14:40 | La caccia all'ombra: cinque tappe, con il forziere | `isola-next/` e [`dati.js`](dati.js) |

Tailwind, le unità di misura, flex e grid: tutto in [`TAILWIND.md`](TAILWIND.md).

## Una volta sola: il materiale di oggi

Dal terminale (su Windows: Ubuntu, WSL). Un comando alla volta.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-14
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

## Il progetto di oggi

Si crea **dentro `giorno-14/`**, con un comando solo. È un progetto nuovo, solo per oggi: il vostro progetto non si tocca.

```bash
node --version               # deve dire v22 o più
npx create-next-app@latest isola-next --js --tailwind --no-eslint --app
cd isola-next
npm run dev                  # poi aprite http://localhost:3000
```

Se `create-next-app` fa altre domande: Invio, cioè la risposta già scelta. Per spegnere il server: Ctrl+C.

| File o cartella | Cosa c'è | Si tocca? |
|---|---|---|
| `app/page.js` | La pagina: quello che si vede su `localhost:3000` | Sì |
| `app/components/` | I vostri componenti. La cartella la create voi | Sì |
| `app/components/index.js` | L'elenco dei componenti: una riga per componente | Sì, dal pomeriggio |
| `app/dati.js` | I sei luoghi della caccia: lo copiate da qui | Si copia |
| `app/layout.js` | La cornice di tutte le pagine: `html` e `body` | Poco |
| `app/globals.css` | Il CSS di tutto il sito. La prima riga accende Tailwind: non si toglie | Poco |
| `node_modules/` | Le librerie scaricate. Mai nel repo: è già nel `.gitignore` | Mai |

## Le regole dei componenti

- **Un componente, un file**, in `app/components/`. Il nome del file è il nome del componente, con la **Maiuscola**: `Header.jsx`, non `header.jsx`.
- Si scrivono tutti così:

  ```jsx
  export default function Header() {
    return <header>…</header>;
  }
  ```

- `Header` con la maiuscola è il vostro componente. `<header>` minuscolo è il tag HTML che c'è dentro.
- **Dal pomeriggio**, ogni componente ha anche una riga in `app/components/index.js`:

  ```js
  export { default as Header } from "./Header.jsx";
  ```

  e la pagina li prende tutti da lì, con un import solo:

  ```js
  import { Header, Footer, Pergamena } from "./components";
  ```

- Dentro `components/` i componenti tra loro si importano diretti: `CardLuogo` scrive `import Bottone from "./Bottone.jsx";`, non passa dall'elenco.

## I componenti della pagina

| Componente | File | Cosa fa | Quando |
|---|---|---|---|
| `Home` | `app/page.js` | La pagina: mette insieme tutti gli altri | Esercizio 2, poi tutto il giorno |
| `Header` | `app/components/Header.jsx` | Il titolo e il sottotitolo | Esercizio 2 |
| `Footer` | `app/components/Footer.jsx` | La riga in fondo | Esercizio 2 |
| `CardLuogo` | `app/components/CardLuogo.jsx` | Una scheda. Riceve `nome`, `descrizione`, `zona` | Esercizio 3, poi tappe 2 e 3 |
| `Pergamena` | `app/components/Pergamena.jsx` | Una cornice per i suoi `children` | Esercizio 3 |
| `ListaLuoghi` | `app/components/ListaLuoghi.jsx` | Le sei schede, con un `map` | Tappa 1 |
| `Bottone` | `app/components/Bottone.jsx` | Il bottone che fa parlare il luogo | Tappa 2 |
| `Finale` | `app/components/Finale.jsx` | La pergamena del finale | Tappa 5 |

## Esercizio 3: i tre luoghi

| Nome | Zona | Descrizione |
|---|---|---|
| Scoglio del Teschio | Laguna | Una roccia a forma di teschio, in mezzo alla laguna |
| Tana dei Bimbi Sperduti | Foresta | La casa sotto l'albero, dove dormono i Bimbi |
| Laghetto del Coccodrillo | *nessuna: vale il default, «Isola che non c'è»* | Acqua ferma, e un rumore strano dal fondo |

Il messaggio della pergamena: «Stanotte l'ombra di Peter è scappata. Campanellino ha segnato sei luoghi sulla mappa: cerchiamola!»

## La caccia

- I sei luoghi sono in [`dati.js`](dati.js): copiatelo in `isola-next/app/dati.js`, accanto a `page.js`.
- Ogni tappa finisce con una **parola d'ordine**, che vi mostra la vostra pagina solo se il codice funziona. La scrivete nel **forziere**: il link ve lo do in aula.
- A ogni tappa scrive un altro del gruppo. Le tappe 1, 2 e 3 sono per tutti; la 4 e la 5 per chi arriva prima.

## Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| `Event handlers cannot be passed to Client Component props` | Manca `"use client";` sulla prima riga di `Bottone.jsx` |
| `Each child in a list should have a unique "key" prop` | Manca `key={luogo.id}` sulla `CardLuogo`, dentro il `map` |
| `Module not found: Can't resolve '../dati.js'` | Il percorso: `dati.js` sta in `app/`, `ListaLuoghi` in `app/components/`. Serve `../` |
| `luoghi is not defined`, o una pagina vuota | `export const` si importa con le graffe: `import { luoghi } from "../dati.js";` |
| `Export ListaLuoghi doesn't exist in target module` | Manca la riga di `ListaLuoghi` in `components/index.js`. Vale per ogni componente |
| L'alert parte da solo, appena si apre la pagina | Manca la freccia: `onClick={() => alert(messaggio)}` |
| Il bottone c'è, ma sembra testo | Tailwind azzera gli stili: servono le classi `bg-…`, `px-…`, `py-…`, `rounded-…` |
| Le tre colonne non arrivano | La finestra è stretta: `md:` parte da 768px. Allargatela |
| `Port 3000 is in use` | C'è già un server acceso in un altro terminale: Ctrl+C lì |
