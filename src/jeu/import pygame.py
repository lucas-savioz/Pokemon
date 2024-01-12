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

class Game:
    def __init__(self):
        self.running = True
        self.screen = Screen()
        self.map = Map(self.screen)

    def run(self):
        while self.running:
            self.map.update()
            self.screen.update()

            
import tkinter as tk
from tkinter import messagebox

pygame.quit()




