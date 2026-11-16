"""PALESTRA · Una nave, come oggetto.

La classe è lo stampo, ogni nave è un biscotto fatto con lo stampo.
__init__ e descrivi sono già scritti. Voi completate i tre metodi con il TODO,
finché  pytest test_nave.py -v  è tutto verde.
"""


class Nave:
    def __init__(self, nome: str, capitano: str, cannoni: int) -> None:
        # self è "questa nave": ogni nave ha i suoi dati
        self.nome = nome
        self.capitano = capitano
        self.cannoni = cannoni
        self.bottino = 0  # ogni nave parte senza dobloni

    def descrivi(self) -> str:
        return f"{self.nome}, {self.cannoni} cannoni"

    def arrembaggio(self, dobloni: int) -> None:
        self.bottino += dobloni

    def perde_cannoni(self, quanti: int) -> None:
        self.cannoni -= quanti

        if self.cannoni < 0:
            self.cannoni = 0

        

    def e_pericolosa(self) -> bool:
        # TODO 3: True se la nave ha più di 30 cannoni, altrimenti False
        if self.cannoni > 30:
            return True
        else: 
            return False
