# Giorno 2 · Codice pulito

Repository dei laboratori del giorno 2 del Corso intensivo di coding.

## Preparazione

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Prima di iniziare tutti i test devono essere verdi.

## 10:05 · Git Exercises

Prima del laboratorio ci alleniamo con il Git vero: la guida passo passo è in [GIT-EXERCISES.md](GIT-EXERCISES.md).

## Mattina · Rendilo professionale

| Cartella | Squadra | Programma | Cosa fa |
|---|---|---|---|
| `squadra-a/` | Registro voti | `voti.py` | Calcola le medie, trova chi è insufficiente e il migliore della classe |
| `squadra-b/` | Carrello | `carrello.py` | Calcola il totale con sconti per quantità, codici sconto e spese di spedizione |
| `squadra-c/` | Iscrizione | `iscrizione.py` | Controlla username, email e password di chi si iscrive a un sito |
| `squadra-d/` | Meteo | `meteo.py` | Riassume minime, massime ed escursioni per città e segnala le giornate anomale |
| `squadra-e/` | Magazzino | `magazzino.py` | Decide quali prodotti riordinare, quanti pezzi e con quale urgenza |

Ogni squadra lavora **solo nella propria cartella**. Il README della cartella spiega come lanciare il programma e le regole del laboratorio.

A ogni regola cambia il **pilota**: condivide lo schermo e scrive dal suo PC, gli altri guidano a voce.

```bash
# il primo pilota crea il branch della squadra
git switch -c squadra-a          # il nome della vostra squadra
git push -u origin squadra-a
# gli altri, la prima volta
git pull
git switch squadra-a
# a ogni regola, il pilota di turno
git pull
# modifica, poi pytest: tutto verde
git add .
git commit -m "Rinomina le variabili"
git push
# alla fine, una volta sola
gh pr create --fill              # oppure su GitHub: «Compare & pull request»
```

## Pomeriggio · Ping-pong del TDD

La cartella `tdd/` è il punto di partenza del validatore di password: si scrive prima il test, poi il codice.
Si lavora in coppia, ogni coppia sul suo branch e **nella sua cartella**, così le pull request non si pestano i piedi.
Dalla cartella `giorno-02` (qui con la coppia 3):

```bash
git switch main && git pull
git switch -c tdd-coppia-3
mkdir tdd/coppia-3
cp tdd/password.py tdd/test_password.py tdd/coppia-3/
cd tdd/coppia-3
pytest                           # sempre da dentro la vostra cartella
```

Si modifica solo `tdd/coppia-N/`: i due file in `tdd/` restano vuoti per tutti.
I test si lanciano da dentro la propria cartella: lanciato da `giorno-02`, pytest troverebbe sette `test_password.py` con lo stesso nome.
Alla fine: commit con il co-autore, `git push -u origin tdd-coppia-3` e la pull request.
