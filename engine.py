
import os, input_handler, json_handler, random
import time
import basic_item, enemy

from utilities import *
from start_world_elements import *

class engine:

    def __init__(self):

        self.room_inv = {
            'item': None,
            'coor_x': 0,
            'coor_y': 0,
            'in_use': False
        }
        self.end_exe = False

        self.map_class = (json_handler.load_random_map())
        self.map = self.map_class['map']
        self.player = start_characters.return_player((self.map_class['player_spawn_coors'])[0], (self.map_class['player_spawn_coors'])[1])
        self.enemy = random.choice(start_characters.return_enemy())
        
        # items print
        for i in range(len(self.map_class['items_spawn_coors'])):
            self.item = random.choice(start_items.return_items()) # A random item selected

            # setting coors for each "item spawn coors" in the map in turn
            self.item.x = (((self.map_class['items_spawn_coors'])[i]))[0]
            self.item.y = (((self.map_class['items_spawn_coors'])[i]))[1]

            # item print
            self.map[self.item.x][self.item.y] = self.item
        # items print end #

        # enemy print
        self.map[self.enemy.x][self.enemy.y] = self.enemy

    def run(self):
        os.system('cls')

        # player print
        self.map[self.player.x][self.player.y] = self.player.sprite

        # map print
        for line in self.map:
            floor = ''
            for square in line:
                if type(square) == basic_item.basic_item:
                    square = square.sprite
                if type(square) == enemy.enemy:
                    square = square.sprite
                floor += square

            print(floor)
        # map print end #

        # inventory's print
        inventory = ''
        for i in range(len(self.player.inventory)):
            slot = (self.player.inventory[i].sprite + ', ') if i < (len(self.player.inventory) - 1) else self.player.inventory[i].sprite
            inventory += slot
        # inventory's print end #

        print(f'Inventario del jugador: [{inventory}]')

        # actions menu
        text = "1. Mirar inventario.\n2. Moverse."
        action = utilities.opciones('Elija una de las opciones:\n' + text + '\nElección', ['1', '2'])

        if action == '1': # look into inventory choice
            print('\n-----Inventario-----')
            if self.player.inventory != []:
                for i in range(len(self.player.inventory)):
                    print(f'{i + 1}. {(self.player.inventory[i]).name}.')
            else:
                print('VACÍO')

        if action == '2': # move choice
            self.move_selection()
        # actions menu end #

        input()

    def move_selection(self):

        # player flanks check
        player_around = [
            self.map[self.player.x - 1][self.player.y], # up
            self.map[self.player.x + 1][self.player.y], # down
            self.map[self.player.x][self.player.y - 1], # left
            self.map[self.player.x][self.player.y + 1], # right
        ]

        # move control
        move_vector = input_handler.valid_move(self.player.x, self.player.y, self.map, player_around)

        # vertical movement
        if move_vector['direc'] in ['w', 's']:
            moved_to = self.player.x + move_vector['move']
            self.load_move('x', move_vector, moved_to, self.player.y, moved_to)
        # vertical movement end #

        # horizontal movement
        elif move_vector['direc'] in ['a', 'd']:
            moved_to = self.player.y + move_vector['move']
            self.load_move('y', move_vector, self.player.x, moved_to, moved_to)
        # horizontal movement end #

    def load_move(self, axis, move_vector, x, y, move):
        sq = self.map[x][y]
        if type(sq) != enemy.enemy: # verifying if the next coor is an enemy

            # player's movement function
            self.movement(axis, move, move_vector['move'])
            print(move_vector['msg'])

        else:
            self.combat_logic(sq)

    # to save a item in the room
    def room_inv_save(self, item, x, y, in_use = True):
        self.room_inv['item'] = item
        self.room_inv['coor_x'] = x
        self.room_inv['coor_y'] = y
        self.room_inv['in_use'] = in_use

    # the player's movement
    def movement(self, axis, new_coor, move_vector):

        # setting the new coor and actuals coors
        new_player_coor = new_coor
        player_coor_x = self.player.x
        player_coor_y = self.player.y

        # the next map item/object
        thing = (self.map[new_player_coor][player_coor_y]) if axis == 'x' else (self.map[player_coor_x][new_player_coor])

        # if in the way there is an object/item
        if type(thing) == basic_item.basic_item:

            # if the player want, or not, take the item
            take_item = True if (utilities.opciones(f'¿Tomar {thing.name}?', ['y', 'n']) == 'y') else False

            if take_item and\
                 (len(self.player.inventory) < self.player.inv_limit): # if the object/item is taken and the inventory is in it's limit
                
                self.player.inventory.append(thing)

                if axis == 'x':
                    self.map[new_player_coor][player_coor_y] = '.'
                else:
                    self.map[player_coor_x][new_player_coor] = '.'

            else: # if not
                if axis == 'x':
                    self.room_inv_save(thing, new_player_coor, player_coor_y)
                else:
                    self.room_inv_save(thing, player_coor_x, new_player_coor)

        # player's axis move
        if axis == 'x': # in horizontal axis
            self.player.x = new_player_coor
        else: # in vertical axis
            self.player.y = new_player_coor
        # player's axis move end #

        if axis == 'x': # in horizontal axis
            self.floor_item_check(self.player.x, (self.player.x - move_vector), self.player.y, self.room_inv['coor_x'])
        else: # in vertical axis
            self.floor_item_check(self.player.y, self.player.x, (self.player.y - move_vector), self.room_inv['coor_y'])

    # to check if where the player is an object/item or just floor
    def floor_item_check(self, used_player_axis, player_x, player_y, room_inv_axis):
        if self.room_inv['in_use'] == True and\
            ((room_inv_axis < used_player_axis) or\
                ((room_inv_axis > used_player_axis))): # if it's an object/item
            self.map[room_inv_axis][room_inv_axis] = self.room_inv['item']
            self.room_inv_save(None, 0, 0, in_use = False)
        else: # if it's floor
            self.map[player_x][player_y] = '.'

    def combat_logic(self, enemy):
        print(f'Coordenadas del enemigo a atacar: ({enemy.x}, {enemy.y}).\nNombre del enemio: {enemy.name}.\n')
        enemy.hp -= self.player.damage
        self.player.hp -= enemy.damage

        print('Tanto tú como el enemigo se dieron un madrazo cruzado.')
        print(f'Salud del enemigo: {enemy.hp}.\nSalud del jugador: {self.player.hp}.\n')
