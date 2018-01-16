from JeuCartes import JeuCartes
from CarteClassique import CarteClassique

class JeuClassique(JeuCartes):
    def __init__(self):
        super().__init__()

    def initialiser(self):
        for val in range(2, 15):
            for col in range(4):
                self.cartes.append(CarteClassique(val, col))
