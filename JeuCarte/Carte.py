class Carte:
    colors = None
    values = None

    def __init__(self, val, col):
        if self.__class__ is Carte:
            raise Exception("Création Interdite")
        self.__class__.validation(val, col)
        self.__value = val
        self.__color = col

    def __getValeur(self):
        return self.__value

    def __setValeur(self, val):
        self.__value = val
    value = property(__getValeur, __setValeur)

    def __getCouleur(self):
        return self.__color

    def __setCouleur(self, col):
        self.__color = col
    color = property(__getCouleur, __setCouleur)

    @staticmethod
    def validation(val, col):
        pass

    def __str__(self):
        return str(Carte.values[self.value]) + " de " + Carte.colors[self.color]

    def affiche_ascii(self):
        nom = str(Carte.values[self.value]) + " de " + Carte.colors[self.color]
        taille = len(nom) + 2
        print("/", "-" * taille, "\\", sep="")
        print("|", " " * taille, "|", sep="")
        print("|", nom, "|")
        print("|", " " * taille, "|", sep="")
        print("\\", "-" * taille, "/", sep="")

