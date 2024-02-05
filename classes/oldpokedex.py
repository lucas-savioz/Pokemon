import json
import os
import pygame

def add_pokemon(pokemon):
    # Vérifie si le Pokémon existe
    if not os.path.exists('pokedex.json'):
        # Si pokedex.json n'existe pas, création d'une liste vide
        saved_pokemon = []
    else:
        # Charger les Pokémon existants depuis pokedex.json
        try:
            with open('pokedex.json', 'r') as file:
                saved_pokemon = json.load(file)
        except json.JSONDecodeError:
            saved_pokemon = []
            
    # Vérifie si le Pokémon est déjà dans la liste
    if any(entry == pokemon for entry in saved_pokemon):
        print("Erreur : Ce Pokémon est déjà enregistré.")
        return False
    else:
        # Ajoute de nouveaux Pokémon dans la liste
        saved_pokemon.append(pokemon)
        
        # Ajoute le Pokémon dans le fichier pokedex.json
        with open('pokedex.json', 'w') as file:
            json.dump(saved_pokemon, file)
            
        print("Pokémon rajouté avec succès dans 'pokedex.json'")
        return True
    
while True:
    pkmn = input("Veuillez entre le nom d'un starter de la G1 : ")
    
    if pkmn == "Bulbizarre":
        print("bulbizarre")
    
    if pkmn == "Salamèche":
        print("salameche")
            
    if pkmn == "Carapuce":
        print("carapuce")
        
    break