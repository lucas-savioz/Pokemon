import pygame


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720)) # Création de la fenètre
        pygame.display.set_caption("Pokémon : Chen's Exploration")
        self.clock = pygame.time.Clock() # Fréquence d'action
        self.framerate = 60 # Taux de rafraichissment

    # Met à jour la fenètre
    def update(self): 
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.screen.fill((0, 0, 0))
    
    def get_size(self):
        return self.display.get_size()
    
    def get_display(self):
        return self.display