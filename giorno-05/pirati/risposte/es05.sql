-- Esercizio 5
-- Per ogni arrembaggio fallito: porto, data, nome della nave e capitano.
--
-- Colonne:      porto, data, nave, capitano
-- Righe attese: 4
-- In ordine:    no
--
-- Scrivi la tua query qui sotto, finisci con il punto e virgola e salva.
-- Poi, dalla cartella pirati:   python3 verifica.py 5

SELECT porto, data, navi.nome, capitano FROM arrembaggi JOIN navi ON arrembaggi.nave_id = navi.id WHERE esito = 'fallito';