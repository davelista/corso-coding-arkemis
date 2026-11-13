-- Esercizio 4
-- Le navi della Marina con più di 30 cannoni.
--
-- Colonne:      nome, cannoni
-- Righe attese: 2
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 4
SELECT nome, cannoni FROM navi WHERE cannoni > 30 AND bandiera= 'Marina';
