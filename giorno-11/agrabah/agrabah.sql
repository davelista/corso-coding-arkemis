-- ============================================================
--  LA LAMPADA DI AGRABAH · i tesori, i padroni, i desideri
--  Corso intensivo di coding · Giorno 11
--
--      createdb agrabah
--      psql -d agrabah -f agrabah.sql
-- ============================================================

SET client_min_messages = warning;
DROP TABLE IF EXISTS desideri, padroni, tesori CASCADE;

-- I tesori del bazar. Chiunque li guarda; li tocca solo chi ha la chiave della Caverna.
CREATE TABLE tesori (
    id         SERIAL PRIMARY KEY,
    nome       TEXT NOT NULL,
    valore     INTEGER NOT NULL CHECK (valore >= 0),
    maledetto  BOOLEAN NOT NULL DEFAULT FALSE
);

-- Chi può avere la lampada. La password NON c'è: c'è solo la sua impronta.
CREATE TABLE padroni (
    id             SERIAL PRIMARY KEY,
    username       TEXT NOT NULL UNIQUE,
    nome           TEXT NOT NULL,
    password_hash  TEXT NOT NULL,
    ruolo          TEXT NOT NULL DEFAULT 'padrone'      -- 'padrone' oppure 'genio' (livello 6)
);

-- I desideri. Ogni desiderio è di un padrone: padrone_id dice di chi.
CREATE TABLE desideri (
    id          SERIAL PRIMARY KEY,
    testo       TEXT NOT NULL,
    esaudito    BOOLEAN NOT NULL DEFAULT FALSE,
    padrone_id  INTEGER NOT NULL REFERENCES padroni(id)
);

INSERT INTO tesori (nome, valore, maledetto) VALUES
('Lampada a olio', 3, FALSE),
('Tappeto volante', 800, FALSE),
('Rubino della scimmia', 1200, TRUE),
('Scarabeo d''oro', 450, FALSE),
('Clessidra rossa', 600, TRUE),
('Flauto del mercante', 40, FALSE);
