from JeuCartes import JeuCartes

class Paquet(JeuCartes):

    def __init__(self):
        super().__init__()

    def ajouter(self, carte):
        self.cartes.append(carte)

    def __add__(self, carte):
        self.ajouter(carte)