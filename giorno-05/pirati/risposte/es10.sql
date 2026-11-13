-- Esercizio 10
-- Le navi che non hanno mai fatto un arrembaggio, senza usare LEFT JOIN.
--
-- Colonne:      nave, capitano
-- Righe attese: 2
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 10

SELECT nome, capitano
FROM navi
WHERE NOT EXISTS(
    SELECT *
    FROM arrembaggi as t2
    WHERE t2.nave_id = navi.id
);