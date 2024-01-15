import json

a = open("pokedex.json", "r")

data = json.load(a)

print(json.dumps(data, indent = 1))