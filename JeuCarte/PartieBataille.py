from Joueur import Joueur
from JeuClassique import JeuClassique


class PartieBataille:

    def __init__(self, joueur):
        self.__joueur = joueur
        self.__ordinateur = Joueur('9000', 'HAL')
        self.__jeu = JeuClassique()

    def demarrerPartie(self):
        self.__melanger()
        self.__distribuer()

        poursuivre = True
        while poursuivre:
            poursuivre = self.__main()

    def __melanger(self):
        self.__jeu.melanger()

    def __distribuer(self):
        for i in range(len(self.__jeu.cartes)):
            carte = self.__jeu.tirer()
            if i % 2 == 0:
                self.__joueur.ajouterCarte(carte)
            else:
                self.__ordinateur.ajouterCarte(carte)

    def __main(self, reste=[]):
        carte_joueur = self.__joueur.tirerCarte(True)
        carte_ordinateur = self.__ordinateur.tirerCarte()

        if carte_joueur is None:
            self.finPartie(self.__joueur, self.__ordinateur)
            return False
        elif carte_ordinateur is None:
            self.finPartie(self.__ordinateur, self.__joueur)
            return False

        print("Main : ")
        print('   -{} {} : {}'.format(self.__joueur.prenom, self.__joueur.nom, str(carte_joueur)))
        print('   -{} {} : {}'.format(self.__ordinateur.prenom, self.__ordinateur.nom, str(carte_ordinateur)))

        if carte_joueur.value == carte_ordinateur.value:
            reste.append(carte_joueur)
            reste.append(carte_ordinateur)
            return self.__bataille(reste)
        elif carte_joueur.value > carte_ordinateur.value:
            self.__joueur.ajouterCarte(carte_joueur)
            self.__joueur.ajouterCarte(carte_ordinateur)
            print('   -{} {} gagne la main'.format(self.__joueur.prenom, self.__joueur.nom))
        else:
            self.__ordinateur.ajouterCarte(carte_ordinateur)
            self.__ordinateur.ajouterCarte(carte_joueur)
            print('   -{} {} gagne la main'.format(self.__ordinateur.prenom, self.__ordinateur.nom))

        return True

    def __bataille(self, reste):
        print('*** BATAILLE ***')
        return self.__main(reste)

    def finPartie(self, perdant, gagnant):
        perdant.defaites += 1
        gagnant.victoires += 1
        print('{} {} a gagné!'.format(gagnant.prenom, gagnant.nom))

