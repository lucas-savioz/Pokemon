import pygame

pygame.init()

# Crée une fenêtre
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Ma première fenêtre Pygame")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettez ici le reste du code pour votre jeu

import tkinter as tk
from tkinter import messagebox

pygame.quit()




