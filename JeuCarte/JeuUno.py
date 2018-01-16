from JeuCartes import JeuCartes
from CarteUno import CarteUno


class JeuUno(JeuCartes):
    def __init__(self):
        super().__init__()

    def initialiser(self):
        for val in range(10):
            for col in range(4):
                self.cartes.append(CarteUno(val, col))
        for i in range(2):
            for val in range(10, 13):
                for col in range(4):
                    self.cartes.append(CarteUno(val, col))
        for i in range(4):
            for val in range(13, 15):
                self.cartes.append(CarteUno(val, 4))
