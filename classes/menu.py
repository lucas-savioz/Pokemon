import pygame
from classes.combat import Combat
from classes.pokemon import Pokemon

########## Eléments de classe Menu ##########

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 900))  # Création de la fenêtre
        pygame.display.set_caption("Pokémon : Chen's Exploration")
        self.clock = pygame.time.Clock()  # Fréquence d'action
        self.framerate = 60  # Taux de rafraîchissement
        self.font = pygame.font.Font(None, 30)  # Police pour le texte des boutons
        self.button_color = (0, 128, 255)  # Couleur des boutons
        self.new_game_button = pygame.Rect(200, 250, 400, 50)
        self.load_game_button = pygame.Rect(200, 320, 400, 50)
        self.background_menu = pygame.image.load("assets/img/menu/background_intro.jpg")  # Background intro
        self.message_intro = "Veuillez cliquer pour commencer"
        self.show_buttons = True
        pygame.mixer.music.load("assets/sounds/Title_Screen_intro.mp3")  # Audio preface intro
        pygame.mixer.music.play(-1)  # Répéte la musique indéfiniment
        self.button_click_sound = pygame.mixer.Sound("assets/sounds/button_click.mp3")  # Effet sonore du clic

    ########## Nouvelle Partie ##########
        
    def new_game(self):
        if self.new_game_button.collidepoint(pygame.mouse.get_pos()):
            self.button_click_sound.play()
            self.show_buttons = True
            self.message_intro = ""
            player = Pokemon("Joueur", 100, "eau", "carapuce_back.png")  # Créez le Pokémon du joueur
            combat_instance = Combat(player, None)  # Créez l'instance de combat avec le joueur
            enemy = combat_instance.create_enemy()  # Créez un ennemi aléatoire
            combat_instance.enemy = enemy  # Mettez à jour l'ennemi dans l'instance de combat
            combat_instance.combat_process()  # Lancez le combat

    ########## Charger une partie existante ##########

    def continue_game(self):
        if self.load_game_button.collidepoint(pygame.mouse.get_pos()):
            self.button_click_sound.play()  # Jouer le son du clic
            self.show_buttons = True
            self.message_intro = ""
            # Instance de combat en cours à faire ...

    ########## Boucle du menu ##########

    def loop_menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.new_game()  # Vérifie si on clique sur "Nouvelle Partie"
                    self.continue_game()  # Vérifie si on clique sur "Continuer la partie"

            self.screen.blit(self.background_menu, (0, 0))
            pygame.draw.rect(self.screen, self.button_color, self.new_game_button)
            pygame.draw.rect(self.screen, self.button_color, self.load_game_button)

            new_game_text = self.font.render("Nouvelle Partie", True, (255, 255, 255))
            load_game_text = self.font.render("Continuer la partie", True, (255, 255, 255))
            self.screen.blit(new_game_text, (self.new_game_button.x + 50, self.new_game_button.y + 15))
            self.screen.blit(load_game_text, (self.load_game_button.x + 50, self.load_game_button.y + 15))

            pygame.display.flip()
            self.clock.tick(self.framerate)