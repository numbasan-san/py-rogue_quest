
import os, input_handler, json_handler, random
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
        self.item = random.choice(start_items.return_items())

        # item print
        self.map[self.item.x][self.item.y] = self.item

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
                    square = self.item.sprite
                if type(square) == enemy.enemy:
                    square = self.enemy.sprite
                floor += square

            print(floor)

        # inventory's print
        inventory = ''
        for i in range(len(self.player.inventory)):
            slot = (self.player.inventory[i].sprite + ', ') if i < (len(self.player.inventory) - 1) else self.player.inventory[i].sprite
            inventory += slot

        print(f'Inventario del jugador: [{inventory}]')

        # actions menu
        text = "1. Mirar inventario.\n2. Moverse."
        action = utilities.opciones('Elija una de las opciones:\n' + text + '\nElección', ['1', '2'])

        if action == '1':
            print('\n-----Inventario-----')
            if self.player.inventory != []:
                for i in range(len(self.player.inventory)):
                    print(f'{i + 1}. {(self.player.inventory[i]).name}.')
            else:
                print('VACÍO')

        if action == '2':
            self.move_selection()

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
            sq = self.map[self.player.x + move_vector['move']][self.player.y]
            if type(sq) == str or type(sq) == basic_item.basic_item: # verifying if the next coor is a "wall"

                # player's movement function
                self.movement('x', self.player.x + move_vector['move'], move_vector['move'])
                print(move_vector['msg'])

            else:
                print('\n##################################################\nAviso: Es imposible desplazarse por esa dirección.\n##################################################\n')

        # horizontal movement
        elif move_vector['direc'] in ['a', 'd']:
            sq = self.map[self.player.x][self.player.y + move_vector['move']]
            if type(sq) == str or type(sq) == basic_item.basic_item: # verifying if the next coor is a "wall"

                # player's movement function
                self.movement('y', self.player.y + move_vector['move'], move_vector['move'])
                print(move_vector['msg'])

            else:
                print('\n##################################################\nAviso: Es imposible desplazarse por esa dirección.\n##################################################\n')    

    # to left a item
    def left_item(self, sprite, x, y):
        self.map[x][y] = sprite

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
        item = (self.map[new_player_coor][player_coor_y]) if axis == 'x' else (self.map[player_coor_x][new_player_coor])

        # if in the way there is an object/item
        if type(item) == basic_item.basic_item:

            # if the player want, or not, take the item
            take_item = True if (utilities.opciones(f'¿Tomar {item.name}?', ['y', 'n']) == 'y') else False

            if take_item and\
                 (len(self.player.inventory) < self.player.inv_limit): # if the object/item is taken and the inventory is in it's limit
                self.player.inventory.append(item)

                if axis == 'x':
                    self.map[new_player_coor][player_coor_y] = '.'
                else:
                    self.map[player_coor_x][new_player_coor] = '.'

            else: # if not
                if axis == 'x':
                    self.room_inv_save(item, new_player_coor, player_coor_y)
                else:
                    self.room_inv_save(item, player_coor_x, new_player_coor)

        # player's axis move
        if axis == 'x': # in horizontal axis
            self.player.x = new_player_coor
        else: # in vertical axis
            self.player.y = new_player_coor

        if axis == 'x': # in horizontal axis
            self.floor_item_check(self.player.x, (self.player.x - move_vector), self.player.y, self.room_inv['coor_x'])
        else: # in vertical axis
            self.floor_item_check(self.player.y, self.player.x, (self.player.y - move_vector), self.room_inv['coor_y'])

    def floor_item_check(self, used_player_axis, player_x, player_y, room_inv_axis):
    
        # little check if where the player is an object/item or just floor
        if self.room_inv['in_use'] == True and\
            ((room_inv_axis < used_player_axis) or\
                ((room_inv_axis > used_player_axis))): # if it's an object/item
            self.left_item(self.room_inv['item'], room_inv_axis, room_inv_axis)
            self.room_inv_save(None, 0, 0, in_use = False)
        else: # if it's floor
            self.map[player_x][player_y] = '.'
