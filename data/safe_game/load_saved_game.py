
import json
from player import player as Player
from data.safe_game.objects_handler import return_object

def load_map():
    # Cargar el mapa desde el archivo JSON
    maps_file = open('data/map_things/maps_data.json', 'r')
    run_file = open('data/safe_game/run_data.json', 'r')

    maps_data = json.load(maps_file)
    run_data = json.load(run_file)

    maps_list = maps_data
    for map_i in maps_list:
        if map_i['name'] == run_data['map_name']:
            map_data = map_i['map']
    
    # Procesar cada celda del mapa
    for obj in run_data['items']:
        obj_instance = (return_object(obj['code'])()).start(obj['x'], obj['y'])
        # obj_instance.x, obj_instance.y = obj['x'], obj['y']
        map_data[obj_instance.x][obj_instance.y] = obj_instance

    return map_data

def load_player():
    file = open('data/safe_game/run_data.json', 'r')
    data = json.load(file)
    serialized_player = (data['player_data'])
    player_data = serialized_player

    player = Player(
        hp=player_data['hp'],
        damage=player_data['damage'],
        defense=player_data['defense'],
        sprite=player_data['sprite'],
        x=player_data['x'],
        y=player_data['y'],
        alter_status=player_data['alter_status']
    )
    player.name = 'player'
    player.max_hp = player_data['max_hp']
    player.base_damage = player_data['base_damage']
    player.base_defense = player_data['base_defense']
    player.inv_limit = player_data['inv_limit']
    player.exp = player_data['exp']
    player.level = player_data['level']
    player.state = player_data['state']
    player.inventory = [((load_objects(obj)) if (load_objects(obj)) != None else 'NO') for obj in player_data['inventory']]

    equipment = [((load_objects(obj)) if (load_objects(obj)) != None else None) for obj in player_data['equipment']]
    player.equipment['sword'] = equipment[0]
    player.equipment['shield'] = equipment[1]

    return player

def load_objects(obj):
    if obj is not None:
        return ((return_object(obj)()).start())
    return None

def load_dungeon_range():
    file = open('data/safe_game/run_data.json', 'r')
    data = json.load(file)
    return (data['map_range'])
