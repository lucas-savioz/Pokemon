import pygame
import sys

class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire

    def calculer_efficacite(self):
        type_joueur = self.joueur.type
        type_adversaire = self.adversaire.type

        if type_joueur == "feu":
            if type_adversaire == "plante":
                return 2
            elif type_adversaire == "eau":
                return 0.5
            else:
                return 1
        elif type_joueur == "eau":
            if type_adversaire == "plante":
                return 0.5
            elif type_adversaire == "feu":
                return 2
            else:
                return 1
        elif type_joueur == "plante":
            if type_adversaire == "feu":
                return 0.5
            elif type_adversaire == "eau":
                return 2
            else:
                return 1
        else:  # type_joueur == "normal"
            return 1
    
    def attaquer(self):
        efficacite = self.calculer_efficacite()
        degats = 10 * efficacite  # Valeur arbitraire, à ajuster selon le besoin
        self.adversaire.point_de_vie -= degats
        print(f"{self.joueur.nom} attaque {self.adversaire.nom} et lui inflige {degats} points de dégâts!")
    