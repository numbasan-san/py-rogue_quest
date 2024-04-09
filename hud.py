
import os

from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from npc.basic_enemy import basic_enemy as enemy
from start_world_elements import player

from utilities import *

def print_hud(__map, __player):
    os.system('cls')
    
    # player print
    __map[__player.x][__player.y] = __player

    # map print
    for line in __map:
        floor = ''
        for sq in line:
            if isinstance(sq, (basic_item, enemy, basic_equip, player)):
                sq = str(sq.sprite)
            floor += str(sq)
        print(floor)
    # map print end #

    # print player stats
    print(f'HP: {__player.hp}/{__player.max_hp}. Atk: {__player.damage}/{__player.base_damage}. Def: {__player.defense}/{__player.base_defense}. Lvl(Exp): {__player.level}({__player.exp}).')
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

def print_full_invent(__player):

    print('\n-----Inventario-----')
    if __player.inventory != []:
        for i in range(len(__player.inventory)):
            print(f'{i + 1}. {(__player.inventory[i]).name}.')
    else:
        print('VACÍO')
    print('-------------------\n')
