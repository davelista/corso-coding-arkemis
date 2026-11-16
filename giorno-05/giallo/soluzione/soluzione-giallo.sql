select id, nome, cognome from persone where id = (select persona_id from licenze_artisti where strumento = 'sassofono' and stazione = 'Porta Codice');

/* 366	Fernando	Pozzi */

select id, nome, cognome,  civico from persone where via= 'Via dei Tornelli' AND civico=(select max(civico) from persone where via = 'Via dei Tornelli')
GROUP BY id, nome, cognome, civico; 

/* 392	Adalgisa	Brivio	41 */

SELECT persona_id, "data", testo 
FROM testimonianze
WHERE persona_id=366 OR persona_id=392

/* 
366	2026-10-14	Alle 23:49 mi passa davanti un tizio con la giacca arancione catarifrangente, quella dei manutentori della metro. Al tornello il display mostra il suo abbonamento: annuale, il codice iniziava con MN-77, il resto non l'ho letto perché stavo facendo l'assolo. Poi è salito sul terzo vagone. Ha buttato venti centesimi nella mia custodia: tirchio, ma educato.
*/

SELECT * FROM abbonamenti WHERE codice LIKE'MN-77%' AND tipo='annuale' 

SELECT * FROM tornelli WHERE stazione='Porta Codice' AND verso='entrata' AND abbonamento LIKE 'MN-77%' AND ora BETWEEN '23:48:00' AND '23:50:00'
/* 871	MN-7731	Porta Codice	2026-10-13	23:49:29	entrata */

SELECT * FROM abbonamenti WHERE codice='MN-7731'
/* MN-7731	181	annuale	2027-03-27 */

SELECT * FROM persone WHERE id=181
/* 181	Furio	Ganassi	Via Ciclo For	22	manutentore */

/* 392	2026-10-14	Io dormo poco. All'1:12 la porta di servizio di Vecchia Fiera, chiusa da vent'anni, si è aperta: il lettore del badge ha fatto bip e si è accesa la lucina verde. È uscito un uomo con una valigetta di pelle, l'ha messa nel cestino di una bici a noleggio e se n'è andato. Mio marito dice che me lo sono sognato. Mio marito dorme. */

SELECT * FROM accessi_badge WHERE stazione= 'Vecchia Fiera' AND ora BETWEEN '01:11:00' AND '01:13:00'
/* 143	B-0451	Vecchia Fiera	2026-10-14	01:12:37	servizio */

SELECT * FROM dipendenti WHERE badge='B-0451'
/* M-394	300	manutentore	Notte 3	B-0451 */

SELECT * FROM persone WHERE id=300
/* 300	Ugo	Ferri	Via Indice Zero	4	manutentore */

SELECT *
FROM dipendenti
WHERE persona_id=300 OR persona_id=181
/* M-394	300	manutentore	Notte 3	B-0451
M-611	181	manutentore	Notte 3	B-6097 */

SELECT *
FROM ferie
WHERE matricola='M-394' OR matricola='M-611'
/* 5	M-394	2026-10-05	2026-10-18	Cagliari */

SELECT * FROM abbonamenti WHERE   persona_id=300
/* MN-4471	300	annuale	2027-07-13 */

SELECT * FROM dipendenti WHERE squadra='Notte 3'

SELECT * FROM tornelli WHERE   abbonamento= 'MN-7731'

SELECT verifica_mandante('Furio	Ganassi');
/* Lui ha staccato il vagone, d'accordo. Ma chi l'ha pagato? */

SELECT * from telefoni WHERE persona_id=181
/* 345 8857702	181	cellulare */

SELECT * from bonifici WHERE a_persona=181 

SELECT * from persone WHERE id=232
/* 232	Ercole	Ravanelli	Via delle Parentesi	15	ristoratore */