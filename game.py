import pygame

from window import Window
from pygame.locals import QUIT

# Classe Game
class Game:
    def __init__(self):
        self.running = True
        self.window = Window()
    
    # Initialisation du jeu
    def init_game(self):
        while self.running: # Boucle de jeu
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
        
        self.window.update()

        pygame.quit()