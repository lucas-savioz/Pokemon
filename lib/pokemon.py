import pygame
import sys

class Pokemon:
    def __init__(self, name, hp, type, level=1):
        self.name = name
        self.hp = hp
        self.type = type  # feu, eau, plante
        self.level = level  # Niveau initial
        self.statut_bar_exp = 0  # Barre d'expérience initiale
        self.atk_1 = "Bulle d'eau"  # Ajoutez l'attaque 1 spécifique au Pokemon
        self.atk_2 = "Soin"  # Ajoutez l'attaque 2 spécifique au Pokemon