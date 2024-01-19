import pygame
from game import Game
from pygame.locals import QUIT

pygame.font.init()
pygame.init()

# Création de l'instance du jeu
if __name__ == "__main__":
    game = Game()
    game.init_game()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_button_click(event)

        game.update()

    pygame.quit()
