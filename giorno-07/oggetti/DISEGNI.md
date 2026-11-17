# Prevedi il disegno

Prima si **disegna**, poi si **controlla**. A coppie, una scheda alla volta: le schede 1–4 sugli oggetti, le 5–7 sull'ereditarietà.

1. **Leggete il codice** della scheda, senza eseguirlo.
2. **Disegnate su Mural**, nella vostra area: le **etichette** (le variabili) a sinistra, le **scatole** (gli oggetti) a destra, una freccia da ogni etichetta alla sua scatola. Dentro ogni scatola, i suoi dati.
3. **Rispondete alle domande** della scheda, sempre su Mural.
4. **Controllate su Python Tutor**: il link della scheda apre il codice già pronto. Premete **Next** una riga alla volta e confrontate il suo disegno con il vostro.
5. Il disegno era diverso? **Correggetelo con un altro colore**, non cancellate: l'errore è la parte che serve.

Python Tutor disegna le cose come le disegniamo noi: a sinistra i *frames* (le etichette), a destra gli *objects* (le scatole).

> Su Python Tutor funziona solo Python «puro»: Pydantic e FastAPI lì non ci sono. Per questo qui le classi sono scritte a mano, con `__init__`.

## Scheda 1 · Due veicoli, due scatole

*Le basi: quante scatole, quante etichette.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"

panda = Veicolo("AB123CD", "Fiat")
vespa = Veicolo("XY98765", "Piaggio")
print(panda.marca, vespa.marca)
```

- Quante scatole `Veicolo` ci sono alla fine? Quante etichette?
- Cosa c'è scritto dentro ogni scatola?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0Apanda%20%3D%20Veicolo%28%22AB123CD%22%2C%20%22Fiat%22%29%0Avespa%20%3D%20Veicolo%28%22XY98765%22%2C%20%22Piaggio%22%29%0Aprint%28panda.marca%2C%20vespa.marca%29%0A&mode=display&py=311)

## Scheda 2 · Due etichette, una scatola

*La trappola più famosa: copiare un'etichetta non copia la scatola.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"

panda = Veicolo("AB123CD", "Fiat")
auto_di_mamma = panda
auto_di_mamma.viaggia(300)
print(panda.km)
```

- Dopo `auto_di_mamma = panda`, quante scatole ci sono? Una o due?
- Cosa stampa l'ultima riga: 0 o 300?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0Apanda%20%3D%20Veicolo%28%22AB123CD%22%2C%20%22Fiat%22%29%0Aauto_di_mamma%20%3D%20panda%0Aauto_di_mamma.viaggia%28300%29%0Aprint%28panda.km%29%0A&mode=display&py=311)

## Scheda 3 · Dove punta self?

*Lo stesso metodo, chiamato su due oggetti diversi.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"

panda = Veicolo("AB123CD", "Fiat")
vespa = Veicolo("XY98765", "Piaggio")
panda.viaggia(100)
vespa.viaggia(40)
panda.viaggia(20)
print(panda.km, vespa.km)
```

- Durante `panda.viaggia(100)`, `self` è attaccato a quale scatola? E durante `vespa.viaggia(40)`?
- Cosa stampa l'ultima riga?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0Apanda%20%3D%20Veicolo%28%22AB123CD%22%2C%20%22Fiat%22%29%0Avespa%20%3D%20Veicolo%28%22XY98765%22%2C%20%22Piaggio%22%29%0Apanda.viaggia%28100%29%0Avespa.viaggia%2840%29%0Apanda.viaggia%2820%29%0Aprint%28panda.km%2C%20vespa.km%29%0A&mode=display&py=311)

## Scheda 4 · Il self dimenticato

*Un errore che vedrete ancora: trovatelo prima che lo trovi Python.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        targa = targa
        self.marca = marca

panda = Veicolo("AB123CD", "Fiat")
print(panda.marca)
print(panda.targa)
```

- Disegnate la scatola di `panda` alla fine: cosa c'è dentro?
- Quale riga darà errore, e quale errore?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%0Apanda%20%3D%20Veicolo%28%22AB123CD%22%2C%20%22Fiat%22%29%0Aprint%28panda.marca%29%0Aprint%28panda.targa%29%0A&mode=display&py=311)

## Scheda 5 · Il figlio eredita

*`class Automobile(Veicolo)`: l'automobile è un veicolo, con qualcosa in più.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"


class Automobile(Veicolo):
    def __init__(self, targa, marca, porte):
        super().__init__(targa, marca)
        self.porte = porte


class Moto(Veicolo):
    def descrivi(self):
        return f"Moto {self.marca}, {self.km} km"

panda = Automobile("AB123CD", "Fiat", 5)
panda.viaggia(50)
print(panda.porte, panda.km)
print(panda.descrivi())
```

- In `Automobile` non c'è nessun `viaggia` e nessun `descrivi`: allora da dove arrivano?
- Disegnate la scatola di `panda`: quanti dati ha? Chi li ha scritti, `Veicolo` o `Automobile`?
- Cosa fa `super().__init__(targa, marca)`?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0A%0Aclass%20Automobile%28Veicolo%29%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%2C%20porte%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28targa%2C%20marca%29%0A%20%20%20%20%20%20%20%20self.porte%20%3D%20porte%0A%0A%0Aclass%20Moto%28Veicolo%29%3A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Moto%20%7Bself.marca%7D%2C%20%7Bself.km%7D%20km%22%0A%0Apanda%20%3D%20Automobile%28%22AB123CD%22%2C%20%22Fiat%22%2C%205%29%0Apanda.viaggia%2850%29%0Aprint%28panda.porte%2C%20panda.km%29%0Aprint%28panda.descrivi%28%29%29%0A&mode=display&py=311)

## Scheda 6 · Il figlio cambia idea

*Un metodo con lo stesso nome nel figlio vince su quello del genitore.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"


class Automobile(Veicolo):
    def __init__(self, targa, marca, porte):
        super().__init__(targa, marca)
        self.porte = porte


class Moto(Veicolo):
    def descrivi(self):
        return f"Moto {self.marca}, {self.km} km"

panda = Automobile("AB123CD", "Fiat", 5)
vespa = Moto("XY98765", "Piaggio")
print(panda.descrivi())
print(vespa.descrivi())
```

- `Moto` non ha un `__init__`: come fa `vespa` ad avere targa e marca?
- Le due `print` chiamano lo stesso `descrivi`?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0A%0Aclass%20Automobile%28Veicolo%29%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%2C%20porte%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28targa%2C%20marca%29%0A%20%20%20%20%20%20%20%20self.porte%20%3D%20porte%0A%0A%0Aclass%20Moto%28Veicolo%29%3A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Moto%20%7Bself.marca%7D%2C%20%7Bself.km%7D%20km%22%0A%0Apanda%20%3D%20Automobile%28%22AB123CD%22%2C%20%22Fiat%22%2C%205%29%0Avespa%20%3D%20Moto%28%22XY98765%22%2C%20%22Piaggio%22%29%0Aprint%28panda.descrivi%28%29%29%0Aprint%28vespa.descrivi%28%29%29%0A&mode=display&py=311)

## Scheda 7 · Un garage di oggetti

*È esattamente com'è fatta la villa di oggi: un dizionario da id a oggetto.*

```python
class Veicolo:
    def __init__(self, targa, marca):
        self.targa = targa
        self.marca = marca
        self.km = 0

    def viaggia(self, quanti):
        self.km = self.km + quanti

    def descrivi(self):
        return f"{self.marca} {self.targa}, {self.km} km"


class Automobile(Veicolo):
    def __init__(self, targa, marca, porte):
        super().__init__(targa, marca)
        self.porte = porte


class Moto(Veicolo):
    def descrivi(self):
        return f"Moto {self.marca}, {self.km} km"

garage = {
    1: Automobile("AB123CD", "Fiat", 5),
    2: Moto("XY98765", "Piaggio"),
}
garage[2].viaggia(30)
for veicolo in garage.values():
    print(veicolo.descrivi())
```

- Disegnate il dizionario: le chiavi da una parte, le frecce verso le scatole dall'altra.
- Leggete `garage[2].viaggia(30)` da sinistra a destra, un pezzo alla volta.
- Il `for` chiama sempre `veicolo.descrivi()`: quale `descrivi` parte, ogni volta?

**Controllate:** [apri su Python Tutor](https://pythontutor.com/visualize.html#code=class%20Veicolo%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%29%3A%0A%20%20%20%20%20%20%20%20self.targa%20%3D%20targa%0A%20%20%20%20%20%20%20%20self.marca%20%3D%20marca%0A%20%20%20%20%20%20%20%20self.km%20%3D%200%0A%0A%20%20%20%20def%20viaggia%28self%2C%20quanti%29%3A%0A%20%20%20%20%20%20%20%20self.km%20%3D%20self.km%20%2B%20quanti%0A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22%7Bself.marca%7D%20%7Bself.targa%7D%2C%20%7Bself.km%7D%20km%22%0A%0A%0Aclass%20Automobile%28Veicolo%29%3A%0A%20%20%20%20def%20__init__%28self%2C%20targa%2C%20marca%2C%20porte%29%3A%0A%20%20%20%20%20%20%20%20super%28%29.__init__%28targa%2C%20marca%29%0A%20%20%20%20%20%20%20%20self.porte%20%3D%20porte%0A%0A%0Aclass%20Moto%28Veicolo%29%3A%0A%20%20%20%20def%20descrivi%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20f%22Moto%20%7Bself.marca%7D%2C%20%7Bself.km%7D%20km%22%0A%0Agarage%20%3D%20%7B%0A%20%20%20%201%3A%20Automobile%28%22AB123CD%22%2C%20%22Fiat%22%2C%205%29%2C%0A%20%20%20%202%3A%20Moto%28%22XY98765%22%2C%20%22Piaggio%22%29%2C%0A%7D%0Agarage%5B2%5D.viaggia%2830%29%0Afor%20veicolo%20in%20garage.values%28%29%3A%0A%20%20%20%20print%28veicolo.descrivi%28%29%29%0A&mode=display&py=311)

## E nel codice di oggi?

Aprite `colpo/villa.py`: `class Guardia(GuardiaNuova)` e `class Ospite(OspiteNuovo)`. È la scheda 5: `Guardia` è una `GuardiaNuova` con in più l'`id`. E `BaseModel`, tra parentesi in tutte le altre, è il genitore che scrive l'`__init__` al posto vostro.

## Se finite prima

Aggiungete una classe `Furgone(Veicolo)` con un dato in più, `carico_massimo`, e un metodo `carica(kg)` che non fa mai superare il carico massimo. Prima disegnate una scatola di `Furgone`, poi controllate su Python Tutor.
