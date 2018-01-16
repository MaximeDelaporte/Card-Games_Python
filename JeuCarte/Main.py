from Joueur import Joueur

class Main:
    carteEnMain = []
    def __init__(self):
        self.__carteAutorisee()
        self.__carteEnMain()

    def __carteEnMain(self):
        global carteEnMain
        carteEnMain = Joueur.paquet()


