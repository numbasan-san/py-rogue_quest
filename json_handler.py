
import json, maps_handler, random

'''
La idea es tener en una esquina todos los mapas en formato .txt.
En un archivo json aparte tendré todos los "objetos" en los que especificaré dónde quiero que aparezca el jugador.
'''

mapas = []

mapas.append(
    {
        'name': 'test_map',
        'player_spawn_coors': (5, 5),
        'map': maps_handler.set_map('test_map.txt')
    }
)
mapas.append(
    {
        'name': 'mapa copy',
        'player_spawn_coors': (1, 1),
        'map': maps_handler.set_map('mapa copy.txt')
    }
)

with open('maps_data.json', 'w') as file:
    json.dump(mapas, file, indent = 4)

def load_random_map():
    MAP = random.choice(json.load(open('maps_data.json', 'r')))
    return MAP

# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(mapas[1]['name'])