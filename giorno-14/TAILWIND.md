# Tailwind CSS · la guida del corso

Tailwind non è un altro linguaggio: è CSS scritto a pezzetti, direttamente nel `className`. Ogni classe è **una regola CSS**. Questa guida non si impara a memoria: si tiene aperta mentre si lavora, e si cerca quello che serve.

> **In una riga:** `p-6` vuol dire `padding: 1.5rem`. Leggete la classe, pensate alla regola CSS, e il resto viene da sé.

## Indice

1. [Come funziona in Next.js](#1-come-funziona-in-nextjs)
2. [Come si legge una classe](#2-come-si-legge-una-classe)
3. [Le misure: px e rem](#3-le-misure-px-e-rem)
4. [Spazi: padding, margin, gap](#4-spazi-padding-margin-gap)
5. [Testo](#5-testo)
6. [Colori](#6-colori)
7. [Bordi e angoli](#7-bordi-e-angoli)
8. [Larghezze e altezze](#8-larghezze-e-altezze)
9. [Flexbox: in fila o in colonna](#9-flexbox-in-fila-o-in-colonna)
10. [Grid: righe e colonne](#10-grid-righe-e-colonne)
11. [Schermi diversi: sm, md, lg](#11-schermi-diversi-sm-md-lg)
12. [Gli stati: hover, focus, disabled](#12-gli-stati-hover-focus-disabled)
13. [Classi che cambiano: il ternario](#13-classi-che-cambiano-il-ternario)
14. [Le classi della pagina di Peter Pan](#14-le-classi-della-pagina-di-peter-pan)
15. [Se qualcosa non va](#15-se-qualcosa-non-va)
16. [Dove approfondire](#16-dove-approfondire)

---

## 1. Come funziona in Next.js

Con `create-next-app … --tailwind` è già tutto pronto. Due cose da sapere:

- In `app/globals.css` la **prima riga** accende Tailwind. Non si toglie:

  ```css
  @import "tailwindcss";
  ```

- Usiamo **Tailwind 4**: non c'è un file `tailwind.config.js`. Se un tutorial vi dice di crearlo, è scritto per Tailwind 3.

E una cosa che spiazza: **Tailwind azzera gli stili del browser.** Un `<h1>` è grande come il testo normale, un `<button>` sembra testo, una lista non ha i pallini. È voluto: ogni cosa si veste con le sue classi.

**Consiglio:** in VS Code installate l'estensione **Tailwind CSS IntelliSense**. Mentre scrivete vi suggerisce le classi, e passandoci sopra con il mouse vi mostra la regola CSS vera.

## 2. Come si legge una classe

Quasi tutte le classi hanno la stessa forma: **cosa**, un trattino, **quanto** (o **quale**).

| Classe | Si legge | In CSS |
|---|---|---|
| `p-6` | spazio interno (padding), 6 gradini | `padding: 1.5rem` |
| `mt-2` | margine sopra (margin-top), 2 gradini | `margin-top: 0.5rem` |
| `text-xl` | testo grande, taglia xl | `font-size: 1.25rem` |
| `font-bold` | testo in grassetto | `font-weight: 700` |
| `bg-slate-900` | sfondo, colore slate, tono 900 | `background-color: …` |
| `text-slate-400` | colore del testo, slate, tono 400 | `color: …` |
| `md:grid-cols-3` | da schermo medio in su: tre colonne | `@media (width >= 48rem) { … }` |

Le classi si mettono una dopo l'altra, separate da uno spazio. L'ordine non conta:

```jsx
<h1 className="text-4xl font-bold text-center">Dov'è finita l'ombra di Peter?</h1>
```

## 3. Le misure: px e rem

Due misure, due immagini.

- **`px` è il righello.** Un pixel è un puntino dello schermo. 16px sono 16 puntini, **sempre**: se qualcuno ingrandisce il testo del browser, i pixel non cambiano.
- **`rem` sono i quadretti del quaderno.** La pagina è un quaderno a quadretti, e un quadretto è grande quanto una lettera del testo normale: di solito **16px**. `1rem` è un quadretto, `2rem` sono due quadretti. Se il testo cresce, crescono anche i quadretti.

**Perché Tailwind usa i quadretti:** chi ci vede poco ingrandisce il testo nelle impostazioni del browser, e con i rem la pagina cresce tutta insieme, spazi compresi. Con il righello il testo cresce e gli spazi no, e tutto si schiaccia.

**I gradini di Tailwind:** ogni quadretto è diviso in **4 gradini**. Un gradino è un quarto di quadretto: `0.25rem`, cioè **4px**. Il numero nelle classi conta i gradini:

| Classe | Gradini | Quadretti (rem) | Pixel |
|---|---|---|---|
| `p-1` | 1 | un quarto · 0.25rem | 4px |
| `p-2` | 2 | mezzo · 0.5rem | 8px |
| `p-4` | 4 | uno · 1rem | 16px |
| `p-6` | 6 | uno e mezzo · 1.5rem | 24px |
| `p-8` | 8 | due · 2rem | 32px |

Per avere i pixel: **il numero per 4**. Con Tailwind 4 vale **qualsiasi numero intero**: anche `p-7` o `mt-13` funzionano.

Ogni tanto vedrete anche `%` (una parte del contenitore: `w-1/2` è il 50%) e `vh` (una parte della finestra: `min-h-screen` vuol dire «alto almeno quanto lo schermo»).

## 4. Spazi: padding, margin, gap

- **padding** (`p-`) è lo spazio **dentro** il riquadro, tra il bordo e il contenuto.
- **margin** (`m-`) è lo spazio **fuori** dal riquadro, tra lui e i vicini.
- **gap** (`gap-`) è lo spazio **tra gli elementi** di una griglia o di un flex. Si mette sul contenitore.

| Classe | Dove | Esempio |
|---|---|---|
| `p-` | su tutti e quattro i lati | `p-6` |
| `px-` · `py-` | a destra e sinistra · sopra e sotto | `px-4 py-2` |
| `pt-` · `pr-` · `pb-` · `pl-` | solo sopra · destra · sotto · sinistra | `pt-8` |
| `m-` · `mx-` · `my-` | come sopra, ma fuori | `my-8` |
| `mt-` · `mb-` | margine sopra · sotto | `mt-2` · `mb-4` |
| `mx-auto` | centra un blocco che ha una larghezza massima | `mx-auto max-w-5xl` |
| `gap-` | spazio tra gli elementi di grid e flex | `gap-4` · `gap-6` |

Le lettere vengono dall'inglese: **t**op, **r**ight, **b**ottom, **l**eft, **x** orizzontale, **y** verticale.

## 5. Testo

| Classe | Cosa fa | Esempio |
|---|---|---|
| `text-xs` … `text-5xl` | grandezza: xs, sm, base, lg, xl, 2xl, 3xl, 4xl, 5xl | `text-xs` = 12px · `text-base` = 16px · `text-4xl` = 36px |
| `font-normal` · `font-semibold` · `font-bold` | spessore | `font-bold` |
| `text-left` · `text-center` · `text-right` | allineamento | `text-center` |
| `uppercase` | tutto maiuscolo | la zona sulla scheda |
| `tracking-wide` · `tracking-widest` | spazio tra le lettere | `tracking-widest` |
| `leading-tight` · `leading-relaxed` | spazio tra le righe | `leading-relaxed` |
| `italic` · `underline` | corsivo · sottolineato | |

Attenzione: `text-` serve a due cose. `text-xl` è la **grandezza**, `text-slate-400` è il **colore**. Si capisce da quello che viene dopo.

## 6. Colori

La forma è sempre **cosa-colore-tono**:

- **cosa**: `bg-` (sfondo), `text-` (testo), `border-` (bordo)
- **colore**: `slate`, `gray`, `zinc`, `red`, `orange`, `amber`, `yellow`, `green`, `emerald`, `teal`, `sky`, `blue`, `indigo`, `violet`, `purple`, `pink`, `rose`, … più `black` e `white`
- **tono**: da `50` (chiarissimo) a `950` (quasi nero), a passi di 100: `50, 100, 200, … 900, 950`

| Classe | Cosa fa |
|---|---|
| `bg-slate-900` | sfondo blu notte, scurissimo |
| `bg-amber-300` | sfondo giallo oro |
| `text-slate-100` | testo quasi bianco |
| `text-slate-400` | testo grigio chiaro |
| `border-amber-300` | bordo giallo |
| `bg-slate-900/50` | lo stesso colore, ma trasparente al 50% |

Tutta la tavolozza, con i colori veri: [tailwindcss.com/docs/colors](https://tailwindcss.com/docs/colors).

## 7. Bordi e angoli

| Classe | Cosa fa |
|---|---|
| `border` | un bordo sottile, 1px |
| `border-2` · `border-4` | un bordo di 2px · 4px |
| `border-t` · `border-b` | un bordo solo sopra · solo sotto |
| `border-slate-700` | il colore del bordo |
| `rounded-md` · `rounded-lg` · `rounded-xl` · `rounded-2xl` | angoli arrotondati, sempre di più (`rounded-lg` = 8px, `rounded-xl` = 12px) |
| `rounded-full` | tondo del tutto: un cerchio, o una pillola |
| `shadow-md` · `shadow-lg` | un'ombra sotto il riquadro, sempre più forte |

**In Tailwind 4, `border` da solo prende il colore del testo.** Mettete sempre anche il colore: `border border-slate-700`.

## 8. Larghezze e altezze

| Classe | Cosa fa |
|---|---|
| `w-full` | largo quanto il contenitore |
| `w-64` | largo 64 gradini (16rem = 256px) |
| `w-1/2` · `w-1/3` | metà · un terzo del contenitore |
| `max-w-md` · `max-w-3xl` · `max-w-5xl` | non più largo di… (`max-w-5xl` = 64rem = 1024px) |
| `min-h-screen` | alto **almeno** quanto lo schermo |
| `h-screen` | alto **esattamente** quanto lo schermo |

La coppia da ricordare per centrare una pagina: `mx-auto max-w-5xl`. Il blocco non supera i 1024px e sta in mezzo.

## 9. Flexbox: in fila o in colonna

Flexbox mette gli elementi **in fila** (o in colonna) e decide come distribuirli. Si accende sul **contenitore**, e vale per i suoi figli diretti.

```jsx
<nav className="flex items-center justify-between gap-4">
  <span>Logo</span>
  <a href="#">Esci</a>
</nav>
```

| Classe | Cosa fa | In CSS |
|---|---|---|
| `flex` | accende flexbox: i figli vanno in fila | `display: flex` |
| `flex-col` | in colonna, uno sotto l'altro | `flex-direction: column` |
| `justify-start` · `justify-center` · `justify-between` | dove stanno **lungo** la fila: all'inizio, al centro, spinti ai due lati | `justify-content` |
| `items-start` · `items-center` · `items-end` | dove stanno **di traverso**: in alto, al centro, in basso | `align-items` |
| `gap-4` | spazio tra un figlio e l'altro | `gap` |
| `flex-wrap` | se non ci stanno, vanno a capo | `flex-wrap: wrap` |
| `flex-1` | questo figlio si prende tutto lo spazio che avanza | `flex: 1` |

Il trucco per centrare qualsiasi cosa, in orizzontale e in verticale: `flex items-center justify-center`.

**Per capirlo davvero:** la guida di CSS-Tricks, con i disegni di ogni proprietà, è la più usata al mondo: [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/). Lì le proprietà hanno il nome CSS: `justify-content: space-between` è il vostro `justify-between`.

**Per allenarvi giocando:** [Flexbox Froggy](https://flexboxfroggy.com/#it), in italiano. Portate le rane sulle ninfee scrivendo CSS.

## 10. Grid: righe e colonne

Grid mette gli elementi in una **griglia**, con righe e colonne insieme. Anche questa si accende sul contenitore.

```jsx
<section className="grid grid-cols-1 gap-6 md:grid-cols-3">
  {/* sei schede: una colonna sul telefono, tre dal tablet in su */}
</section>
```

| Classe | Cosa fa | In CSS |
|---|---|---|
| `grid` | accende la griglia | `display: grid` |
| `grid-cols-3` | tre colonne uguali | `grid-template-columns: repeat(3, minmax(0, 1fr))` |
| `gap-6` | spazio tra le celle | `gap` |
| `col-span-2` | questo elemento occupa due colonne | `grid-column: span 2 / span 2` |
| `grid-rows-2` | due righe uguali | `grid-template-rows` |

**Flex o grid?** Flex quando le cose stanno **in una fila sola** (un menu, una barra, un bottone con un'icona). Grid quando servono **righe e colonne** insieme (una galleria, delle schede).

**Per capirlo davvero:** [A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/), sempre su CSS-Tricks.

**Per allenarvi giocando:** [Grid Garden](https://cssgridgarden.com/#it): annaffiate le carote scrivendo CSS.

## 11. Schermi diversi: sm, md, lg

Tailwind parte dal **telefono**. Una classe senza prefisso vale **sempre**; con un prefisso vale **da quella larghezza in su**.

| Prefisso | Da quanto in su |
|---|---|
| `sm:` | 640px |
| `md:` | 768px |
| `lg:` | 1024px |
| `xl:` | 1280px |
| `2xl:` | 1536px |

```jsx
<section className="grid grid-cols-1 md:grid-cols-3">
```

Si legge: **una colonna sempre, tre colonne da 768px in su.** Per provarlo: stringete e allargate la finestra del browser.

## 12. Gli stati: hover, focus, disabled

Un prefisso con i due punti dice **quando** vale la classe.

| Prefisso | Quando | Esempio |
|---|---|---|
| `hover:` | il mouse ci passa sopra | `hover:bg-amber-200` |
| `focus:` | il campo è selezionato (ci state scrivendo) | `focus:border-amber-300` |
| `active:` | mentre lo premete | `active:scale-95` |
| `disabled:` | il bottone è disabilitato | `disabled:opacity-50 disabled:cursor-not-allowed` |

I prefissi si possono combinare: `md:hover:bg-amber-200` vale solo da 768px in su, e solo con il mouse sopra.

## 13. Classi che cambiano: il ternario

Le classi sono un testo. Se dipendono da una prop, si sceglie il testo con un ternario e lo si mette dentro un template literal, con il backtick:

```jsx
const colori =
  variante === "primario"
    ? "bg-amber-300 text-slate-900"
    : "border border-slate-500 text-slate-400";

<button className={`mt-4 rounded-lg px-4 py-2 font-semibold ${colori}`}>
```

Una regola importante: **scrivete sempre la classe intera.** `"bg-amber-300"` funziona; `` `bg-${colore}-300` `` no, perché Tailwind cerca le classi nel testo dei file, e un pezzo di classe non lo riconosce.

## 14. Le classi della pagina di Peter Pan

| Dove | Le classi | Cosa fanno |
|---|---|---|
| il `main` di `page.js` | `min-h-screen bg-slate-900 p-8 text-slate-100` | alto almeno lo schermo, blu notte, spazio intorno, testo chiaro |
| il `div` attorno a tutto | `mx-auto max-w-5xl` | al centro, mai più largo di 1024px |
| `Header` | `text-center` · `text-4xl font-bold` · `mt-2 text-slate-400` | centrato · titolo grande in grassetto · sottotitolo grigio |
| `Pergamena` | `my-8 rounded-xl border-2 border-amber-300 bg-amber-50 p-6 text-slate-900` | spazio sopra e sotto, angoli tondi, bordo giallo, fondo crema, testo scuro |
| `ListaLuoghi` | `grid grid-cols-1 gap-6 md:grid-cols-3` | una colonna, tre da 768px in su |
| `CardLuogo` | `rounded-xl border border-slate-700 bg-slate-800 p-6` | la scheda: angoli tondi, bordo sottile, fondo un po' più chiaro |
| la zona | `text-xs uppercase tracking-widest text-amber-300` | piccola, maiuscola, lettere larghe, gialla |
| `Bottone` | `mt-4 rounded-lg px-4 py-2 font-semibold` | spazio sopra, angoli tondi, spazio dentro, testo spesso |
| `Footer` | `mt-12 text-center text-sm text-slate-400` | lontano dal resto, centrato, piccolo, grigio |

## 15. Se qualcosa non va

| Se vedete | Cosa fate |
|---|---|
| Nessuno stile, la pagina è tutta bianca e nera | In `app/globals.css` manca la prima riga, `@import "tailwindcss";` |
| Una classe non fa niente | Controllate che sia scritta giusta: con l'estensione IntelliSense, se ci passate sopra e non vedete il CSS, la classe non esiste |
| `class=` invece di `className=` | In JSX si scrive `className` |
| Il bottone sembra testo | Tailwind azzera gli stili: dategli `bg-…`, `px-…`, `py-…`, `rounded-…` |
| Il bordo ha un colore strano | In Tailwind 4 `border` prende il colore del testo: aggiungete `border-slate-700` |
| Le colonne non arrivano | `md:` vale da 768px: allargate la finestra |
| Una classe costruita con `${…}` non funziona | Scrivete la classe intera nel ternario (sezione 13) |

## 16. Dove approfondire

**La documentazione ufficiale**, da tenere aperta. In alto c'è la ricerca: scrivete la proprietà CSS che vi serve (per esempio *padding* o *justify-content*) e trovate le classi.

- [tailwindcss.com/docs](https://tailwindcss.com/docs): tutto Tailwind
- [Styling with utility classes](https://tailwindcss.com/docs/styling-with-utility-classes): l'idea di base
- [Responsive design](https://tailwindcss.com/docs/responsive-design): `sm:`, `md:`, `lg:`
- [Hover, focus, and other states](https://tailwindcss.com/docs/hover-focus-and-other-states): `hover:`, `disabled:` e gli altri
- [Colors](https://tailwindcss.com/docs/colors): la tavolozza completa

**Flexbox e grid, spiegati bene**

- [A Complete Guide to Flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/) · CSS-Tricks
- [A Complete Guide to CSS Grid](https://css-tricks.com/snippets/css/complete-guide-grid/) · CSS-Tricks
- [An Interactive Guide to Flexbox](https://www.joshwcomeau.com/css/interactive-guide-to-flexbox/) · Josh W. Comeau, con esempi da muovere
- [An Interactive Guide to CSS Grid](https://www.joshwcomeau.com/css/interactive-guide-to-grid/) · Josh W. Comeau

**Per allenarsi giocando**

- [Flexbox Froggy](https://flexboxfroggy.com/#it): flexbox, in italiano
- [Grid Garden](https://cssgridgarden.com/#it): grid, in italiano

**Le unità di misura**

- [CSS values and units](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Values_and_units) · MDN

**In VS Code**

- [Tailwind CSS IntelliSense](https://marketplace.visualstudio.com/items?itemName=bradlc.vscode-tailwindcss): suggerimenti, e il CSS vero passando sopra le classi
