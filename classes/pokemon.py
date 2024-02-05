import pygame
import sys

class Pokemon:
    def __init__(self, name, hp, pokemon_type, image, level=1):
        self.name = name
        self.hp = hp
        self.type = pokemon_type  # "feu", "eau", "plante"
        self.level = level  # Niveau initial
        self.image = image
        self.statut_bar_exp = 0  # Barre d'expérience initiale
        self.atk_1 = "Bulle d'eau"  # Attaque 1 spécifique au Pokemon
        self.atk_2 = "Soin"  # Attaque 2 spécifique au Pokemon
