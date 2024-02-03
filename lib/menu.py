import pygame
from lib.combat import Combat
from lib.pokemon import Pokemon

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
        pygame.mixer.music.play(-1)  # -1 pour répéter la musique indéfiniment
        self.button_click_sound = pygame.mixer.Sound("assets/sounds/button_click.mp3")  # Effet sonore du clic

        # Création d'une instance de joueur et d'adversaire
        self.player = Pokemon("Joueur", 100, "eau", 5)
        self.enemy = Pokemon("Adversaire", 100, "plante", 5)

    def new_game(self):
        if self.new_game_button.collidepoint(pygame.mouse.get_pos()):
            self.button_click_sound.play()  # Jouer le son du clic
            self.show_buttons = True  # Afficher les boutons après le clic
            self.message_intro = ""  # Effacer le message introductif
            combat_instance = Combat(self.player, self.enemy)  # Crée une instance de combat
            combat_instance.combat_process()  # Lance le combat

    def continue_game(self):
        if self.load_game_button.collidepoint(pygame.mouse.get_pos()):
            self.button_click_sound.play()  # Jouer le son du clic
            self.show_buttons = True
            self.message_intro = ""
            # Instance de combat en cours à faire ...

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



    # def wipe(screen, clacks, rate, old, new):
    #     self.draw_text("Lancement d'une nouvelle partie")

    #     screen.blit(old, (0, 0))
    #     screnn_arr = pygame.PixelArray(screen)
    #     new_arr = pygame.PixelArray(new)

    #     for i in range(rate):
    #         screen_arr[i::rate] = new_arr[i::rate]

    #         pygame.display.flip()
    #         clacks.clock.tick(rate)