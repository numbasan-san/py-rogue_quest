
import json, random
# import maps_handler as maps_handler
import data.map_things.maps_handler as maps_handler
import data.map_things.map_classes.map_gene as map_gene

from world.player import *

FILE_PATH = 'data/map_things/maps_data.json'
# FILE_PATH = 'maps_data.json'
mapas = None

'''
La idea es tener en una esquina todos los mapas en formato .txt.
En un archivo json aparte tendré todos los "objetos" en los que especificaré dónde quiero que aparezca el jugador.
'''
def save_maps():
    mapas = []

    # mapas.append(
    #     {
    #         'name': 'test_map',
    #         'player_spawn_coords': (2, 1),
    #         'enemys_spawn_coords': [()],
    #         'items_spawn_coords': [(1, 2), (2, 2), (2, 3)],
    #         'map': maps_handler.set_map('test_map.txt')
    #     }
    # )

    mapas.append(
        {
            'name': 'test_map2',
            'player_spawn_coords': (1, 2),
            'enemys_spawn_coords': [(3, 3), (4, 3), (5, 1), (6, 2)],
            'stairs_spawn_coords': [(1, 3)],
            'items_spawn_coords': [(8, 3), (4, 3), (1, 1), (3, 5)],
            'map': maps_handler.set_map('test_map2.txt')
        }
    )

    with open(FILE_PATH, 'w') as file:
        json.dump(mapas, file, indent = 4)

# save_maps()

def load_random_map():
    MAP = random.choice(json.load(open(FILE_PATH, 'r')))
    # return json.load(open(FILE_PATH, 'r'))[0]
    return MAP

def load_procedural_map(player):
    map_width = 25
    map_height = 50
    max_rooms = 5
    room_min_size = 5
    room_max_size = 15
    game_map = map_gene.MapGene(map_width, map_height)
    game_map.make_map(max_rooms, room_min_size, room_max_size, map_width, map_height, player)
    return game_map

# with open('maps_data.json', 'r') as file:
#     data = json.load(open(FILE_PATH, 'r'))[0]
#     print(data)