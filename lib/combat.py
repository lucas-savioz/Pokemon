import pygame
import sys
from lib.pokemon import Pokemon
import random 

class Combat:
    def __init__(self, joueur, adversaire):
        self.joueur = joueur
        self.adversaire = adversaire

    def calculer_efficacite(self):
        type_joueur = self.joueur.type
        type_adversaire = self.adversaire.type

        if type_joueur == "eau":
            if type_adversaire == "plante":
                return 0.5
            elif type_adversaire == "feu":
                return 2
            else:
                return 1

    def attaque_1(self):
        efficacite = self.calculer_efficacite()
        degats = 10 * efficacite  # Dégats reçus en fonction de l'efficacité
        self.adversaire.point_de_vie -= degats
        print(f"{self.joueur.nom} attaque {self.adversaire.nom} avec {self.joueur.attaque_1} et lui inflige {degats} points de dégâts !")

    def attaque_2(self):
        soins = random.randint(10, 30)  # Soins aléatoires entre 10 et 30
        self.joueur.point_de_vie += soins
        print(f"{self.joueur.nom} utilise {self.joueur.attaque_2} et recouvre {soins} points de vie !")

    def attaque_adversaire(self):
        efficacite = self.calculer_efficacite()
        degats = 10 * efficacite
        self.joueur.point_de_vie -= degats
        print(f"{self.adversaire.nom} attaque {self.joueur.nom} avec {self.adversaire.attaque_1} et lui inflige {degats} points de dégâts!")

    def deroulement_combat(self):
        print(f"Un combat commence entre {self.joueur.nom} et {self.adversaire.nom}!")

        # Tant que les points de chacun des pokemon sont au dessus de zéro, la boucle while et la méthode attaque_adversaire continue
        while self.joueur.point_de_vie > 0 and self.adversaire.point_de_vie > 0:
            self.attaque_adversaire()

            if self.adversaire.point_de_vie <= 0:
                print(f"{self.joueur.nom} a gagné le combat!")
                break

            choix_attaque = input("Choisissez votre attaque : 1 ou 2 ")

            while choix_attaque not in ["1", "2"]:
                print("Veuillez choisir une attaque valide.")
                choix_attaque = input("Choisissez votre attaque : 1 ou 2 ")

            if choix_attaque == "1":
                self.attaque_1()
            elif choix_attaque == "2":
                self.attaque_2()

            if self.joueur.point_de_vie <= 0:
                print(f"{self.adversaire.nom} a gagné le combat!")
                break

joueur = Pokemon("Joueur", 100, "eau")
adversaire = Pokemon("Adversaire", 100, "plante")

combat_instance = Combat(joueur, adversaire)
combat_instance.deroulement_combat()