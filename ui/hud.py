
import shutil, os, sys, time

import config.setting as setting
from getpass import getpass
from config import setting
from items.basic_equip import BasicEquip
from items.basic_item import BasicItem
from items.basic_environment_item import BasicEnvironmentItem
from npc.basic_enemy import BasicEnemy
from world.start_world_elements import Player
from common_utilities import *
from data import classes_handler
from colorama import init, Fore
from common_utilities import color_mappings

init(autoreset=True)

def print_hud(game_map, player):
    
    os.system(setting.get_clear_cmd())
    
    # map update
    game_map[player.x][player.y] = player
    for line in game_map:
        floor = '' 
        for sq in line:
            if isinstance(sq, (BasicEnemy, Player, BasicEquip, BasicItem, BasicEnvironmentItem)):
                sq = f"{sq.color}{sq.sprite}{Fore.RESET}"
            floor += str(sq)
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
    print(f'{(setting.get_language())["game"]["hud"]["inventory"]}: [{inventory_items}]')

    sword = f'{(player.equipment["sword"]).color}{(player.equipment["sword"]).name}{Fore.RESET}' if player.equipment["sword"] else 'NO'
    shield = f'{(player.equipment["shield"]).color}{(player.equipment["shield"]).name}{Fore.RESET}' if player.equipment["shield"] else 'NO'
    
    print(f'{(setting.get_language())["game"]["hud"]["weapon"]}: [{sword}]. {(setting.get_language())["game"]["hud"]["shield"]}: [{shield}].')

def print_full_inventory(player):
    print('\n-----Inventario-----')
    if player.inventory:
        for i, item in enumerate(player.inventory, start=1):
            print(f'{i}. {item.color}{item.name}{Fore.RESET}.')
    else:
        print(Fore.RED + 'VACÍO')
    print('--------------------\n')

def print_full_equip(player):
    sword = player.equipment.get("sword", 'NO').name if player.equipment["sword"] else 'NO'
    shield = player.equipment.get("shield", 'NO').name if player.equipment["shield"] else 'NO'

    print('\n-----EQUIPAMENTO-----\n'
          f'1. {sword}\n'
          f'2. {shield}\n'
          '---------------------\n')

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

def print_almanac(almanac):
    print(f'\n---------------------ALMANAQUE---------------------')
    if len(almanac) >= 1:
        for item in almanac:
            class_ = (classes_handler.get_class(item["code"]))()
            print(f'\n---------{class_.color}{class_.name}{Fore.RESET}-----------\n'
                f'- description: {class_.desc}.\n'
                f'- sprite: {class_.color}{class_.sprite}{Fore.RESET}.\n'
                f'- rarity: {(color_mappings.get_enemy_taxonomy_mapping()).get(class_.rarity)}{Fore.RESET}.'
            )
            try:
                print(
                f'- damage: {class_.damage}.\n'
                f'- defense: {class_.defense}.\n'
                f'- critic: {class_.critic}.')
            except:
                pass
    else:
        print(Fore.LIGHTYELLOW_EX + 'No hay registros.')
    getpass('')

def print_bestiary(bestiary):
    print(f'\n---------------------BESTIARIO---------------------')
    if len(bestiary) >= 1:
        for beast in bestiary:
            monster = (classes_handler.get_class(beast["code"]))()
            print(f'---------{monster.color}{monster.name}{Fore.RESET}-----------\n'
                f'- description: {monster.descrip}\n'
                f'- sprite: {monster.color}{monster.sprite}{Fore.RESET}.\n'
                f'- taxonomy: {monster.color}{(color_mappings.get_enemy_taxonomy_mapping()).get(monster.taxonomy)}{Fore.RESET}.\n'
                f'- exp: {monster.exp}.\n'
                f'- range: {monster.range}.\n'
                f'- hp: {monster.hp}.\n'
                f'- damage: {monster.damage}.\n'
                f'- defense: {monster.defense}.\n'
            )
    else: print(Fore.LIGHTYELLOW_EX + 'No hay registros.')
    getpass('')

def print_languaje_options():
    
    list_files = (os.listdir('config/data/languajes'))
    files_names = []
    for i in list_files:
        if i[0] != '_':
            files_names.append(i.replace('.json', ''))
    
    for i, it in enumerate(files_names, start=1):
        print(f'{i}. {it}.')
    return files_names

def print_title_style(s):

    def center_string(string):
        columns, rows = shutil.get_terminal_size()  # Obtener el tamaño de la terminal
        centered_string = "\n" * ((rows // 2) - (string.count('\n') // 2))  # Centra verticalmente
        for line in string.splitlines():
            centered_string += line.center(columns) + "\n"  # Centra horizontalmente
        return centered_string

    simbols = ['_','(',')','~','|']
    for i, c in enumerate(center_string(s)):
        color = Fore.LIGHTYELLOW_EX if c == '~' else Fore.LIGHTBLACK_EX if c in simbols else Fore.WHITE
        c = '█' if c == '*' else c
        sys.stdout.write(color + c + Fore.RESET)
        sys.stdout.flush()
        time.sleep(0.001)

def print_effect(s, color = Fore.RESET):
    for c in s:
        sys.stdout.write(color + c)
        sys.stdout.flush()
        time.sleep(0.05)
