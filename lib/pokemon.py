import pygame
import sys

class Pokemon:
    def __init__(self, nom, point_de_vie, type, niveau=1):
        self.nom = nom
        self.point_de_vie = point_de_vie
        self.type = type  # feu, eau, plante
        self.niveau = niveau  # Niveau initial
        self.statut_bar_exp = 0  # Barre d'expérience initiale
        self.attaque_1 = "Bulle d'eau"  # Ajoutez l'attaque 1 spécifique au Pokemon
        self.attaque_2 = "Soin"  # Ajoutez l'attaque 2 spécifique au Pokemon