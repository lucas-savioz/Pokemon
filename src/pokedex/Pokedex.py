import json

with open('donnees_pokemon.json') as a:
    b = json.load(a)
    
print(json.dumps(b, indent=4, ensure_ascii=False))