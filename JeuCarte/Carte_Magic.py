from Carte import Carte

class CarteMagic(Carte):
    def __init__(self, cout, mana, illustration, description, attaque=None, pv=None):
        Carte.values = (0, 1, 2, 3, 4, 5, 6)
        Carte.colors = ("plaine", "ile", "montagne", "foret", "marais")
        super().__init__(cout, mana)
        self.__illustration = illustration
        self.__description = description
        self.__attaque = attaque
        self.__pv = pv

    def getIllustration(self):
        return self.__illustation
    def setIllustration(self, illustration):
        self.__illustration = illustration
    illustration = property(getIllustration, setIllustration)

    def getDescription(self):
        return self.__description
    def setDescription(self, description):
        self.__description = description
    description = property(getDescription, setDescription)

    def getAttaque(self):
        return self.__attaque
    def setAttaque(self, attaque):
        self.__attaque = attaque
    attaque = property(getAttaque, setAttaque)

    def getPv(self):
        return self.__pv
    def setPv(self, pv):
        self.__pv = pv
    pv = property(getPv, setPv)

    @staticmethod
    def validation(cout, mana):
        if mana not in Carte.colors:
            print("Erreur : {} n'est pas un type de mana valide".format(mana))
            exit(1)
        if cout < 0 or cout > 6:
            print("Erreur :  Les valeurs doivent etre comprise entre 0 et 6")
            exit(1)

    def __str__(self):
        return "Carte  {} : {}".format(self.color, self.description)