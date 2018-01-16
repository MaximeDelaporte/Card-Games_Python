
import random

class JeuCartes:

    def __init__(self, vide=False):
        if self.__class__ is JeuCartes:
                raise Exception("Creation interdite!")
        else:
            self.__cartes = []
            self.initialiser()

    def __getCartes(self):
        return self.__cartes

    def __setCartes(self, carte):
        self.__cartes.append(carte)
    cartes = property(__getCartes, __setCartes)

    def __str__(self):
        cartes_du_jeu = ""
        for carte in self.cartes:
            if cartes_du_jeu == "":
                cartes_du_jeu = str(carte)
            else:
                cartes_du_jeu += ", " + str(carte)
        return cartes_du_jeu

    def melanger(self):
        random.shuffle(self.cartes)

    def tirer(self, manuel=False):
        try:
            if manuel:
                input('Appuyer sur <Return> pour tirer une carte')
            return self.cartes.pop(0)
        except IndexError:
            print("Il n'y a plus de carte")
            return None

    def initialiser(self):
        pass
