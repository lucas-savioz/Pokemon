import pygame
import sys
from lib.pokemon import Pokemon
import random 

########## Eléments de classe combat ##########

class Combat:
    def __init__(self, joueur, adversaire):
        pygame.init()
        self.joueur = joueur
        # self.aversaire doit être random parmis les 3 pokemon
        self.adversaire = adversaire
        self.screen = pygame.display.set_mode((1200, 900))  # Ajoutez la taille de votre fenêtre
        self.clock = pygame.time.Clock()
        self.background_combat = pygame.image.load("assets/img/map/background_combat.jpg")
        self.image_joueur = pygame.image.load("assets/img/sprites/pokemon_joueur/carapuce_back.png")
        self.image_adversaire = pygame.image.load("assets/img/sprites/adversaire/salameche_face.png")
        self.font = pygame.font.Font(None, 36)
        self.text_rect = pygame.Rect(30, 600, 800, 120)  # Barre pour les messages d'actions
        self.status_bar_hp_joueur = pygame.Rect(220, 450, 300, 20)
        self.status_bar_hp_adversaire = pygame.Rect(700, 100, 300, 20)
        self.border_radius = 15 # Bords de la barre d'actions
        self.text_padding = 10
        espace_entre_boutons = 20
        self.bouton_largeur = 100
        self.x_bouton_1 = self.screen.get_width() // 2 - self.bouton_largeur - espace_entre_boutons // 2
        self.x_bouton_2 = self.screen.get_width() // 2 + espace_entre_boutons // 2
        self.input_active = False  # Indique si l'input est actif
        self.input_text = ''  # Texte entré par l'utilisateur

    ########## Boucle principale du combat ##########

    def deroulement_combat(self):

        self.screen.blit(self.background_combat, (0, 0))
        self.screen.blit(self.image_joueur, (220, 500))  # Position de l'image pour le joueur
        self.screen.blit(self.image_adversaire, (700, 250))  # Position de l'image pour l'adversaire
        pygame.display.flip()
        pygame.time.wait(2000)  # Attendre 2 secondes pour afficher les images
        # Position du rectangle de texte de début de combat
        self.text_rect.y = 700
        # Afficher le message de début de combat
        self.draw_text(f"Un combat commence entre {self.joueur.nom} et {self.adversaire.nom}!")

        # Boucle principale du combat
        while self.joueur.point_de_vie > 0 and self.adversaire.point_de_vie > 0:
            self.draw_hp_bars()  # Dessiner les barres de vie
            self.draw_buttons()  # Dessiner les boutons
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isdigit() and event.unicode in ["1", "2"]:
                        self.handle_attack(event.unicode)

                # Gestion des clics de souris sur les boutons
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    self.check_button_click(mouse_pos)

            # Actions du combat (attaques, vérifications, etc.)
            choix_attaque = self.get_user_input("Choisissez votre attaque : 1 ou 2 ", ["1", "2"])

            if choix_attaque == "1":
                self.attaque_1()
            elif choix_attaque == "2":
                self.attaque_2()
            else:
                self.draw_text("Veuillez choisir une attaque valide.")

            # Vérification si l'adversaire est toujours en vie
            if self.adversaire.point_de_vie <= 0:
                self.draw_text(f"{self.joueur.nom} a gagné le combat!")
                break

            # Action de l'adversaire
            self.attaque_adversaire()

            # Vérification si le joueur est toujours en vie
            if self.joueur.point_de_vie <= 0:
                self.draw_text(f"{self.adversaire.nom} a gagné le combat!")
                break

    def draw_text(self, message):
        pygame.draw.rect(self.screen, (255, 255, 255), self.text_rect, border_radius=self.border_radius)
        
        # Ajuster la taille de la police en fonction de la longueur du texte
        max_text_width = self.text_rect.width - 2 * self.text_padding
        font_size = 36
        while self.font.size(message)[0] > max_text_width:
            font_size -= 1
            self.font = pygame.font.Font(None, font_size)

        text = self.font.render(message, True, (0, 0, 0))
        
        text_rect = text.get_rect(topleft=(self.text_rect.x + self.text_padding, self.text_rect.y + self.text_padding))
        self.screen.blit(text, text_rect.topleft)
        
        pygame.display.flip()
        pygame.time.wait(2000)
        pygame.display.flip()

    
    ########## Barre de vie des pokemon ##########
        
    def draw_hp_bars(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.status_bar_hp_joueur)
        pygame.draw.rect(self.screen, (0, 255, 0), self.status_bar_hp_adversaire)

        joueur_percent_hp = self.joueur.point_de_vie / 100.0
        adversaire_percent_hp = self.adversaire.point_de_vie / 100.0

        # Variation de la largeur de la barre de vie en fonction du pourcentage
        joueur_width = int(self.status_bar_hp_joueur.width * joueur_percent_hp)
        adversaire_width = int(self.status_bar_hp_adversaire.width * adversaire_percent_hp)

        pygame.draw.rect(self.screen, (255, 0, 0), (self.status_bar_hp_joueur.x, self.status_bar_hp_joueur.y, joueur_width, self.status_bar_hp_joueur.height))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.status_bar_hp_adversaire.x, self.status_bar_hp_adversaire.y, adversaire_width, self.status_bar_hp_adversaire.height))

        # Couleur de base des barres de vie
        joueur_color = (0, 255, 0)  # Vert (en bonne santé)

        # Déterminez l'état du pokemon joueur en fonction de son pourcentage de points de vie
        if joueur_percent_hp <= 0.6:
            joueur_color = (255, 255, 0)  # Jaune (blessé)
        if joueur_percent_hp <= 0.2:
            joueur_color = (255, 0, 0)  # Rouge (très faible)

        # Barre de vie du pokemon joueur fond gris
        pygame.draw.rect(self.screen, (192, 192, 192), self.status_bar_hp_joueur)  # Fond gris clair
        pygame.draw.rect(self.screen, joueur_color, (self.status_bar_hp_joueur.x, self.status_bar_hp_joueur.y, joueur_width, self.status_bar_hp_joueur.height))

        # Barre de vie du pokemon adversaire
        adversaire_color = (0, 255, 0)  # Vert (en bonne santé)
        if adversaire_percent_hp <= 0.6:
            adversaire_color = (255, 255, 0)  # Jaune (blessé)
        if adversaire_percent_hp <= 0.2:
            adversaire_color = (255, 0, 0)  # Rouge (très faible)

        pygame.draw.rect(self.screen, (192, 192, 192), self.status_bar_hp_adversaire)  # Fond gris clair
        pygame.draw.rect(self.screen, adversaire_color, (self.status_bar_hp_adversaire.x, self.status_bar_hp_adversaire.y, adversaire_width, self.status_bar_hp_adversaire.height))
    
    def draw_buttons(self):
        bouton_largeur = 150  # Modifiez la largeur des boutons selon vos besoins

        # Calcul des positions des boutons en fonction de l'espacement et de la largeur des boutons
        x_bouton_1 = 700
        y_bouton_1 = 720
        self.button_rect_1 = pygame.Rect(x_bouton_1, y_bouton_1, bouton_largeur, 100)

        x_bouton_2 = 1200
        y_bouton_2 = 700
        self.button_rect_2 = pygame.Rect(x_bouton_2, y_bouton_2, bouton_largeur, 100)

        pygame.draw.rect(self.screen, (0, 200, 255), self.button_rect_1, border_radius=self.border_radius)  # Couleur bleue pour le bouton 1
        pygame.draw.rect(self.screen, (0, 200, 255), self.button_rect_2, border_radius=self.border_radius)  # Couleur bleue pour le bouton 2

        font = pygame.font.Font(None, 36)

        text_attaque_1 = font.render(self.joueur.attaque_1, True, (255, 255, 255))
        text_rect_attaque_1 = text_attaque_1.get_rect(center=self.button_rect_1.center)
        self.screen.blit(text_attaque_1, text_rect_attaque_1)

        text_attaque_2 = font.render(self.joueur.attaque_2, True, (255, 255, 255))
        text_rect_attaque_2 = text_attaque_2.get_rect(center=self.button_rect_2.center)
        self.screen.blit(text_attaque_2, text_rect_attaque_2)

        pygame.display.flip()

    def check_button_click(self, mouse_pos):
        # Vérifier si le clic est sur le bouton 1
        if self.button_rect_1.collidepoint(mouse_pos):
            self.handle_attack("1")

        # Vérifier si le clic est sur le bouton 2
        elif self.button_rect_2.collidepoint(mouse_pos):
            self.handle_attack("2")

    def handle_attack(self, choix_attaque):
        if choix_attaque == "1":
            self.attaque_1()
        elif choix_attaque == "2":
            self.attaque_2()
        else:
            self.draw_text("Veuillez choisir une attaque valide.")

    def calculer_efficacite(self):
        type_joueur = self.joueur.type
        type_adversaire = self.adversaire.type

        if type_joueur == "eau":
            if type_adversaire == "plante":
                return 0.5
            elif type_adversaire == "feu":
                return 2
            else:
                return 1

    def attaque_1(self):
        efficacite = self.calculer_efficacite()
        degats = 20 * efficacite  # Dégats reçus en fonction de l'efficacité
        self.adversaire.point_de_vie -= degats
        self.draw_text(f"{self.joueur.nom} attaque {self.adversaire.nom} avec {self.joueur.attaque_1} et lui inflige {degats} points de dégâts !")

    def attaque_2(self):
        soins = random.randint(10, 30)  # Soins aléatoires entre 10 et 30
        self.joueur.point_de_vie += soins
        self.draw_text(f"{self.joueur.nom} utilise {self.joueur.attaque_2} et recouvre {soins} points de vie !")

    def attaque_adversaire(self):
        efficacite = self.calculer_efficacite()
        degats = 20 * efficacite

        # Attaque spécifique en fonction du type de l'adversaire
        if self.adversaire.type == "feu":
            attaque = "Flamèche"
        elif self.adversaire.type == "eau":
            attaque = "Bulle d'eau"
        else:
            attaque = "Fouet"

        self.joueur.point_de_vie -= degats
        self.draw_text(f"{self.adversaire.nom} attaque {self.joueur.nom} avec {attaque} et lui inflige {degats} points de dégâts!")

    def get_user_input(self, prompt, valid_inputs):
        self.input_active = True
        user_input = ""

        while self.input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isdigit() and event.unicode in valid_inputs:
                        user_input = event.unicode
                        self.input_active = False

        return user_input

# Création des Pokémon et du combat
joueur = Pokemon("Carapuce", 100, "eau")
adversaire = Pokemon("Salamèche", 100, "Feu")

combat_instance = Combat(joueur, adversaire)
combat_instance.deroulement_combat()

# Quitter pygame à la fin du programme
pygame.quit()
sys.exit()