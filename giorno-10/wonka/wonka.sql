-- ============================================================
--  LA FABBRICA DI CIOCCOLATO · i bambini e le sale
--  Corso intensivo di coding · Giorno 9 e 10
--
--      createdb wonka
--      psql -d wonka -f wonka.sql
-- ============================================================

SET client_min_messages = warning;
DROP TABLE IF EXISTS bambini, sale CASCADE;

-- Chi entra in fabbrica. La password NON c'è: c'è solo la sua impronta.
CREATE TABLE bambini (
    id             SERIAL PRIMARY KEY,
    username       TEXT NOT NULL UNIQUE,
    nome           TEXT NOT NULL,
    password_hash  TEXT NOT NULL
);

-- Le sale della fabbrica. Il nome lo vedono tutti, l'ingrediente solo chi ha il biglietto.
CREATE TABLE sale (
    id           SERIAL PRIMARY KEY,
    nome         TEXT NOT NULL UNIQUE,
    descrizione  TEXT NOT NULL,
    ingrediente  TEXT NOT NULL
);

INSERT INTO sale (nome, descrizione, ingrediente) VALUES
('Sala delle invenzioni', 'Macchine che sbuffano, fischiano e inventano dolci che nessuno ha mai assaggiato.', 'Dragée al lampone'),
('Sala delle noci', 'Cento scoiattoli sgusciano noci, una alla volta, senza romperne nemmeno una.', 'Olio di nocciola'),
('Sala del cioccolato', 'Un prato che si mangia e un fiume di cioccolato, mescolato da una cascata.', 'Latte del fiume di cioccolato'),
('Sala delle caramelle', 'Alberi di zucchero filato e caramelle appese ai rami come frutti.', 'Caramello filante'),
('Sala delle bibite frizzanti', 'Bibite con così tante bollicine che chi le beve si alza da terra.', 'Essenza di bollicine');
