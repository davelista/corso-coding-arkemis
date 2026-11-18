-- ============================================================
--  VILLA DUMARAIS · i dati della sicurezza, nel database
--  Corso intensivo di coding · Giorno 7, ripreso al giorno 9
--
--  È lo stesso file di giorno-07/villa-db. Serve ai test,
--  che rifanno villa_test da capo prima di ogni test.
--
--      createdb villa
--      psql -d villa -f villa.sql
-- ============================================================

SET client_min_messages = warning;
DROP TABLE IF EXISTS telecamere, guardie, ospiti, stanze CASCADE;

-- Le stanze della villa. Quelle segrete non sono sulla piantina degli ospiti.
CREATE TABLE stanze (
    id       SERIAL PRIMARY KEY,
    nome     TEXT NOT NULL UNIQUE,
    piano    INTEGER NOT NULL,
    segreta  BOOLEAN NOT NULL DEFAULT false
);

-- Ogni telecamera è montata in una stanza: stanza_id è il numero della stanza.
CREATE TABLE telecamere (
    id         SERIAL PRIMARY KEY,
    stanza_id  INTEGER NOT NULL REFERENCES stanze(id),
    modello    TEXT NOT NULL,
    accesa     BOOLEAN NOT NULL
);

-- Ogni guardia sta davanti a una stanza.
CREATE TABLE guardie (
    id             SERIAL PRIMARY KEY,
    nome           TEXT NOT NULL,
    stanza_id      INTEGER NOT NULL REFERENCES stanze(id),
    turno          TEXT NOT NULL CHECK (turno IN ('sera', 'notte')),
    anni_servizio  INTEGER NOT NULL CHECK (anni_servizio >= 0)
);

-- La lista degli ospiti del gala. Due ospiti con lo stesso nome? No.
CREATE TABLE ospiti (
    id           SERIAL PRIMARY KEY,
    nome         TEXT NOT NULL UNIQUE,
    professione  TEXT NOT NULL
);

INSERT INTO stanze (nome, piano, segreta) VALUES
('Ingresso', 0, false),
('Salone delle feste', 0, false),
('Caveau', -1, true),
('Biblioteca', 1, false),
('Studio di Gaston Dumarais', 1, false),
('Galleria dei ritratti', 1, false),
('Giardino d''inverno', 0, false),
('Cucine', -1, false),
('Cantina dei vini', -1, false),
('Passaggio dietro la libreria', 1, true);

INSERT INTO telecamere (stanza_id, modello, accesa) VALUES
(1, 'Argus 2', true),
(1, 'Argus 2', true),
(2, 'Vigil HD', true),
(3, 'Argus 3', true),
(6, 'Vigil HD', true),
(6, 'Argus 2', false),
(3, 'Argus 3', false),
(5, 'Vigil HD', true),
(3, 'Argus 3', true),
(7, 'Argus 2', false),
(8, 'Argus 2', true),
(3, 'Argus 3', false),
(3, 'Vigil HD', true),
(4, 'Argus 2', true);

INSERT INTO guardie (nome, stanza_id, turno, anni_servizio) VALUES
('Mathis Lefèvre', 1, 'sera', 12),
('Claire Dubois', 2, 'sera', 3),
('Karim Haddad', 3, 'notte', 20),
('Léa Martin', 6, 'notte', 5),
('Gabriel Roux', 3, 'notte', 7),
('Inès Fontaine', 5, 'sera', 9),
('Hugo Bernard', 9, 'notte', 1),
('Chloé Garnier', 1, 'notte', 15),
('Antoine Mercier', 7, 'sera', 4);

INSERT INTO ospiti (nome, professione) VALUES
('Gaston Dumarais', 'padrone di casa'),
('Hélène Dumarais', 'padrona di casa'),
('Mathilde Dumarais', 'figlia dei padroni di casa'),
('Isabelle Moreau', 'gallerista'),
('Contessa di Cagliostro', 'collezionista di gioielli'),
('Victor Hautefeuille', 'notaio'),
('Sophie Lenoir', 'giornalista'),
('Ispettore Ganimard', 'polizia');
