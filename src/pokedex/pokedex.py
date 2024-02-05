# appending doesn't work as expected (lines, 29, 44 and 59): instead of separating objects properly, the script adds unnecessary curly braces in between objects, effectively rendering the json file that's being appended to unusable unless the user edits it manually afterwards, which they're not supposed to

# importing modules
import json
from os import path

# check if output file exists and load it
filename = 'full_pokedex.json'

if path.isfile(filename) is False:
    raise Exception("File not found")

with open("full_pokedex.json", "r") as read_file:
  input_file_dict = json.load(read_file)

# input field (for testing purposes)
pkmn = input("Enter the name of a G1 starter Pokémon: ")

# write Bulbasaur in json file    
if pkmn == "Bulbasaur":
    inc_id_list = [1]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Data added to Pokédex")

# write Charmander in json file
if pkmn == "Charmander":
    inc_id_list = [4]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Data added to Pokédex")

# write Squirtle in json file        
if pkmn == "Squirtle":
    inc_id_list = [7]

    output_dict = dict()

    for id in input_file_dict.keys():
        if int(id) in inc_id_list:
            output_dict[id] = input_file_dict.get(id)
        
    with open('pokedex.json', 'a') as output_json_file:
        json.dump(output_dict, output_json_file, indent = 1, separators=(',',": "), ensure_ascii=False)
    
    print("Data added to Pokédex")