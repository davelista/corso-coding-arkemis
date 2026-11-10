# Palestra · per chi finisce prima

Dieci esercizi individuali, dal più facile al più difficile. Prima però: avete già letto e approvato la PR del vostro compagno?

```bash
git switch main && git pull
git switch -c palestra-anna                  # il vostro nome
mkdir palestra/anna                          # dalla cartella giorno-03
cp palestra/esercizi.py palestra/test_esercizi.py palestra/anna/
cd palestra/anna
pytest -v                                    # sempre da dentro la vostra cartella
```

Si modifica solo `palestra/<nome>/`: i due file in `palestra/` restano vuoti per tutti.
Commit a ogni esercizio verde; la PR a fine giornata, anche se non li avete finiti tutti.
