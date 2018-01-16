from Paquet import Paquet

class Joueur:

    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
        self.__victoires = 0
        self.__defaites = 0
        self.__paquet = Paquet()

    def getNom(self):
        return self.__nom
    nom = property(getNom)

    def getPrenom(self):
        return self.__prenom
    prenom = property(getPrenom)

    def getVictoires(self):
        return self.__victoires
    def setVictoires(self, n):
        self.__victoires = n
    victoires = property(getVictoires, setVictoires)

    def getDefaites(self):
            return self.__defaites
    def setDefaites(self, n):
        self.__defaites = n
    defaites = property(getDefaites, setDefaites)

    def getPaquet(self):
        return self.__paquet
    paquet = property(getPaquet)

    def tirerCarte(self, manuel=False):
        if not manuel:
            return self.paquet.tirer(False)
        else:
            return self.paquet.tirer(True)

    def ajouterCarte(self, carte):
        self.paquet.ajouter(carte)

    def __str__(self):
        return "{} {}\nPalmares: {} defaite(s) et {} victoire(s)\n{}".format(self.prenom, self.nom, self.defaites, self.victoires, str(self.paquet))
