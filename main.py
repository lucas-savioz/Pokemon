import pygame

from game import Game

pygame.init()

# Création de l'instance du jeu
if __name__ == "__main__":
    game = Game()
    game.init_game()