# Checklist dello schema

Per la revisione a coppie, prima che passi il docente. Ogni punto: sì, no, o «non so» (e si chiede).

1. Il dominio si spiega **in una frase**, a qualcuno che non programma.
2. Ci sono **da 4 a 7 tabelle**, compresa `utenti`. Di più: si taglia.
3. Ogni tabella ha una **chiave primaria** (`id`).
4. C'è almeno una **uno a molti**: la chiave esterna sta dalla parte del «molti».
5. C'è almeno una **molti a molti**, con la tabella ponte e le due chiavi esterne.
6. **Niente liste dentro una colonna** (`"rock, jazz, pop"`): quella è un'altra tabella.
7. **Niente dati copiati** in due posti (il nome del cliente non sta anche negli ordini). Eccezione: le «fotografie», come il prezzo pagato in un ordine.
8. I **tipi giusti**: date in `DATE`, soldi in `NUMERIC`, sì/no in `BOOLEAN`.
9. Almeno un **vincolo** che impedisce un dato sbagliato (`NOT NULL`, `UNIQUE`, `CHECK`).
10. I nomi sono **coerenti**: minuscole, al plurale per le tabelle, `snake_case`.
