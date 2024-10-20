
import os

from data.config import config as config
from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from items.basic_environment_item import basic_environment_item as basic_environment_item
from npc.basic_enemy import basic_enemy as enemy
from start_world_elements import player as _player_

from utilities import *
from colorama import *

# Inicializar colorama
init(autoreset=True)

def print_hud(game_map, player):
    os.system(config.load_config())
    
    # player print
    game_map[player.x][player.y] = player

    # map print
    for line in game_map:
        floor = ''
        for sq in line:
            if isinstance(sq, (enemy, _player_, basic_item, basic_equip, basic_environment_item)):
                floor += f"{sq.color}{str(sq.sprite)}{Fore.RESET}"  # Aplica el color del enemigo
            else:
                floor += sq  # Añade los muros directamente
        print(floor)
    # map print end #

    # print player stats
    print(f'HP: {player.hp}/{player.max_hp}. Atk: {player.damage}/{player.base_damage}. Def: {player.defense}/{player.base_defense}. Lvl(Exp): {player.level}({player.exp}).')
    # print player stats end #

    # inventory's print
    inventory = ''
    for i in range(len(player.inventory)):
        slot = (player.inventory[i].sprite + ', ') if i < (len(player.inventory) - 1) else player.inventory[i].sprite
        inventory += slot
    # inventory's print end #

    print(f'Inventario: [{inventory}]')

    sword = 'NO' if player.equipment["sword"] is None else (player.equipment["sword"]).name
    shield = 'NO' if player.equipment["shield"] is None else (player.equipment["shield"]).name
    print(Fore.CYAN + f'Arma: [{sword}]. Escudo: [{shield}].')

def print_full_inventory(player):
    print(Fore.MAGENTA + '\n-----Inventario-----')
    if player.inventory:
        for i in range(len(player.inventory)):
            print(f'{i + 1}. {(player.inventory[i]).name}.')
    else:
        print(Fore.RED + 'VACÍO')
    print('-------------------\n')

def print_full_equip(player):
    sword = 'NO' if player.equipment["sword"] is None else (player.equipment["sword"]).name
    shield = 'NO' if player.equipment["shield"] is None else (player.equipment["shield"]).name

    print(Fore.MAGENTA + '\n-----EQUIPAMENTO-----')
    print(f'1. {sword}')
    print(f'2. {shield}')
    print('-------------------\n')

def print_equip_stats(equip):
    text = f'-----ESTADÍSTICAS: {(equip.name).upper()}-----'
    print(f'\n{text}')
    attributes = vars(equip)
    skipped_attributes = ['battle_effect', 'x', 'y', 'func', 'to_player', 'sprite', 'nonfunc']
    for attr, value in attributes.items():
        if attr not in skipped_attributes:
            print(f'- {attr.capitalize()}: {value}.')
    print(('-' * len(text)) + '\n')
