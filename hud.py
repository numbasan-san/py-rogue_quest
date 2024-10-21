
import os
from data.config import config
from items.basic_item import basic_item
from items.basic_equip import basic_equip
from items.basic_environment_item import basic_environment_item
from npc.basic_enemy import basic_enemy as enemy
from start_world_elements import player as _player_
from common_utilities import *
from colorama import init, Fore

init(autoreset=True)

def print_hud(game_map, player):
    
    os.system(config.load_config())
    
    # map update
    game_map[player.x][player.y] = player

    # map print
    for line in game_map:
        floor = ''.join(
            f"{sq.color}{sq.sprite}{Fore.RESET}" if isinstance(sq, (enemy, _player_, basic_item, basic_equip, basic_environment_item)) else sq 
            for sq in line
        )
        print(floor)

    def get_hp_status(player): # to get player's HP %
        hp_ratio = player.hp / player.max_hp
        if hp_ratio > 0.74:
            return Fore.LIGHTGREEN_EX
        elif 0.5 <= hp_ratio <= 0.74:
            return Fore.LIGHTYELLOW_EX
        elif 0.15 <= hp_ratio < 0.5:
            return Fore.LIGHTRED_EX
        return Fore.RED

    # print player's stats
    hp_status = get_hp_status(player)
    print(f'{hp_status}HP: {player.hp}/{player.max_hp}{Fore.RESET}. '
          f'Atk: {player.damage}/{player.base_damage}. '
          f'Def: {player.defense}/{player.base_defense}. '
          f'Lvl(Exp): {player.level}({player.exp}).')

    inventory_items = ', '.join(item.sprite for item in player.inventory)
    print(f'Inventario: [{inventory_items}]')

    sword = f'{(player.equipment["sword"]).color}{(player.equipment["sword"]).name}{Fore.RESET}' if player.equipment["sword"] else 'NO'
    shield = f'{(player.equipment["shield"]).color}{(player.equipment["shield"]).name}{Fore.RESET}' if player.equipment["shield"] else 'NO'
    
    print(f'Arma: [{sword}]. Escudo: [{shield}].')

def print_full_inventory(player):
    print('\n-----Inventario-----')
    if player.inventory:
        for i, item in enumerate(player.inventory, start=1):
            print(f'{i}. {item.name}.')
    else:
        print(Fore.RED + 'VACÍO')
    print('--------------------\n')

def print_full_equip(player):
    sword = player.equipment.get("sword", 'NO').name if player.equipment["sword"] else 'NO'
    shield = player.equipment.get("shield", 'NO').name if player.equipment["shield"] else 'NO'

    print('\n-----EQUIPAMENTO-----')
    print(f'1. {sword}')
    print(f'2. {shield}')
    print('---------------------\n')

def print_item_stats(equip):
    text = f'{equip.name.upper()}'
    print(f'\n-----ESTADÍSTICAS: {equip.color}{text}{Fore.RESET}-----')

    # mapping equipment attributes, excluding somes attributes
    attributes = {
        k: v for k, v in vars(equip).items() if k not in ['name', 'battle_effect', 'x', 'y', 'func', 'color', 'to_player', 'sprite', 'nonfunc']
    }

    # attribute's print
    for attr, value in attributes.items():
        if attr == "rarity": # if the object have "rarity", print the color
            print(f'- {attr.capitalize()}: {equip.color}{value}{Fore.RESET}.')
        else:
            print(f'- {attr.capitalize()}: {value}.')

    print('-------------------' + ('-' * len(text)) + '-----\n')
