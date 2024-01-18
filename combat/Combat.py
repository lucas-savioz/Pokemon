import pygame
import sys
from Pokemon import Pokemon

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

    def attaquer_adversaire(self):
        self.attaquer()
        if self.adversaire.point_de_vie <= 0:
            print(f"{self.joueur.nom} a gagné le combat!")

    def attaquer_joueur(self):
        adversaire_attaque = self.adversaire.attaquer(self.joueur)
        if adversaire_attaque:
            print(f"{self.adversaire.nom} attaque {self.joueur.nom} et lui inflige des dégâts!")
            if self.joueur.point_de_vie <= 0:
                print(f"{self.adversaire.nom} a gagné le combat!")

    def derouler_combat(self):
        print(f"Un combat commence entre {self.joueur.nom} et {self.adversaire.nom}!")

        while self.joueur.point_de_vie > 0 and self.adversaire.point_de_vie > 0:
            # Logique du combat ici...
            self.attaquer_adversaire()

            if self.adversaire.point_de_vie <= 0:
                break

            self.attaquer_joueur()

            if self.joueur.point_de_vie <= 0:
                break


# Initialisation Pygame et autres paramètres du jeu à ajouter ici
            


# Création d'une instance de la classe Pokemon pour le joueur
joueur = Pokemon("Joueur", 100, "feu", 20, 1.5, "Forêt volcanique", "Ce pokémon ne tient pas en place, il a toujours besoin d'être en activité")