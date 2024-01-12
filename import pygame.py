import pygame

pygame.init()

# Crée une fenêtre
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Ma première fenêtre Pygame")

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mettez ici le reste du code pour votre jeu

import tkinter as tk
from tkinter import messagebox

class InterfaceUtilisateur:
def init(self, jeu):
self.jeu = jeu

    self.fenetre = tk.Tk()
    self.fenetre.title("Pokémon Game")

    self.bouton_nouvelle_partie = tk.Button(self.fenetre, text="Nouvelle Partie", command=self.commencer_partie)
    self.bouton_nouvelle_partie.pack()

    self.bouton_combat = tk.Button(self.fenetre, text="Combat", command=self.commencer_combat)
    self.bouton_combat.pack()

def commencer_partie(self):
    self.jeu.commencer_partie()
    messagebox.showinfo("Information", "Nouvelle partie commencée!")

def commencer_combat(self):
    adversaire = "Adversaire Pokémon"  # Remplacez par la logique de choix d'adversaire
    self.jeu.effectuer_combat(adversaire)
    messagebox.showinfo("Information", "Combat commencé contre {}".format(adversaire))

def demarrer_interface(self):
    self.fenetre.mainloop()


pygame.quit()




