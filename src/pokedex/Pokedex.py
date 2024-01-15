import json
pokedex = 'pokedex.json'


with open(pokedex, 'r') as a:
    data = json.load(a)
    print(data)