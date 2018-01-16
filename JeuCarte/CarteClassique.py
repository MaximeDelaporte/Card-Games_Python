from Carte import Carte

class CarteClassique(Carte):

    def __init__(self, val, col):
        Carte.colors = ("Coeur", "Carreau", "Trefle", "Pique")
        Carte.values = (None, None, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Valet", "Dame", "Roi", "As")
        super().__init__(val, col)

    @staticmethod
    def validation(val, col):
        if val < 2 or val > 14:
            print("Erreur, Cette valeur n'est pas comprise entre 2 et 14")
            exit(1)
        if col < 0 or col > 3:
            print("Erreur, Ce code couleur n'est pas compris entre 0 et 3")
            exit(1)
