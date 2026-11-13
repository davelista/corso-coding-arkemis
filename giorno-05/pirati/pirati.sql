-- ============================================================
--  PIRATI · il diario di bordo dei Caraibi
--  Corso intensivo di coding · Giorno 5
--
--      createdb pirati
--      psql -d pirati -f pirati.sql
-- ============================================================

SET client_min_messages = warning;
DROP TABLE IF EXISTS arrembaggi, navi CASCADE;

-- Ogni nave ha un capitano, una bandiera e un porto dove torna.
-- Alcune navi non tornano mai in porto: lì il porto è vuoto (NULL).
CREATE TABLE navi (
    id          SERIAL PRIMARY KEY,
    nome        TEXT NOT NULL UNIQUE,
    capitano    TEXT NOT NULL,
    bandiera    TEXT NOT NULL CHECK (bandiera IN ('pirata', 'Marina', 'Compagnia delle Indie', 'mercantile')),
    cannoni     INTEGER NOT NULL,
    porto_base  TEXT
);

-- Ogni arrembaggio è di una nave: nave_id è il numero della nave.
-- Il bottino è in dobloni. Se l'arrembaggio è fallito, il bottino è 0.
CREATE TABLE arrembaggi (
    id       SERIAL PRIMARY KEY,
    nave_id  INTEGER NOT NULL REFERENCES navi(id),
    porto    TEXT NOT NULL,
    data     DATE NOT NULL,
    bottino  INTEGER NOT NULL,
    esito    TEXT NOT NULL CHECK (esito IN ('riuscito', 'fallito', 'in corso'))
);

INSERT INTO navi (nome, capitano, bandiera, cannoni, porto_base) VALUES
('Perla Nera',           'Jack Sparrow',      'pirata',                32, 'Tortuga'),
('Olandese Volante',     'Davy Jones',        'pirata',                46, NULL),
('Queen Anne''s Revenge','Barbanera',         'pirata',                40, 'Nassau'),
('Dauntless',            'James Norrington',  'Marina',                50, 'Port Royal'),
('Endeavour',            'Cutler Beckett',    'Compagnia delle Indie', 60, 'Port Royal'),
('Empress',              'Sao Feng',          'pirata',                24, 'Singapore'),
('Silent Mary',          'Armando Salazar',   'Marina',                38, NULL),
('Providence',           'Hector Barbossa',   'Marina',                30, 'Londra'),
('Edinburgh Trader',     'Capitano Bellamy',  'mercantile',            12, 'Tortuga');

INSERT INTO arrembaggi (nave_id, porto, data, bottino, esito) VALUES
(1, 'Port Royal',            '1728-03-12',  4200, 'riuscito'),
(1, 'Nassau',                '1728-07-02',  6500, 'riuscito'),
(1, 'Isla de Muerta',        '1729-01-20',  9800, 'riuscito'),
(1, 'Singapore',             '1730-05-15',     0, 'fallito'),
(2, 'Kingston',              '1728-11-03',  7300, 'riuscito'),
(2, 'Shipwreck Cove',        '1730-09-09',     0, 'fallito'),
(2, 'L''Avana',              '1731-02-14',  5100, 'riuscito'),
(3, 'Florida',               '1729-06-06',  3900, 'riuscito'),
(3, 'Charleston',            '1729-08-21', 12000, 'riuscito'),
(5, 'Tortuga',               '1730-04-01',  2500, 'riuscito'),
(5, 'Shipwreck Cove',        '1730-09-10',     0, 'fallito'),
(6, 'Singapore',             '1729-12-24',  1500, 'riuscito'),
(6, 'Macao',                 '1731-03-30',   800, 'in corso'),
(7, 'Saint Martin',          '1731-05-05',     0, 'fallito'),
(7, 'Triangolo del Diavolo', '1731-06-11',  2200, 'riuscito'),
(8, 'Whitecap Bay',          '1729-07-15',  1100, 'riuscito');
