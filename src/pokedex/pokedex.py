import json

class pokedex:
    def __init__(self, pokedex_list):
        self.pokedex_list = pokedex_list
        
    def load_json(self):
        pokedex = 'pokedex.load'
        with open(pokedex, 'r') as a:
            data = json.load(a)
            return f"{self.pokedex_list}"