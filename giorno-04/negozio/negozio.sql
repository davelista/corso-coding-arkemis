-- ============================================================
--  NEGOZIO · il database degli esempi di oggi
--  Corso intensivo di coding · Giorno 4
--
--      createdb negozio
--      psql -d negozio -f negozio.sql
-- ============================================================

SET client_min_messages = warning;
DROP TABLE IF EXISTS righe_ordine, articoli, ordini, clienti CASCADE;

CREATE TABLE clienti (
    id           SERIAL PRIMARY KEY,
    nome         TEXT NOT NULL,
    cognome      TEXT NOT NULL,
    email        TEXT UNIQUE,
    citta        TEXT NOT NULL,
    iscritto_il  DATE NOT NULL
);

CREATE TABLE ordini (
    id           SERIAL PRIMARY KEY,
    cliente_id   INTEGER NOT NULL REFERENCES clienti(id),
    data         DATE NOT NULL,
    totale       NUMERIC(8, 2) NOT NULL,
    stato        TEXT NOT NULL CHECK (stato IN ('nuovo', 'spedito', 'consegnato', 'annullato'))
);

INSERT INTO clienti (nome, cognome, email, citta, iscritto_il) VALUES
('Anna',     'Rossi',     'anna.rossi@example.com',     'Milano',  '2025-01-14'),
('Luca',     'Bianchi',   'luca.b@example.com',         'Torino',  '2025-02-02'),
('Giulia',   'Colombo',   'giulia.colombo@example.com', 'Milano',  '2025-03-21'),
('Marco',    'Ferrari',   NULL,                         'Bologna', '2025-03-30'),
('Sara',     'Romano',    'sara.romano@example.com',    'Roma',    '2025-04-11'),
('Paolo',    'Galli',     'paolo.galli@example.com',    'Milano',  '2025-05-05'),
('Elena',    'Conti',     'elena.conti@example.com',    'Napoli',  '2025-06-18'),
('Matteo',   'Fontana',   'matteo.f@example.com',       'Torino',  '2025-07-01'),
('Chiara',   'Costa',     NULL,                         'Milano',  '2025-09-09'),
('Davide',   'Rizzo',     'davide.rizzo@example.com',   'Bergamo', '2025-10-23'),
('Marta',    'Moretti',   'marta.moretti@example.com',  'Roma',    '2026-01-07'),
('Simone',   'Barbieri',  'simone.b@example.com',       'Milano',  '2026-02-15'),
('Federica', 'Lombardi',  'federica.l@example.com',     'Monza',   '2026-04-30'),
('Andrea',   'Mariani',   'andrea.mariani@example.com', 'Bologna', '2026-06-12'),
('Irene',    'Riva',      'irene.riva@example.com',     'Milano',  '2026-09-01');

INSERT INTO ordini (cliente_id, data, totale, stato) VALUES
(1,  '2026-01-10',  42.50, 'consegnato'),
(1,  '2026-03-02', 118.00, 'consegnato'),
(1,  '2026-09-28',  19.90, 'spedito'),
(2,  '2026-02-14',  65.00, 'consegnato'),
(3,  '2026-02-20', 230.40, 'consegnato'),
(3,  '2026-05-11',  12.00, 'annullato'),
(3,  '2026-08-03',  89.90, 'consegnato'),
(3,  '2026-10-01',  54.30, 'nuovo'),
(4,  '2026-04-04',  15.00, 'consegnato'),
(5,  '2026-04-18', 310.00, 'consegnato'),
(5,  '2026-07-22',  27.80, 'consegnato'),
(6,  '2026-05-30',  99.00, 'spedito'),
(7,  '2026-06-01',  45.60, 'consegnato'),
(7,  '2026-06-15',  45.60, 'annullato'),
(8,  '2026-07-07', 150.00, 'consegnato'),
(8,  '2026-09-19',  64.20, 'spedito'),
(10, '2026-08-08',  33.33, 'consegnato'),
(11, '2026-09-02',  72.00, 'nuovo'),
(12, '2026-09-10', 188.80, 'spedito'),
(12, '2026-09-25',  21.00, 'nuovo'),
(13, '2026-09-30',  49.99, 'nuovo'),
(14, '2026-10-02', 260.00, 'nuovo');
-- Chiara Costa (9) e Irene Riva (15) non hanno ancora ordinato: servono per la LEFT JOIN.
