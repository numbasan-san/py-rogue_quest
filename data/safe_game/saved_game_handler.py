
from player import player as player
from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from npc.basic_enemy import basic_enemy as basic_enemy
from items.basic_environment_item import basic_environment_item as basic_environment_item

PATH_FILE = 'data/safe_game/run_data'

import json

def serialize_object(object):
    serialized_objects = []

    if isinstance(object, (basic_item, basic_enemy, basic_equip, basic_environment_item)):
        serialized_objects.append({
            'code': object.code
        })
    elif isinstance(object, (player)):
        serialized_objects.append(
            serialize_player_full(object)
        )

    return serialized_objects

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
    serialized_map = []
    for row in map_data:
        serialized_row = []
        for item in row:
            if isinstance(item, str):
                serialized_row.append(str(item))
            else:
                serialized_row.append(serialize_object(item))
        serialized_map.append(serialized_row)
    return serialized_map

def save_run(map_data, player,map_range):
    serialized_map = serialize_map(map_data)
    serialized_player = serialize_object(player)
    
    with open(f'{PATH_FILE}.json', 'w') as file:
        json.dump({'player_data': serialized_player, 'map_data': serialized_map, 'map_range': map_range}, file, indent=4)
