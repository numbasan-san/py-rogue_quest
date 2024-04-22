
import json
from player import player as Player
from data.safe_game.objects_handler import return_object

def load_world():
    # Cargar el mapa desde el archivo JSON
    with open('data/safe_game/run_data.json', 'r') as file:
        data = json.load(file)
        map_data = data['map_data']
    
    # Crear un array bidimensional para almacenar el mapa
    map_array = []
    
    # Procesar cada celda del mapa
    for row in map_data:
        row_array = []
        for cell in row:
            if isinstance(cell, list):
                for obj in cell:
                    if isinstance(obj, dict):
                        obj_instance = (return_object(obj['code'])()).start()
                        row_array.append(obj_instance.sprite)
                    else:
                        row_array.append(obj)
            else:
                row_array.append(cell)
        map_array.append(row_array)

    return map_array

def load_player(serialized_player):
    player_data = serialized_player[0]

    player = Player(
        hp=player_data['max_hp'],
        damage=player_data['base_damage'],
        defense=player_data['base_defense'],
        sprite=player_data['sprite'],
        x=player_data['x'],
        y=player_data['y'],
        alter_status=player_data['alter_status']
    )
    player.name = 'player'
    player.hp = player_data['hp']
    player.damage = player_data['damage']
    player.defense = player_data['defense']
    player.inv_limit = player_data['inv_limit']
    player.equipment = [((load_objects(obj)).sprite if (load_objects(obj)) != None else 'NO') for obj in player_data['equipment']]
    player.inventory = [((load_objects(obj)).sprite if (load_objects(obj)) != None else 'NO') for obj in player_data['inventory']]
    player.exp = player_data['exp']
    player.level = player_data['level']
    player.state = player_data['state']

    return player

def load_objects(obj):
    if obj is not None:
        return ((return_object(obj)()).start())
    return None
