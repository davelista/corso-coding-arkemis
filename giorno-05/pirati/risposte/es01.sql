-- Esercizio 1
-- Le navi pirata, in ordine alfabetico di nome.
--
-- Colonne:      nome, capitano
-- Righe attese: 4
-- In ordine:    sì, per nome
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 1

SELECT nome, capitano FROM navi WHERE bandiera = 'pirata' ORDER BY nome ASC LIMIT 4;