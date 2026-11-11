-- ============================================================
--  SCHEMA DEL PROGETTO · <nome del progetto>
--  <cosa fa l'app, in una frase>
--
--      createdb progetto
--      psql -d progetto -f db/schema.sql
-- ============================================================

SET client_min_messages = warning;
-- Elenca qui tutte le tue tabelle, dalla più "figlia" alla più "madre",
-- così puoi rilanciare il file quante volte vuoi.
DROP TABLE IF EXISTS utenti CASCADE;

-- Gli utenti dell'app. La password non si salva MAI in chiaro:
-- password_hash la riempiamo il giorno 7, con il login.
CREATE TABLE utenti (
    id             SERIAL PRIMARY KEY,
    email          TEXT NOT NULL UNIQUE,
    nome           TEXT NOT NULL,
    password_hash  TEXT NOT NULL,
    creato_il      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ------------------------------------------------------------
--  Le tue tabelle qui sotto. Un esempio di forma:
--
--  CREATE TABLE <tabella> (
--      id          SERIAL PRIMARY KEY,
--      utente_id   INTEGER NOT NULL REFERENCES utenti(id),   -- uno a molti
--      <colonna>   <TIPO> NOT NULL,
--      ...
--  );
--
--  Molti a molti: una tabella ponte con due chiavi esterne
--  CREATE TABLE <a>_<b> (
--      <a>_id  INTEGER NOT NULL REFERENCES <a>(id) ON DELETE CASCADE,
--      <b>_id  INTEGER NOT NULL REFERENCES <b>(id) ON DELETE CASCADE,
--      PRIMARY KEY (<a>_id, <b>_id)
--  );
-- ------------------------------------------------------------

-- Qualche riga di prova, per vedere che tutto funziona
INSERT INTO utenti (email, nome, password_hash) VALUES
    ('prova@example.com', 'Utente di prova', 'da-sostituire-il-giorno-7');
