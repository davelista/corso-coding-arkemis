# La talpa · caccia al bug con il debugger

La collana è al sicuro, ma quando la banda fa i conti qualcosa non torna. Qualcuno ha sabotato il programma del bottino: c'è una talpa.

Il programma non si rompe: risponde sempre 200, con numeri che sembrano veri. **Sono tre bug silenziosi**, uno per rotta. Non c'è un traceback da leggere: per trovarli bisogna fermare il server e guardare dentro, con il debugger.

## Prima di tutto

Il debugger configurato come in [`../DEBUG.md`](../DEBUG.md), con la configurazione **«La talpa»**. Poi:

1. In VS Code: **Run and Debug**, scegliete «La talpa» nel menu, poi il **triangolo verde**.
2. Nel browser: **http://127.0.0.1:8000/docs**.
3. In un terminale, dentro `talpa`, con il venv acceso: `pytest -v`. Tre test rossi.

## Come si gioca

Per ogni bug, sempre lo stesso giro:

1. **Leggete il test rosso**: cosa si aspettava, cosa ha ricevuto.
2. **Mettete un breakpoint** sulla prima riga della rotta (clic a sinistra del numero di riga: pallino rosso).
3. **Fate la richiesta da `/docs`**: Try it out, Execute. VS Code si ferma sul pallino.
4. **Andate avanti una riga alla volta** con **↷ Step Over** (o F10) e guardate il pannello **Variables**: quando un valore diventa diverso da quello che vi aspettate, avete trovato la riga.
5. **Prima di correggere**, scrivete sopra la riga un commento: cosa avete visto nel debugger.
6. **Correggete il minimo**: un carattere, a volte un numero. Riaccendete il server con il bottone verde **↻ Restart**, poi rilanciate `pytest -v`.

| Bug | Richiesta da fare in `/docs` | Cosa guardare nel debugger |
|---|---|---|
| 1 | `GET /bottino/totale` | `i` e `somma`, giro per giro: quali pezzi vengono sommati? |
| 2 | `GET /bottino/quota/Lupin` | `tot` e `parte`: il 30% di `tot` quanto dovrebbe fare? |
| 3 | `GET /refurtiva?stanza=Studio` | `risultato`, a ogni giro del `for` |

Il bug 2 si vede bene solo dopo aver corretto il bug 1: la quota usa il totale.

## La Debug Console

Quando VS Code è fermo su un breakpoint, nella **Debug Console** (in basso) potete scrivere Python e vedere subito il risultato, con le variabili di quel momento:

```python
len(refurtiva)
refurtiva[0].nome
tot * 30 / 100
[p.nome for p in refurtiva]
```

È il modo più veloce per provare un'idea prima di cambiare il codice.

<details><summary>Bloccati sul bug 1?</summary>

Contate i giri del `for`: quanti sono? E da che numero parte `i`? Il primo elemento di una lista ha indice…

</details>

<details><summary>Bloccati sul bug 3?</summary>

Guardate `risultato` dopo il primo pezzo dello studio e dopo il secondo. Il secondo si aggiunge al primo, o lo sostituisce?

</details>
