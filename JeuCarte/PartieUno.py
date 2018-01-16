from Joueur import Joueur
from JeuUno import JeuUno

class PartieUno:
    Defausse = []
    cartesValides = []
    def __init__(self, joueur):
        self.__joueur = joueur
        self.__ordinateur1 = Joueur('C3PO', 'Droid')
        self.__ordinateur2 = Joueur('D2', 'R2')
        self.__ordinateur3 = Joueur('9000', 'HAL')
        self.__jeu = JeuUno()

    def demarrerPartie(self):
        self.__melanger()
        self.__distribuer()
        self.__premiereCarte()


        poursuivre = True
        Tour = 1
        while poursuivre:
            if Tour == 1:
                poursuivre = self.__tour(self.__joueur, self.Defausse)
                Tour += 1
            elif Tour == 2:
                poursuivre = self.__tour(self.__ordinateur1, self.Defausse)
                Tour += 1
            elif Tour == 3:
                poursuivre = self.__tour(self.__ordinateur2, self.Defausse)
                Tour += 1
            elif Tour == 4:
                poursuivre = self.__tour(self.__ordinateur3, self.Defausse)
                Tour += 1
            else:
                Tour =1


    def __melanger(self):
        self.__jeu.melanger()

    def __distribuer(self):
        for i in range(7):
            self.__joueur.ajouterCarte(self.__jeu.tirer())
            self.__ordinateur1.ajouterCarte(self.__jeu.tirer())
            self.__ordinateur2.ajouterCarte(self.__jeu.tirer())
            self.__ordinateur3.ajouterCarte(self.__jeu.tirer())

    def __premiereCarte(self):
        Defausse = self.Defausse
        Defausse.append(self.__jeu.cartes[0])
        self.__jeu.cartes.pop(0)
        while Defausse[0].value == 4:
            Defausse.insert(0, self.__jeu.cartes[0])
            self.__jeu.cartes.pop(0)
        print('La première carte est :' + str(Defausse[0]))
        self.Defausse = Defausse

    def __main(self, joueur):


        return True

    def finPartie(self, perdant1, perdant2, perdant3, gagnant):
        perdant1.defaites += 1
        perdant2.defaites += 1
        perdant3.defaites += 1
        gagnant.victoires += 1
        print('{} {} a gagné!'.format(gagnant.prenom, gagnant.nom))

    def __validation(self, carteJouee, carteJoueur):
        if carteJoueur.value != carteJouee.value:
            if carteJoueur.color != carteJouee.color:
                if carteJoueur.color != 4:
                    return False
        carteJoueur
        return True

    def __tour(self, joueur, jeu):
        print("La carte en jeu est :" + str(jeu[0]))
        if jeu[0].value > 14:
            return True
        else:
            mainJoueur = joueur.paquet.cartes
            if len(mainJoueur) > 0:
                for i in range(len(mainJoueur)):
                    if self.__validation(mainJoueur[i], jeu[0]):
                        self.cartesValides.insert(0, mainJoueur[i])
                print("Au tour de : {} {}".format(joueur.prenom, joueur.nom))
                print("Vos cartes sont : " + str(mainJoueur) + " ")
                if len(self.cartesValides) > 0:
                    print("Les cartes que vous pouvez jouer sont :" + str(self.cartesValides))
                    self.Defausse.insert(0, self.cartesValides[0])
                    self.cartesValides.pop(0)
                else:
                    print("Vous ne pouvez pas jouer, vous piochez une carte")
                    joueur.ajouterCarte(self.__jeu.tirer(True))
                if len(mainJoueur) > 0:
                    return True
        return False
