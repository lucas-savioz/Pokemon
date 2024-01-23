import pygame
from lib.menu import Menu
from pygame.locals import QUIT

class Game:
    def __init__(self):
        pygame.font.init()
        pygame.init()

        self.running = True
        self.menu = Menu()

    # Initialisation du jeu
    def init_game(self):
        while self.running:  # Boucle de jeu
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.menu.handle_button_click(event)

            # Rafraîchir l'écran
            self.menu.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.init_game()