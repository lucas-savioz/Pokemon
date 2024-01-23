import pygame
from lib.combat import Combat
from lib.pokemon import Pokemon
from pygame.locals import QUIT

class Menu:
    def __init__(self):
        pygame.init()
        self.in_combat = False
        self.screen = pygame.display.set_mode((1200, 900))  # Création de la fenêtre
        pygame.display.set_caption("Pokémon : Chen's Exploration")
        self.clock = pygame.time.Clock()  # Fréquence d'action
        self.framerate = 60  # Taux de rafraîchissement
        self.font = pygame.font.Font(None, 30)  # Police pour le texte des boutons
        self.button_color = (0, 128, 255)  # Couleur des boutons
        self.button_hover_color = (0, 180, 255)  # Couleur des boutons lorsqu'ils sont survolés
        self.new_game_button_rect = pygame.Rect(200, 250, 400, 50)
        self.load_game_button_rect = pygame.Rect(200, 320, 400, 50)
        self.background_menu = pygame.image.load("assets/img/menu/background_intro.jpg")  # Background intro
        self.message_intro = "Veuillez cliquer pour commencer"
        self.show_buttons = True
        self.in_combat = False

        # Charger et jouer la musique
        pygame.mixer.music.load("assets/sounds/Title_Screen_intro.mp3")  # Audio preface_intro
        pygame.mixer.music.play(-1)  # -1 pour répéter la musique indéfiniment

        # Charger l'effet sonore pour le clic sur un bouton
        self.button_click_sound = pygame.mixer.Sound("assets/sounds/button_click.mp3")  # Effet sonore

        # Création d'une instance de la classe Pokemon pour le joueur
        self.joueur = Pokemon("Joueur", 100, "eau", 5)
        self.adversaire = Pokemon("Adversaire", 100, "plante", 5)
        self.combat_instance = Combat(self.joueur, self.adversaire)

    # Met à jour la fenêtre
    def update(self):
        if self.in_combat:
            self.combat_instance.update()
        else:
            pygame.display.flip()
            pygame.display.update()
            self.clock.tick(self.framerate)
            self.screen.fill((0, 0, 0))  # Fond noir

        # Affichage du fond interactif avec le message
        self.screen.blit(self.background_menu, (0, 0))

        # Affichage du message en bas
        message_text = self.font.render(self.message_intro, True, (255, 255, 255))
        message_rect = message_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() - 50))  # Position du message sur la fenêtre
        self.screen.blit(message_text, message_rect)

        # Si les boutons doivent être affichés, les afficher
        if self.show_buttons:
            pygame.draw.rect(self.screen, self.button_color, self.new_game_button_rect)
            pygame.draw.rect(self.screen, self.button_color, self.load_game_button_rect)

            # Texte des boutons
            new_game_text = self.font.render("Nouvelle Partie", True, (255, 255, 255))
            load_game_text = self.font.render("Charger une partie existante", True, (255, 255, 255))

            # Centrer le texte dans les boutons
            new_game_text_rect = new_game_text.get_rect(center=self.new_game_button_rect.center)
            load_game_text_rect = load_game_text.get_rect(center=self.load_game_button_rect.center)

            self.screen.blit(new_game_text, new_game_text_rect)
            self.screen.blit(load_game_text, load_game_text_rect)

    # Gère les clics sur les boutons
    def handle_button_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            # Vérifier si le clic est sur le bouton Nouvelle Partie
            if self.new_game_button_rect.collidepoint(mouse_pos):
                self.button_click_sound.play()  # Jouer le son du clic
                self.show_buttons = True  # Afficher les boutons après le clic
                self.message_intro = ""  # Effacer le message introductif

                # Démarrer le combat
                self.in_combat = True
                self.combat_instance.deroulement_combat()

            # Vérifier si le clic est sur le bouton Charger une partie existante
            elif self.load_game_button_rect.collidepoint(mouse_pos):
                self.button_click_sound.play()  # Jouer le son du clic

# Boucle principale du menu
menu = Menu()
menu_running = True
while menu_running:
    for event in pygame.event.get():
        if event.type == QUIT:
            menu_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            menu.handle_button_click(event)

    menu.update()
