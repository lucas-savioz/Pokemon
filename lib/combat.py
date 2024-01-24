import pygame
import sys
from lib.pokemon import Pokemon
import random 

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
        self.input_rect = pygame.Rect(50, 550, 700, 30)  # Rectangle pour les saisies utilisateur
        self.status_bar_rect_joueur = pygame.Rect(220, 450, 300, 20)
        self.status_bar_rect_adversaire = pygame.Rect(700, 100, 300, 20)
        self.border_radius = 15 # Bords de la barre d'actions
        self.text_padding = 10
        self.input_active = False  # Indique si l'input est actif
        self.input_text = ''  # Texte entré par l'utilisateur

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
        pygame.time.wait(1500)
        pygame.display.flip()


    def draw_input(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.input_rect)
        text = self.font.render(self.input_text, True, (0, 0, 0))
        self.screen.blit(text, (self.input_rect.x + 5, self.input_rect.y + 5))
        pygame.display.flip()
    
    # Barre de status des pokemon
    def draw_status_bars(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.status_bar_rect_joueur)
        pygame.draw.rect(self.screen, (0, 255, 0), self.status_bar_rect_adversaire)

        joueur_percent_hp = self.joueur.point_de_vie / 100.0
        adversaire_percent_hp = self.adversaire.point_de_vie / 100.0

        joueur_width = int(self.status_bar_rect_joueur.width * joueur_percent_hp)
        adversaire_width = int(self.status_bar_rect_adversaire.width * adversaire_percent_hp)

        pygame.draw.rect(self.screen, (255, 0, 0), (self.status_bar_rect_joueur.x, self.status_bar_rect_joueur.y, joueur_width, self.status_bar_rect_joueur.height))
        pygame.draw.rect(self.screen, (255, 0, 0), (self.status_bar_rect_adversaire.x, self.status_bar_rect_adversaire.y, adversaire_width, self.status_bar_rect_adversaire.height))

        pygame.display.flip()

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Si l'utilisateur appuie sur Entrée, traiter l'input
                choix_attaque = self.input_text
                self.input_text = ''
                self.input_active = False
                self.handle_attack(choix_attaque)
            elif event.key == pygame.K_BACKSPACE:
                # Si l'utilisateur appuie sur Retour arrière, supprimer un caractère de l'input
                self.input_text = self.input_text[:-1]
            else:
                # Sinon, ajouter le caractère à l'input
                self.input_text += event.unicode

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
        degats = 10 * efficacite  # Dégats reçus en fonction de l'efficacité
        self.adversaire.point_de_vie -= degats
        self.draw_text(f"{self.joueur.nom} attaque {self.adversaire.nom} avec {self.joueur.attaque_1} et lui inflige {degats} points de dégâts !")

    def attaque_2(self):
        soins = random.randint(10, 30)  # Soins aléatoires entre 10 et 30
        self.joueur.point_de_vie += soins
        self.draw_text(f"{self.joueur.nom} utilise {self.joueur.attaque_2} et recouvre {soins} points de vie !")

    def attaque_adversaire(self):
        efficacite = self.calculer_efficacite()
        degats = 10 * efficacite

        # Attaque spécifique en fonction du type de l'adversaire
        if self.adversaire.type == "feu":
            attaque = "Flamèche"
        elif self.adversaire.type == "eau":
            attaque = "Bulle d'eau"
        else:
            attaque = "Fouet"

        self.joueur.point_de_vie -= degats
        self.draw_text(f"{self.adversaire.nom} attaque {self.joueur.nom} avec {attaque} et lui inflige {degats} points de dégâts!")


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
            self.draw_status_bars()

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