
import os, input_handler, json_handler

from utilities import *
from start_characters import *

class engine:

    def __init__(self):
        self.message = ''
        self.item = {
            'sprite': '',
            'coor_x': 0,
            'coor_y': 0
        }
        self.room_inv = {
            'item': None,
            'coor_x': 0,
            'coor_y': 0,
            'in_use': False
        }
        self.end_exe = False

        self.map_class = json_handler.load_random_map()
        self.map = self.map_class['map']
        self.player = start_characters.return_player((self.map_class['player_spawn_coors'])[0], (self.map_class['player_spawn_coors'])[1])
        self.enemy = start_characters.return_enemy()

        self.player_around = []

    def run(self):
        os.system('cls')

        # enemy print
        self.map[self.enemy.x][self.enemy.y] = self.enemy.sprite

        # player print
        self.map[self.player.x][self.player.y] = self.player.sprite

        self.player_around = [
            self.map[self.player.x - 1][self.player.y], # up
            self.map[self.player.x + 1][self.player.y], # down
            self.map[self.player.x][self.player.y - 1], # left
            self.map[self.player.x][self.player.y + 1] # right
        ]

        """
        La idea es validar si la siguiente coordenada es piso. Solo no se me ocurre cómo validarlo.
        """

        # map print
        for line in self.map:
            floor = ''
            for square in line:
                floor += square

            print(floor)

        print(f'Inventario del jugador: {self.player.inventory}')

        # move control
        move_vector = input_handler.valid_move(self.player.x, self.player.y, self.map, self.player_around)

        # vertical movement
        if move_vector['direc'] in ['w', 's']:
            if self.map[self.player.x + move_vector['move']][self.player.y] != ' ': # verifying if the next coor is a "wall"

                # player's movement function
                self.movement('x', self.player.x + move_vector['move'], move_vector['move'])
                print(move_vector['msg'])

            else:
                print('''
##################################################
Aviso: Es imposible desplazarse por esa dirección.
##################################################
''')

        # horizontal movement
        elif move_vector['direc'] in ['a', 'd']:
            if self.map[self.player.x][self.player.y + move_vector['move']] != ' ': # verifying if the next coor is a "wall"

                # player's movement function
                self.movement('y', self.player.y + move_vector['move'], move_vector['move'])
                print(move_vector['msg'])

            else:
                print('''
##################################################
Aviso: Es imposible desplazarse por esa dirección.
##################################################
''')

        # print(f'Player current coors: ({self.player.x}, {self.player.y})')

        '''a = input('¿Cambiar de mapa?')
        if a == 'y':
            self.map = map_charge.charge_map()      '''      

        input()

    # to left a item
    def left_item(self, sprite, x, y):
        self.map[x][y] = sprite

    # to save a item in the room
    def room_inv_save(self, item, x, y, in_use = True):
        self.room_inv['item'] = item
        self.room_inv['coor_x'] = x
        self.room_inv['coor_y'] = y
        self.room_inv['in_use'] = in_use
        # print(f'El objeto {self.room_inv["item"]} está en las coordenadas ({self.room_inv["coor_x"]}, {self.room_inv["coor_y"]})')

    # to take a item to the player
    def grab_item(self, x, y):
        
        if self.map[x][y] != '.':
            take_item = True if (utilities.opciones('¿Tomar item?', ['y', 'n']) == 'y') else False
            return take_item

    # the player's movement
    def movement(self, axis, new_coor, move_vector):

        # setting the new coor and actuals coors
        new_player_coor = new_coor
        player_coor_x = self.player.x
        player_coor_y = self.player.y

        # the next map item/object
        item = (self.map[new_player_coor][player_coor_y]) if axis == 'x' else (self.map[player_coor_x][new_player_coor])

        # if in the way there is an object/item
        if item != '.':
            
            # if the player want, or not, take the item
            take_item = True if (utilities.opciones('¿Tomar item?', ['y', 'n']) == 'y') else False
            if take_item: # if the object/item is taken
                self.player.inventory.append(item)
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
            # little check if where the player is an object/item or just floor
            if self.room_inv['in_use'] == True and\
                ((self.room_inv['coor_x'] < self.player.x) or\
                    ((self.room_inv['coor_x'] > self.player.x))): # if it's an object/item
                self.left_item(self.room_inv['item'], self.room_inv['coor_x'], self.room_inv['coor_y'])
                self.room_inv_save(None, 0, 0, in_use = False)
            else: # if it's floor
                self.map[self.player.x - move_vector][player_coor_y] = '.'

        else: # in vertical axis
            # little check if where the player is an object/item or just floor
            if self.room_inv['in_use'] == True and\
                ((self.room_inv['coor_y'] < self.player.y) or\
                  (self.room_inv['coor_y'] > self.player.y)): # if it's an object/item
                self.left_item(self.room_inv['item'], self.room_inv['coor_x'], self.room_inv['coor_y'])
                self.room_inv_save(None, 0, 0, in_use = False)
            else: # if it's floor
                self.map[self.player.x][self.player.y - move_vector] = '.'
