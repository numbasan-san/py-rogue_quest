
import json, random
import data.map_things.maps_handler as maps_handler

FILE_PATH = 'data/map_things/maps_data.json'

'''
La idea es tener en una esquina todos los mapas en formato .txt.
En un archivo json aparte tendré todos los "objetos" en los que especificaré dónde quiero que aparezca el jugador.
'''
def save_maps():
    mapas = []

    mapas.append(
        {
            'name': 'test_map',
            'player_spawn_coors': (2, 1),
            'enemys_spawn_coors': [()],
            'items_spawn_coors': [(1, 2), (2, 2), (2, 3)],
            'map': maps_handler.set_map('test_map.txt')
        }
    )

    # mapas.append(
    #     {
    #         'name': 'mapa copy',
    #         'player_spawn_coors': (1, 2),
    #         'enemys_spwan_coors': [()],
    #         'items_spwan_coors': [()],
    #         'map': maps_handler.set_map('mapa copy.txt')
    #     }
    # )

    with open(FILE_PATH, 'w') as file:
        json.dump(mapas, file, indent = 4)

# save_maps()

def load_random_map():
    MAP = random.choice(json.load(open(FILE_PATH, 'r')))
    return json.load(open(FILE_PATH, 'r'))[0]

# with open('data.json', 'r') as file:
#     data = json.load(file)
#     print(mapas[1]['name'])