from Carte import Carte


class CarteUno(Carte):

    def __init__(self, val, col):
        Carte.colors = ("Bleue", "Rouge", "Jaune", "Vert", "Noire")
        Carte.values = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Changement de sens", "Interdiction de jouer", "+2 Cartes", "Change couleur", "+4 change couleur")
        super().__init__(val, col)

    @staticmethod
    def validation(val, col):
        if val < 0 or val > 15:
            print("Erreur, Cette valeur n'est pas comprise entre 0 et 15")
            exit(1)
        if col < 0 or col > 5:
            print("Erreur, Ce code couleur n'est pas compris entre 0 et 5")
            exit(1)
