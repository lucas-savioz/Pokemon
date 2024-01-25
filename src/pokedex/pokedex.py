# importing modules
import json
from os import path

# check if output file exists and load it
filename = 'pokedex_complet.json'

if path.isfile(filename) is False:
    raise Exception("File not found")

with open("pokedex_complet.json", "r") as read_file:
  input_file_dict = json.load(read_file)

# input field (for testing purposes)
pkmn = input("Veuillez entre le nom d'un starter de la G1 : ")

# write Bulbasaur in json file    
if pkmn == "Bulbizarre":
    inc_id_list = [1]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Données rajoutées au Pokédex")

# write Charmender in json file
if pkmn == "Salamèche":
    inc_id_list = [4]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Données rajoutées au Pokédex")

# write Squirtle in json file        
if pkmn == "Carapuce":
    inc_id_list = [7]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Données rajoutées au Pokédex")