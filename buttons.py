# import tkinter as tk
# from tkinter import messagebox

# class InterfaceUtilisateur:
# def init(self, jeu):
# self.jeu = jeu

#     self.fenetre = tk.Tk()
#     self.fenetre.title("Pokémon Game")

#     self.bouton_nouvelle_partie = tk.Button(self.fenetre, text="Nouvelle Partie", command=self.commencer_partie)
#     self.bouton_nouvelle_partie.pack()

#     self.bouton_combat = tk.Button(self.fenetre, text="Combat", command=self.commencer_combat)
#     self.bouton_combat.pack()

# def commencer_partie(self):
#     self.jeu.commencer_partie()
#     messagebox.showinfo("Information", "Nouvelle partie commencée!")

# def commencer_combat(self):
#     adversaire = "Adversaire Pokémon"  # Remplacez par la logique de choix d'adversaire
#     self.jeu.effectuer_combat(adversaire)
#     messagebox.showinfo("Information", "Combat commencé contre {}".format(adversaire))

# def demarrer_interface(self):
#     self.fenetre.mainloop()
    
# Exemple d'utilisation
# jeu_pokemon = Jeu()
# interface = InterfaceUtilisateur(jeu_pokemon)
# interface.demarrer_interface()