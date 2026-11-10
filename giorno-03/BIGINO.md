# Il bigino di Python

Tutto quello che serve oggi, in una pagina. Provate ogni riga nel terminale interattivo: `python3`, e per uscire `exit()`.

## Lanciare

```bash
python3                  # il terminale interattivo: >>> e scrivete una riga alla volta
python3 iniziali.py      # lancia un file
pytest test_iniziali.py -v
```

## Variabili e tipi

```python
nome = "Anna"            # str, testo: tra virgolette
eta = 30                 # int, numero intero
prezzo = 1.5             # float, numero con la virgola (che in Python è un punto)
iscritta = True          # bool: True o False, con la maiuscola
nulla = None             # «nessun valore»

type(prezzo)             # <class 'float'>
int("7")    float("2.5")    str(7)     # conversioni
```

`=` mette un valore in una variabile. `==` chiede «sono uguali?».

## Operazioni

```python
7 + 2    7 - 2    7 * 2    7 / 2       # 9  5  14  3.5
7 // 2   7 % 2    2 ** 3               # 3 (divisione intera)  1 (resto)  8 (potenza)
round(33.3333, 2)                      # 33.33
totale = totale + prezzo               # aggiornare una variabile
```

## Stringhe

```python
nome = "  Anna Maria "
nome.strip()             # "Anna Maria"    toglie gli spazi ai lati
nome.lower()             # tutto minuscolo      nome.upper()  tutto maiuscolo
nome.replace(" ", "")    # "AnnaMaria"
"a,b,c".split(",")       # ["a", "b", "c"]      "il gatto".split()  →  ["il", "gatto"]
"-".join(["a", "b"])     # "a-b"
len("ciao")              # 4
"ciao"[0]                # "c", il primo (si conta da 0)
"ciao"[-1]               # "o", l'ultimo
"ciao"[1:3]              # "ia", dal secondo al terzo
"ia" in "ciao"           # True

f"Ciao {nome}, totale {prezzo:.2f}"   # f-string: le variabili tra graffe, :.2f = 2 decimali
```

I metodi restituiscono una stringa nuova: `nome.lower()` da solo non cambia `nome`. Serve `nome = nome.lower()`.

## Confronti e condizioni

```python
==  !=  <  <=  >  >=          # uguale, diverso, minore, …
and  or  not                  # tutte e due, almeno una, il contrario
1 <= voto <= 10               # tra 1 e 10, estremi compresi

if voto >= 9:
    giudizio = "ottimo"
elif voto >= 6:               # solo se la condizione sopra è falsa
    giudizio = "sufficiente"
else:
    giudizio = "insufficiente"
```

I due punti `:` e il rientro di **4 spazi** dicono a Python cosa sta dentro l'`if`. Niente parentesi graffe.

## Liste

```python
voti = [7, 4, 6]
voti[0]                  # 7
voti.append(9)           # aggiunge in fondo: [7, 4, 6, 9]
len(voti)                # 4
4 in voti                # True
voti[1:]                 # [4, 6, 9]: tutti tranne il primo
sorted(voti)             # [4, 6, 7, 9], una lista nuova in ordine
```

## Tuple

```python
punto = (45.07, 7.69)          # una tupla: come una lista, ma tra tonde e non si modifica
punto[0]                       # 45.07
lat, lon = punto               # spacchettare: lat = 45.07, lon = 7.69
```

Lista quando i dati cambiano (si aggiunge, si toglie), tupla quando sono fissi (le coordinate di una città).

## Cicli

```python
for voto in voti:                # un giro per ogni elemento
    print(voto)

for i in range(3):               # 0, 1, 2
    print(i)
range(1, 11)                     # da 1 a 10: l'ultimo è escluso

numero = 3
while numero > 0:                # finché la condizione è vera
    print(numero)
    numero = numero - 1          # senza questa riga il ciclo non finisce mai
```

Lo schema dell'accumulatore, che userete tutto il giorno:

```python
somma = 0                        # 1. prima del ciclo: il valore di partenza
for voto in voti:
    somma = somma + voto         # 2. dentro: si aggiorna
print(somma)                     # 3. dopo il ciclo (rientro tolto): si usa
```

## Dizionari

```python
listino = {"penna": 1.5, "zaino": 25.0}    # chiave: valore
listino["penna"]                           # 1.5 (KeyError se la chiave non c'è)
listino.get("gomma", 0)                    # 0: il valore, oppure il default
listino["gomma"] = 0.8                     # aggiunge o sovrascrive
"zaino" in listino                         # True: cerca tra le chiavi

for prodotto, prezzo in listino.items():   # chiave e valore insieme
    print(f"{prodotto}: {prezzo}")
```

## Funzioni

```python
def prezzo_scontato(prezzo: float, sconto: float) -> float:
    """Cosa fa la funzione: una frase."""
    return prezzo - prezzo * sconto

finale = prezzo_scontato(100, 0.2)   # 80.0
```

**`return` non è `print`.** `print` mostra un valore sullo schermo e la funzione restituisce `None`.
`return` consegna il valore a chi ha chiamato la funzione: è quello che controllano i test.
Dopo `return` la funzione finisce: le righe sotto non vengono eseguite.

## Errori

```python
try:
    voto = int(testo)
except ValueError:               # sempre l'errore preciso, mai except da solo
    print("Non è un numero")

if persone <= 0:
    raise ValueError("Serve almeno una persona")   # l'errore lo sollevate voi
```

Gli errori che vedrete di più: `SyntaxError` (manca `:` o una parentesi), `IndentationError` (rientro sbagliato), `NameError` (variabile scritta male o mai creata), `TypeError` (`"3" + 4`: testo più numero), `KeyError` (chiave che non c'è), `IndexError` (posizione che non c'è).
Leggete l'ultima riga del messaggio: dice cosa; quella con `line` dice dove.

## File

```python
with open("spese.csv") as file:          # with: il file si chiude da solo
    righe = file.read().splitlines()     # lista di righe, senza "a capo"

for riga in righe[1:]:                   # salta l'intestazione
    data, persona, categoria, importo = riga.split(",")
```
