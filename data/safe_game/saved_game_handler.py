
import json

PATH_FILE = 'data/safe_game/run_data'


def serialize_player_full(player):

    sword = (player.equipment['sword']).code if player.equipment['sword'] != None else None
    shield = (player.equipment['shield']).code if player.equipment['shield'] != None else None

    serialized_player = {
        'max_hp': player.max_hp,
        'hp': player.hp,
        'base_damage': player.base_damage,
        'damage': player.damage,
        'base_defense': player.base_defense,
        'defense': player.defense,
        'sprite': player.sprite,
        'x': player.x,
        'y': player.y,
        'alter_status': player.alter_status,
        'inv_limit': player.inv_limit,
        'inventory': [item.code for item in player.inventory],
        'equipment': [sword, shield],
        'exp': player.exp,
        'level': player.level,
        'state': player.state
    }
    return serialized_player

def serialize_map(map_data):
    items_in_map = []
    for row in map_data:
        serialized_row = []
        for item in row:
            if not(isinstance(item, str)):
                serialized_row.append('.')
                items_in_map.append({
                    'code': item.code,
                    'x': item.x,
                    'y': item.y
                })
    return items_in_map

def save_run(map_data, player, map_range, map_name):
    items_in_map = serialize_map(map_data)
    serialized_player = serialize_player_full(player)
    
    with open(f'{PATH_FILE}.json', 'w') as file:
        json.dump({
            'player_data': serialized_player,
            'map_name': map_name,
            'map_range': map_range,
            'items': items_in_map
        }, file, indent=4)
