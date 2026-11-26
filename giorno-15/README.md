# Giorno 15 · Lo stato, e il tè dei matti

La mattina si lavora ancora sulla pagina dell'ombra di Peter Pan: lo stato (`useState`) e i clic che cambiano la pagina. Verso mezzogiorno si accende un'API e le si fanno le prime domande dalla console del browser. Il pomeriggio i dati entrano nella pagina: la pagina li legge, li aspetta e li cambia.

| Quando | Cosa | Dove |
|---|---|---|
| 9:15 | Quiz: il ritorno dei componenti | AhaSlides |
| 9:55 | Esercizio 1, tutti insieme: la polvere di fata (`PolvereDiFata`) | `giorno-14/isola-next/` |
| 10:50 | Esercizio 2: il cannocchiale di Campanellino (`Bottone`, `CardLuogo`) | `giorno-14/isola-next/` |
| 11:35 | Accendiamo l'API, in un terminale nuovo | [`meraviglie-api/`](meraviglie-api) |
| 12:15 | Esercizio 3: le prime domande, dalla console del browser | la console di `localhost:3000` |
| 14:00 | Il progetto del pomeriggio | `tavola-next/` |
| 14:35 | Il tè dei matti: cinque tappe a puntate, con il forziere | `tavola-next/` |

Tailwind: il manualetto è ancora quello di ieri, [`giorno-14/TAILWIND.md`](../giorno-14/TAILWIND.md).

## Stamattina: si riparte dalla pagina di ieri

Il codice di ieri è già nel vostro computer: alle 9:15 non si scarica niente. Dal terminale (su Windows: Ubuntu, WSL):

```bash
cd ~/corso-coding-arkemis/giorno-14/isola-next
npm run dev                  # poi aprite http://localhost:3000
```

**Ieri non avete finito la caccia?** Prima scaricate il materiale di oggi:

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
```

Se `git switch main` risponde «Your local changes would be overwritten»: scrivete `git stash` e rifate `git switch main`.

Poi in [`isola-partenza/app`](isola-partenza/app) c'è la pagina di ieri, finita. Copiate i file dentro la vostra `giorno-14/isola-next/app`, sostituendo quelli che ci sono. Salvate e ricaricate il browser.

## Lo stato, in quattro righe

```jsx
"use client";                                   // c'è uno stato o un clic: serve il browser
import { useState } from "react";               // useState lo dà React

const [pizzichi, setPizzichi] = useState(0);    // il valore, il campanello, da dove si parte
<button onClick={() => setPizzichi(pizzichi + 1)}>Un pizzico in più</button>
```

- Si legge il valore: `{pizzichi}`. Si cambia **solo** con il set: `pizzichi = 5` non suona il campanello.
- `useState` sta in cima al componente, prima del `return`. Mai dentro un `if`.
- `const [pizzichi, setPizzichi]`: `pizzichi` è un dato, `setPizzichi` una **funzione** (si chiama con le tonde).

## Gli esercizi della mattina

| Esercizio | Cosa | File |
|---|---|---|
| 1 · La polvere di fata, insieme | Un contatore di pizzichi che sale a ogni clic | `PolvereDiFata.jsx` (nuovo), `index.js`, `page.js` |
| 2 · Il cannocchiale | L'indizio si apre dentro la scheda, non più con l'alert | `Bottone.jsx`, `CardLuogo.jsx` |
| 3 · Le prime domande | Una `fetch` all'API dalla console del browser, il CORS, `.json()` | la console, e il blocco CORS in `meraviglie-api/main.py` |

Le consegne passo per passo sono sulle slide verdi.

## 11:35 · L'API, in un terminale nuovo

`isola-next` resta acceso nel suo terminale. Ne aprite **un altro** (in VS Code: il `+` in alto a destra del pannello del terminale). L'API resta accesa fino alle 18. Il `git pull` scarica il materiale di oggi.

```bash
cd ~/corso-coding-arkemis
git switch main
git pull
cd giorno-15
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd meraviglie-api
fastapi dev main.py          # poi aprite http://127.0.0.1:8000/docs
```

Prova: in `/docs`, `GET /ospiti`, *Try it out*, *Execute*. Dopo un secondo e mezzo arrivano sei ospiti.

Se risponde `Address already in use`: è ancora accesa l'API di Agrabah. Ctrl+C nel suo terminale.

## 12:15 · Le prime domande, dalla console

Sulla pagina di `isola-next` (`localhost:3000`): F12, scheda **Console**. In console `const` non serve.

```js
risposta = await fetch("http://localhost:8000/ospiti")   // la prima volta: errore CORS
// in meraviglie-api/main.py togliete i # dalle sei righe del blocco CORS, salvate, e rifate la riga
risposta.status            // 200
ospiti = await risposta.json()
ospiti                     // sei ospiti
```

Poi provate `/ospiti/4` e `/regina`. **Niente PUT dalla console**: la tavola serve com'è per la caccia. Se l'avete cambiata, Ctrl+C sull'API e riaccendetela.

## 14:00 · Il progetto del pomeriggio

Nel terminale di `isola-next`: **prima Ctrl+C**. La porta 3000 serve a `tavola-next`: se è occupata, Next parte sul 3001 e il CORS dice di no. L'API invece resta accesa.

```bash
cd ~/corso-coding-arkemis/giorno-15
npx create-next-app@latest tavola-next --js --tailwind --no-eslint --app
cd tavola-next
npm run dev                  # poi aprite http://localhost:3000
```

Poi **sostituite** `app/page.js` con questo, e create `app/components/index.js`. È solo la cornice: il resto lo scrivete voi.

```jsx
// app/page.js
import { Tavola } from "./components";

export default function Home() {
  return (
    <main className="min-h-screen bg-sky-50 p-8 text-slate-900">
      <div className="mx-auto max-w-5xl">
        <header className="text-center">
          <h1 className="text-4xl font-bold">Il tè dei matti</h1>
          <p className="mt-2">
            Alice aiuta il Cappellaio a invitare gli ospiti
          </p>
        </header>
        <Tavola />
      </div>
    </main>
  );
}
```

```js
// app/components/index.js · una riga per componente, come ieri
export { default as Tavola } from "./Tavola.jsx";
```

Finché `Tavola.jsx` non esiste, la pagina dà errore: è normale, lo create alla tappa 1.

## L'API del Paese delle Meraviglie

È già scritta: oggi si lavora sul frontend. L'unica cosa da toccare è il blocco **CORS** in `meraviglie-api/main.py`, nell'esercizio 3 di stamattina.

| Rotta | Cosa fa |
|---|---|
| `GET /ospiti` | I sei ospiti. Ci mette un secondo e mezzo: il Bianconiglio è sempre in ritardo |
| `GET /ospiti/{id}` | Un ospite solo |
| `PUT /ospiti/{id}` | Corpo `{"invitato": true}`: l'ospite arriva a tavola, e risponde con la sua `frase` |

Per rimettere tutti gli ospiti come all'inizio: Ctrl+C sull'API, e riaccendetela.

## La caccia: il tè dei matti

A puntate: prima di ogni tappa, dieci minuti di teoria insieme.

- Cinque tappe. Ogni tappa finisce con una **parola d'ordine**, che vi mostra la vostra pagina solo se il codice funziona. La scrivete nel **forziere**: il link ve lo do in aula.
- A ogni tappa scrive un altro del gruppo. Le tappe 1, 2, 3 e 4 sono per tutti; la 5 per chi arriva prima.

| Tappa | Cosa | File |
|---|---|---|
| 1 · La lista degli ospiti | I nomi degli ospiti, dall'API: `useState`, `useEffect`, `fetch` | `Tavola.jsx`, `index.js` |
| 2 · Ognuno al suo posto | Una scheda per ospite, su tre colonne | `CardOspite.jsx`, `Tavola.jsx` |
| 3 · Aspettando il Bianconiglio | «Sta caricando…» e i messaggi di errore | `Tavola.jsx` |
| 4 · Gli inviti | Il bottone «Invita»: un `PUT` all'API | `CardOspite.jsx`, `Tavola.jsx` |
| 5 · Buon non-compleanno! | Il contatore, e la festa finale | `Tavola.jsx` |

## Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| `You're importing a component that needs useState` | Manca `"use client";` sulla prima riga del file che usa lo stato |
| `useState is not defined` | Manca `import { useState } from "react";` (e `useEffect`, se lo usate) |
| `Too many re-renders` | Manca la freccia: `onClick={() => setPizzichi(pizzichi + 1)}` |
| Il numero non cambia mai | Usate una `let`, o assegnate a mano: si cambia solo con il set |
| Nella console: `blocked by CORS policy` | In `meraviglie-api/main.py` togliete i `#` dal blocco CORS, e salvate. Next è sul 3000? |
| `TypeError: Failed to fetch` | L'API è spenta, o c'è il CORS: guardate il terminale dell'API |
| `ospiti.map is not a function` | Manca `.json()`, o un `await`: in `setOspiti` deve arrivare la lista |
| Il terminale dell'API scorre senza fermarsi | Mancano le `[]` in fondo allo `useEffect` |
| «È tardi, è tardi!…» non se ne va | Manca `setCaricamento(false)` in fondo a `carica` |
| `422 Unprocessable Content` sul PUT | Manca l'header `Content-Type`, o il `body` senza `JSON.stringify` |
| `404 Not Found` | Indirizzo sbagliato: porta `8000`, `/ospiti`. Avete lasciato `/regina`? |
| `Address already in use` | Un'altra API è già accesa sull'8000: Ctrl+C là |
| `Port 3000 is in use`, o Next parte sul 3001 | `isola-next` è ancora acceso: Ctrl+C nel suo terminale |
