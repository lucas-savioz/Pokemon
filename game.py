import pygame
from window import Window
from pygame.locals import QUIT

class Game:
    def __init__(self):
        self.running = True
        self.window = Window()

    # Initialisation du jeu
    def init_game(self):
        while self.running:  # Boucle de jeu
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.window.handle_button_click(event)

            # Rafraîchir l'écran
            self.window.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.init_game()
