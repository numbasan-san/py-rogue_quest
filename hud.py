
import os

from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from items.basic_environment_item import basic_environment_item as basic_environment_item
from npc.basic_enemy import basic_enemy as enemy
from start_world_elements import player

from utilities import *

def print_hud(__map, __player, level):
    os.system('cls')
    
    # player print
    __map[__player.x][__player.y] = __player

    # map print
    for line in __map:
        floor = ''
        for sq in line:
            if isinstance(sq, (basic_item, enemy, player, basic_equip, basic_environment_item)):
                sq = str(sq.sprite)
            floor += str(sq)
        print(floor)
    # map print end #

    # print player stats
    print(f'HP: {__player.hp}/{__player.max_hp}. Atk: {__player.damage}/{__player.base_damage}. Def: {__player.defense}/{__player.base_defense}. Lvl(Exp): {__player.level}({__player.exp}). Floor: {level}')
    # print player stats end #

    # inventory's print
    inventory = ''
    for i in range(len(__player.inventory)):
        slot = (__player.inventory[i].sprite + ', ') if i < (len(__player.inventory) - 1) else __player.inventory[i].sprite
        inventory += slot
    # inventory's print end #

    print(f'Inventario: [{inventory}]')

    sword = 'NO' if __player.equipment["sword"] == None else (__player.equipment["sword"]).name
    shield = 'NO' if __player.equipment["shield"] == None else (__player.equipment["shield"]).name
    print(f'Arma: [{sword}]. Escudo: [{shield}].')

def print_full_inventory(__player):

    print('\n-----Inventario-----')
    if __player.inventory != []:
        for i in range(len(__player.inventory)):
            print(f'{i + 1}. {(__player.inventory[i]).name}.')
    else:
        print('VACÍO')
    print('-------------------\n')

def print_full_equip(__player):
    
    sword = 'NO' if __player.equipment["sword"] == None else (__player.equipment["sword"]).name
    shield = 'NO' if __player.equipment["shield"] == None else (__player.equipment["shield"]).name

    print('\n-----EQUIPAMENTO-----')
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
