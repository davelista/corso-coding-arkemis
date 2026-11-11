"""GRAN BURRONE · Il fascicolo dell'indagine

Questo file NON si tocca: sono le prove. Si legge, e si usa da indagine.py.

Dentro ci sono tre cose:
    PERSONE        un dizionario:      nome -> {"razza": ..., "fuma": True/False}
    TESTIMONIANZE  una lista di dizionari, uno per testimone
    SPOSTAMENTI    un dizionario:      nome -> lista dei suoi passaggi, in ordine di ora

Gli spostamenti vengono dal registro delle guardie elfiche: ogni passaggio
è l'ora in cui una persona è entrata in un luogo. Il registro parte a mezzanotte.
"""

PERSONE = {
    "Frodo": {"razza": "hobbit", "fuma": False},
    "Sam": {"razza": "hobbit", "fuma": False},
    "Merry": {"razza": "hobbit", "fuma": True},
    "Pipino": {"razza": "hobbit", "fuma": True},
    "Bilbo": {"razza": "hobbit", "fuma": True},
    "Gandalf": {"razza": "stregone", "fuma": True},
    "Aragorn": {"razza": "uomo", "fuma": True},
    "Boromir": {"razza": "uomo", "fuma": False},
    "Legolas": {"razza": "elfo", "fuma": False},
    "Gimli": {"razza": "nano", "fuma": True},
    "Elrond": {"razza": "elfo", "fuma": False},
}

TESTIMONIANZE = [
    {
        "chi": "Frodo",
        "testo": "Alle 23 l'Anello era sul comodino, con la sua catenina. "
        "All'alba non c'era più. Nella stanza c'era odore di erba pipa.",
    },
    {
        "chi": "Sam",
        "testo": "Ho fatto la guardia davanti alla porta di Frodo. All'1:05 è entrato Pipino "
        "a riprendersi la mantella: l'Anello era ancora sul comodino, l'ho visto io. "
        "All'1:15 sono sceso in cucina per uno spuntino. Quando sono tornato, alle 2, "
        "la porta era socchiusa. Ah: in corridoio ho sentito passi leggeri, a piedi nudi.",
    },
    {
        "chi": "Elrond",
        "testo": "La Sala del Fuoco è sorvegliata dai miei elfi tutta la notte. "
        "Stamattina l'abbiamo perquisita due volte: lì l'Anello non c'è.",
    },
    {
        "chi": "Legolas",
        "testo": "Ho passato la notte sulla terrazza a guardare le stelle. "
        "Verso l'1:30 qualcuno di piccolo ha attraversato il ponte, senza candela.",
    },
    {
        "chi": "Gandalf",
        "testo": "Ero in biblioteca, a leggere vecchie pergamene. Non mi sono mosso fino all'alba.",
    },
    {
        "chi": "Pipino",
        "testo": "Ho solo ripreso la mia mantella! E un pezzo di torta, ma quello in cucina.",
    },
    {
        "chi": "Gimli",
        "testo": "Ho dormito tutta la notte. Chi dice che russavo mente.",
    },
]

SPOSTAMENTI = {
    "Frodo": [
        {"ora": "00:00", "luogo": "Camera di Frodo"},
    ],
    "Sam": [
        {"ora": "00:00", "luogo": "Camera di Frodo"},
        {"ora": "01:15", "luogo": "Cucine"},
        {"ora": "02:00", "luogo": "Camera di Frodo"},
    ],
    "Merry": [
        {"ora": "00:00", "luogo": "Cucine"},
        {"ora": "00:45", "luogo": "Camera di Merry e Pipino"},
    ],
    "Pipino": [
        {"ora": "00:00", "luogo": "Cucine"},
        {"ora": "00:45", "luogo": "Camera di Merry e Pipino"},
        {"ora": "01:05", "luogo": "Camera di Frodo"},
        {"ora": "01:08", "luogo": "Camera di Merry e Pipino"},
        {"ora": "01:40", "luogo": "Cucine"},
        {"ora": "01:55", "luogo": "Camera di Merry e Pipino"},
    ],
    "Bilbo": [
        {"ora": "00:00", "luogo": "Camera di Bilbo"},
        {"ora": "01:20", "luogo": "Camera di Frodo"},
        {"ora": "01:28", "luogo": "Ponte"},
        {"ora": "01:31", "luogo": "Giardino"},
        {"ora": "01:49", "luogo": "Sala del Fuoco"},
        {"ora": "verso le due", "luogo": "Camera di Bilbo"},
    ],
    "Gandalf": [
        {"ora": "00:00", "luogo": "Biblioteca"},
    ],
    "Aragorn": [
        {"ora": "00:00", "luogo": "Sala del Fuoco"},
        {"ora": "00:50", "luogo": "Terrazza"},
        {"ora": "01:10", "luogo": "Stalle"},
        {"ora": "02:30", "luogo": "Camera di Aragorn"},
    ],
    "Boromir": [
        {"ora": "00:00", "luogo": "Terrazza"},
        {"ora": "01:00", "luogo": "Camera di Boromir"},
    ],
    "Legolas": [
        {"ora": "00:00", "luogo": "Terrazza"},
    ],
    "Gimli": [
        {"ora": "00:00", "luogo": "Camera di Gimli"},
    ],
    "Elrond": [
        {"ora": "00:00", "luogo": "Sala del Consiglio"},
        {"ora": "03:00", "luogo": "Sala del Fuoco"},
    ],
}
