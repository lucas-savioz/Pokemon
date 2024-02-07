import pygame
import sys
from classes.pokemon import Pokemon
import random
from pygame.locals import QUIT

########## Eléments de classe combat ##########

class Combat:
    def __init__(self, player, enemy=None):
        pygame.init()
        self.player = player
        self.enemy = enemy
        self.screen = pygame.display.set_mode((1200, 900))
        self.clock = pygame.time.Clock()
        self.background_combat = pygame.image.load("assets/img/map/background_combat.jpg")
        self.image_player = pygame.image.load("assets/img/sprites/pokemon_joueur/carapuce_back.png")
        self.image_enemy = [
            pygame.image.load("assets/img/sprites/adversaire/salameche_face.png"),
            pygame.image.load("assets/img/sprites/adversaire/carapuce_face.png"),
            pygame.image.load("assets/img/sprites/adversaire/bulbizarre_face.png")
        ]
        self.font = pygame.font.Font(None, 36)
        self.bar_hp_player = pygame.Rect(220, 450, 300, 20)
        self.bar_hp_enemy = pygame.Rect(700, 100, 300, 20)
        self.border_radius = 15
        self.text_padding = 10
        self.text_actions = pygame.Rect(30, 600, 800, 120)
        self.action_btn_weight = 150
        self.action_btn_height = 120
        self.button_color_base = (173, 216, 230)
        self.button_color_hover = (25, 25, 112)
        self.button_rect_1 = pygame.Rect(850, 700, self.action_btn_weight, self.action_btn_height)
        self.button_rect_2 = pygame.Rect(1020, 700, self.action_btn_weight, self.action_btn_height)
        self.button_click_sound = pygame.mixer.Sound("assets/sounds/button_click.mp3")

    def create_enemy(self):
        # Choix aléatoire entre Salamèche, Carapuce ou Bulbizarre
        enemy_name = random.choice(["Salamèche", "Carapuce", "Bulbizarre"])
        
        # Mapper les noms d'ennemis aux types et images correspondants
        enemy_info = {
            "Salamèche": ("feu", "salameche_face.png"),
            "Carapuce": ("eau", "carapuce_face.png"),
            "Bulbizarre": ("plante", "bulbizarre_face.png")
        }

        # Obtien les informations de l'ennemi en fonction de son nom
        enemy_type, enemy_image = enemy_info[enemy_name]

        # Création d'une instance de Pokemon avec le nom, les points de vie, le type, l'image et le niveau de l'ennemi
        enemy = Pokemon(enemy_name, 100, enemy_type, enemy_image, 1)
        return enemy

    def combat_process(self):
        # Arrêter la musique du menu
        pygame.mixer.music.stop()

        self.screen.blit(self.background_combat, (0, 0))
        pygame.mixer.music.load("assets/sounds/battle.mp3")  # Charger la musique de combat
        pygame.mixer.music.play(-1)  # Jouer la musique en boucle indéfiniment
        pygame.display.flip()
        pygame.time.wait(1000)  # Attendre 1 seconde pour que la musique commence avant de passer à la suite du combat


        # Position de la barre de texte d'actions de combat
        self.text_actions.y = 700

        # Affichage du message de début de combat
        self.draw_text_actions(f"Un combat commence entre {self.player.name} et {self.enemy.name}!")

        pygame.display.flip()
        pygame.time.wait(2000)  # Attendre 2 secondes avant d'afficher l'image du joueur

        # Redessiner le fond pour s'assurer que le message est au-dessus de l'image du joueur
        self.screen.blit(self.background_combat, (0, 0))

        # Afficher l'image du joueur
        self.screen.blit(self.image_player, (220, 500))  # Position de l'image pour le player

        pygame.display.flip()
        pygame.time.wait(2000)  # Attendre 2 secondes pour afficher les images

        # Affiche l'image de l'ennemie
        self.screen.blit(random.choice(self.image_enemy), (700, 250))

        # Déclaration de la variable pour stocker le message
        self.message = ""

        while self.player.hp > 0 and self.enemy.hp > 0:
            # Affichage des éléments du combat
            self.draw_hp_bars()
            self.draw_info_bars()
            self.draw_buttons()

            # Affichage du message
            self.draw_text_actions(self.message)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isdigit() and event.unicode in ["1", "2"]:
                        self.handle_attack(event.unicode)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_button_click(mouse_pos)

            # Actions du combat
            choice_atk = self.get_user_input("Choisissez votre attaque", self.button_rect_1, self.button_rect_2)
            if choice_atk == "1":
                self.atk_1()
            elif choice_atk == "2":
                self.atk_2()
            else:
                self.draw_text_actions("Veuillez choisir une attaque valide.")
                pygame.display.flip()
                pygame.time.wait(500)


            # Vérifications de fin de combat
            if self.enemy.hp <= 0:
                self.message = f"{self.player.name} a gagné le combat!"
                break
            self.atk_enemy()  # Action d'attaque de l'adversaire
            if self.player.hp <= 0:
                self.message = f"{self.enemy.name} a gagné le combat!"
                break

            pygame.display.flip()  # Rafraîchir l'écran à chaque itération de la boucle
            pygame.mixer.music.stop()

    # Barre d'evenements en bas de la fenêtre de combat
    def draw_text_actions(self, message):
        pygame.draw.rect(self.screen, (255, 255, 255), self.text_actions, border_radius=self.border_radius)
        
        # Ajuster la taille de la police en fonction de la longueur du texte
        max_text_actions_width = self.text_actions.width - 2 * self.text_padding
        font_size = 36
        while self.font.size(message)[0] > max_text_actions_width:
            font_size -= 1
            self.font = pygame.font.Font(None, font_size)

        text = self.font.render(message, True, (0, 0, 0))
        
        text_actions = text.get_rect(topleft=(self.text_actions.x + self.text_padding, self.text_actions.y + self.text_padding))
        self.screen.blit(text, text_actions.topleft)
        
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.display.flip()

    ########## Barre d'information des pokemon ##########

    def draw_info_bars(self):
        # Paramètrage des barres d'infos joueur et ennemi
        info_bar_player = pygame.Rect(220, 400, 300, 80)
        info_bar_enemy = pygame.Rect(700, 50, 300, 80)
        
        pygame.draw.rect(self.screen, (255, 255, 255), info_bar_player, border_radius=self.border_radius)
        pygame.draw.rect(self.screen, (255, 255, 255), info_bar_enemy, border_radius=self.border_radius)

        self.draw_pokemon_info(self.player, info_bar_player)
        self.draw_pokemon_info(self.enemy, info_bar_enemy)

        pygame.display.flip()

    # Barres d'infos des pokemons
    def draw_pokemon_info(self, pokemon, info_bar_rect):
        font = pygame.font.Font(None, 24)
        info_text = f"{pokemon.name} {pokemon.type}          N.{pokemon.level}"  # Assurez-vous d'utiliser pokemon.name pour obtenir le nom de l'ennemi
        text = font.render(info_text, True, (0, 0, 0))
        # Ajuste la largeur de la barre d'information en fonction de la longueur du texte
        info_bar_rect.width = text.get_width() + 20  # Ajouter un espace de marge

        # Affiche le texte centré dans la barre d'information
        text_rect = text.get_rect(center=info_bar_rect.center)

        # Dessine la barre d'information mise à jour
        pygame.draw.rect(self.screen, (255, 255, 255), info_bar_rect, border_radius=self.border_radius)

        # Afficher la barre de vie
        self.screen.blit(text, text_rect.topleft)
        self.draw_hp_bars()

        
        pygame.display.flip()


    
    ########## Barre de vie des pokemon ##########
        
    def draw_hp_bars(self):
        # Création des paramètres des barres de vie joueur et ennemi
        pygame.draw.rect(self.screen, (0, 255, 0), (self.bar_hp_player.x + 10, self.bar_hp_player.y, self.bar_hp_player.width, self.bar_hp_player.height))
        pygame.draw.rect(self.screen, (0, 255, 0), (self.bar_hp_enemy.x + 10, self.bar_hp_enemy.y, self.bar_hp_enemy.width, self.bar_hp_enemy.height))
        
        # Affiche les points de vie du joueur et ennemi
        info_hp_player = f"{self.player.hp}"
        info_hp_enemy = f"{self.enemy.hp}"

        # Pourcentage de points de vie en fonction du nombre de points de vie du joueur et ennemi
        player_percent_hp = self.player.hp / 100.0
        enemy_percent_hp = self.enemy.hp / 100.0

        # Variation de la largeur de la barre de vie du joueur en fonction du pourcentage
        player_width = int(self.bar_hp_player.width * player_percent_hp)
        enemy_width = int(self.bar_hp_enemy.width * enemy_percent_hp)

        pygame.draw.rect(self.screen, (255, 0, 0), (self.bar_hp_player.x + 10, self.bar_hp_player.y, player_width, self.bar_hp_player.height))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.bar_hp_enemy.x + 10, self.bar_hp_enemy.y, enemy_width, self.bar_hp_enemy.height))

        # Couleur de base de la barre de vie du joeur
        player_color_bar = (0, 255, 0)  # Vert (en bonne santé)

        # Détermine l'état du pokemon joueur en fonction de son pourcentage de points de vie
        if player_percent_hp <= 0.6:
            player_color_bar = (255, 255, 0)  # Jaune (blessé)
        if player_percent_hp <= 0.2:
            player_color_bar = (255, 0, 0)  # Rouge (très faible)

        # Barre de vie du pokemon joueur fond gris
        pygame.draw.rect(self.screen, (192, 192, 192), (self.bar_hp_player.x + 10, self.bar_hp_player.y, self.bar_hp_player.width, self.bar_hp_player.height))  # Fond gris clair
        pygame.draw.rect(self.screen, player_color_bar, (self.bar_hp_player.x + 10, self.bar_hp_player.y, player_width, self.bar_hp_player.height))

        # Barre de vie du pokemon ennemi
        enemy_color_bar = (0, 255, 0)  # Vert (en bonne santé)
        if enemy_percent_hp <= 0.6:
            enemy_color_bar = (255, 255, 0)  # Jaune (blessé)
        if enemy_percent_hp <= 0.2:
            enemy_color_bar = (255, 0, 0)  # Rouge (très faible)

        # Barre de vie du pokemon ennemi
        pygame.draw.rect(self.screen, (192, 192, 192), (self.bar_hp_enemy.x + 10, self.bar_hp_enemy.y, self.bar_hp_enemy.width, self.bar_hp_enemy.height))  # Fond gris clair
        pygame.draw.rect(self.screen, enemy_color_bar, (self.bar_hp_enemy.x + 10, self.bar_hp_enemy.y, enemy_width, self.bar_hp_enemy.height))

        # Affiche les points de vie du joueur et ennemi
        font = pygame.font.Font(None, 24)
        text_player = font.render(info_hp_player, True, (0, 0, 0))
        text_enemy = font.render(info_hp_enemy, True, (0, 0, 0))

        # Centrer le texte dans les barres de vie
        text_player_hp_bar = text_player.get_rect(center=(self.bar_hp_player.x + 10 + player_width // 2, self.bar_hp_player.centery))
        text_enemy_hp_bar = text_enemy.get_rect(center=(self.bar_hp_enemy.x + 10 + enemy_width // 2, self.bar_hp_enemy.centery))

        self.screen.blit(text_player, text_player_hp_bar.topleft)
        self.screen.blit(text_enemy, text_enemy_hp_bar.topleft)

    
    ########## Boutons d'attaques ##########

    def draw_buttons(self):
        action_btn_weight = self.action_btn_weight  # largeur des boutons
        action_btn_height = self.action_btn_height  # hauteur des boutons

        # Calcul des positions, largeurs, hauteurs, des buttons en fonction de l'espacement et de la largeur des buttons
        x_button_1 = 850
        y_button_1 = 700
        self.button_rect_1 = pygame.Rect(x_button_1, y_button_1, action_btn_weight, action_btn_height)

        x_button_2 = 1020
        y_button_2 = 700
        self.button_rect_2 = pygame.Rect(x_button_2, y_button_2, action_btn_weight, action_btn_height)

        pygame.draw.rect(self.screen, (0, 200, 255), self.button_rect_1, border_radius=self.border_radius)  # Couleur bleue pour le button 1
        pygame.draw.rect(self.screen, (0, 200, 255), self.button_rect_2, border_radius=self.border_radius)  # Couleur bleue pour le button 2

        font = pygame.font.Font(None, 36)

        text_atk_1 = font.render(self.player.atk_1, True, (255, 255, 255))
        text_actions_atk_1 = text_atk_1.get_rect(center=self.button_rect_1.center)
        self.screen.blit(text_atk_1, text_actions_atk_1)

        text_atk_2 = font.render(self.player.atk_2, True, (255, 255, 255))
        text_actions_atk_2 = text_atk_2.get_rect(center=self.button_rect_2.center)
        self.screen.blit(text_atk_2, text_actions_atk_2)

        pygame.display.flip()

    def check_button_click(self, mouse_pos):
        # Vérifie si le clic est sur le bouton 1 ou le bouton 2
        if self.button_rect_1.collidepoint(mouse_pos):
            self.atk_1()  # Exécute l'attaque 1
        elif self.button_rect_2.collidepoint(mouse_pos):
            self.atk_2()  # Exécute l'attaque 2

    def get_user_input(self, message, button_rect_1, button_rect_2):
        # Affichage du message
        self.draw_text_actions(message)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Vérification du clic de souris sur les boutons
                    if button_rect_1.collidepoint(mouse_pos):
                        self.button_click_sound.play()  # Lecture du son du clic
                        return "1"
                    elif button_rect_2.collidepoint(mouse_pos):
                        self.button_click_sound.play()  # Lecture du son du clic
                        return "2"


    def calculer_efficacite(self):
        # Obtenez le type de l'ennemi
        enemy_type = self.enemy.type

        # Vérifie le type de l'ennemi et détermine l'efficacité des attaques du joueur
        if enemy_type == "feu":
            return 2  # Dégâts x2
        elif enemy_type == "eau":
            return 1  # Dégâts normaux (x1)
        elif enemy_type == "plante":
            return 0.5  # Dégâts réduits de moitié (x0.5)


    # Attaque 1 du joueur
        
    def atk_1(self):
        # Calculer l'efficacité des dégâts en fonction du type de l'ennemi
        efficacite = self.calculer_efficacite()

        # Calculer les dégâts infligés par l'attaque
        degats = 20 * efficacite  # Dégâts de l'attaque 1

        # Affiche le message en fonction de l'efficacité des dégâts
        if efficacite > 1:
            self.draw_text_actions(f"{self.player.name} attaque {self.enemy.name} avec {self.player.atk_1} c'est super efficace !")
        elif efficacite < 1:
            self.draw_text_actions(f"{self.player.name} attaque {self.enemy.name} avec {self.player.atk_1} ce n'est pas très efficace !")
        else:
            self.draw_text_actions(f"{self.player.name} attaque {self.enemy.name} avec {self.player.atk_1}")

        # Affiche les dégâts infligés à l'ennemi
        self.draw_text_actions(f"{self.enemy.name} perd {degats} points de vie !")

        # Applique les dégâts à l'ennemi
        self.enemy.hp -= degats


    # Attaque 2 du joueur
    def atk_2(self):
        soins = random.randint(20, 40)  # Soins aléatoires entre 20 et 40
        self.player.hp += soins
        self.draw_text_actions(f"{self.player.name} utilise {self.player.atk_2} et recouvre {soins} points de vie !")

    def atk_enemy(self):
        # Calcule l'efficacité des dégâts en fonction du type de l'ennemi
        efficacite = self.calculer_efficacite_enemy()

        # Calcule les dégâts infligés par l'attaque de l'ennemi
        degats = 20 * efficacite  # Dégâts de l'attaque de l'ennemi

        # Affiche le message en fonction de l'efficacité des dégâts de l'ennemi
        if efficacite > 1:
            self.draw_text_actions(f"{self.enemy.name} attaque {self.player.name} avec {self.enemy.atk_enemy} c'est super efficace !")
        elif efficacite < 1:
            self.draw_text_actions(f"{self.enemy.name} attaque {self.player.name} avec {self.enemy.atk_enemy} ce n'est pas très efficace !")
        else:
            self.draw_text_actions(f"{self.enemy.name} attaque {self.player.name} avec {self.enemy.atk_enemy}")

        # Affiche les dégâts infligés au joueur
        self.draw_text_actions(f"{self.player.name} perd {degats} points de vie !")

        # Appliquer les dégâts au joueur
        self.player.hp -= degats

    def calculer_efficacite_enemy(self):
        # Verifie le type de l'ennemi
        enemy_type = self.enemy.type

        # Ajuste l'attaque de l'ennemi en fonction de son type
        if enemy_type == "feu":
            self.enemy.atk_enemy = "Flammèche"
        elif enemy_type == "eau":
            self.enemy.atk_enemy = "Bulle d'eau"
        elif enemy_type == "plante":
            self.enemy.atk_enemy = "Fouet"

        # Vérifie le type de l'ennemi et détermine l'efficacité des attaques du joueur
        if enemy_type == "feu":
            return 0.5  # Dégâts réduits de moitié x0.5
        elif enemy_type == "eau":
            return 1  # Dégâts normaux x1
        elif enemy_type == "plante":
            return 2  # Dégâts x2


# Création des Pokémon et du combat
player = Pokemon("Carapuce", 100, "eau", "carapuce_back.png")

# Création de l'instance de combat avec le joueur
combat_instance = Combat(player, None)
# Détermine l'ennemi
enemy = None

# Met à jour l'ennemi dans combat_instance
combat_instance.enemy = enemy
pygame.quit()
