-- Esercizio 5
-- Per ogni arrembaggio fallito: porto, data, nome della nave e capitano.
--
-- Colonne:      porto, data, nave, capitano
-- Righe attese: 4
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 5

SELECT a.porto, a.data, n.nome, n.capitano FROM arrembaggi a LEFT JOIN navi n ON a.nave_id = n.id WHERE esito='fallito';