import pygame


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 720)) # Création de la fenètre
        pygame.display.set_caption("Pokémon : Chen's Exploration")
        self.clock = pygame.time.Clock() # Fréquence d'action
        self.framerate = 60 # Taux de rafraichissment
        self.font = pygame.font.Font(None, 30) # Police pour le texte des boutons
        self.button_color = (0, 128, 255)  # Couleur des boutons
        self.button_hover_color = (0, 180, 255)  # Couleur des boutons lorsqu'ils sont survolés
        self.new_game_button_rect = pygame.Rect(200, 250, 400, 50)
        self.load_game_button_rect = pygame.Rect(200, 320, 400, 50)

    # Met à jour la fenètre
    def update(self): 
        pygame.display.flip()
        pygame.display.update()
        self.clock.tick(self.framerate)
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, self.button_color, self.new_game_button_rect)  # Bouton Nouvelle Partie
        pygame.draw.rect(self.screen, self.button_color, self.load_game_button_rect)  # Bouton Charger une partie existante
    
        # Texte des boutons
        new_game_text = self.font.render("Nouvelle Partie", True, (255, 255, 255))
        load_game_text = self.font.render("Charger une partie existante", True, (255, 255, 255))

        # Centrer le texte dans les boutons
        new_game_text_rect = new_game_text.get_rect(center=self.new_game_button_rect.center)
        load_game_text_rect = load_game_text.get_rect(center=self.load_game_button_rect.center)

        self.screen.blit(new_game_text, new_game_text_rect)
        self.screen.blit(load_game_text, load_game_text_rect)


    def get_size(self):
        return self.display.get_size()
    
    def get_display(self):
        return self.display