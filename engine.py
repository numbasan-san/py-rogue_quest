
from colorama import Fore
import input_handler, random, hud, combat_logic
import data.map_things.json_handler as json_handler
import data.level_things.levels as levels

from common_utilities.utilities import *
from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from items.basic_environment_item import basic_environment_item as basic_environment_item
from npc.basic_enemy import basic_enemy as basic_enemy

from getpass import getpass
from start_world_elements import start_player, start_enemies, start_items

class engine:

    def __init__(self):
        self.room_inv = {
            'item': None,
            'coor_x': 0,
            'coor_y': 0,
            'in_use': False
        }
        self.end_exe = False
        self.start_player = start_player() # to return the player
        self.start_enemies = start_enemies() # to return the enemies
        self.items = start_items() # to return the items
        self.map = None
        self.player = None
        self.dungeon_floor = 0
        self.dungeon_lvlup = True
        self.to_next_turn = 1

    def run(self):
        # time.sleep(5)
        if self.dungeon_lvlup:
            self.dungeon_floor += 1
            self.dungeon_lvlup = False
            self.load_world()
        else:

            hud.print_hud(self.map, self.player)
            # print(self.to_next_turn)

            # actions menu
            text = "1. Mirar inventario.\n2. Moverse.\n3. Mirar Equipamento"
            action = utilities.opciones('\nElija una de las opciones:\n' + text + '\nElección', ['1', '2', '3'])
            end_player_turn = self.menu_actions(action)
            # actions menu end #

            # enemies movement
            if end_player_turn or self.to_next_turn >= 5:
                self.to_next_turn = 1
                for row in self.map:
                    for cell in row:
                        if isinstance(cell, basic_enemy):
                            enemy = cell
                            if enemy.state:
                                if enemy.strategy_ia:
                                    enemy.strategy_ia(self.map)
                                else:
                                    enemy.move(self.map, self.player)

            if not self.player.state: # if the player is dead
                utilities.print_effect(f'\n[player] murió.')
                utilities.print_effect(f'\n\n\n-+-+-+-+- M O R T I S -+-+-+-+-\n', color=Fore.RED)
                self.end_exe = True
            getpass('')

    def menu_actions(self, action):
        if action == '1':  # look inventory
            self.handle_inventory()
            self.to_next_turn += 1
        elif action == '2':  # move
            self.move_selection()
            self.to_next_turn = 1
            return True

        elif action == '3':  # look equipment
            self.handle_equipment()
            self.to_next_turn += 1

        return False

    def handle_inventory(self):
        hud.print_full_inventory(self.player)

        opt = utilities.pregunta('Elija qué usar (0 para nada): ', 0, len(self.player.inventory)) - 1
        
        def use_item(item, opt):
            item_used = item.func(self.player) if item.to_player else item.func()
            if item_used or isinstance(item, basic_equip):
                self.player.inventory.pop(opt)
                utilities.print_effect(f'\n[{item.name}] fue utilizado.')

        def drop_item(item, opt):
            utilities.print_effect(f'[{item.name}] se soltó.')
            self.room_inv_save(item, self.player.x, self.player.y, True)
            self.player.inventory.pop(opt)
        
        if opt == -1:
            return

        item = self.player.inventory[opt]
        action_options = {
            '0': lambda: None,  # No hacer nada
            '1': lambda: use_item(item, opt), # Usar objeto
            '2': lambda: drop_item(item, opt), # Soltar objeto
            '3': lambda:  hud.print_item_stats(item) # Inspeccionar objeto
        }

        text = "0. Nada.\n1. Usar.\n2. Soltar.\n3. Inspeccionar."
        inv_action = utilities.opciones(f'\nElija qué hacer con [{item.name}]:\n{text}\nElección', ['0', '1', '2', '3'])
        action_options[inv_action]()

    def handle_equipment(self):
        hud.print_full_equip(self.player)
        sword, shield = self.player.equipment["sword"], self.player.equipment["shield"]

        if sword or shield:
            equip_opt = utilities.opciones('Elija (0 para salir): ', ['0', '1', '2'])
            equip = sword if equip_opt == '1' else shield

            if equip:
                self.manage_equipment(equip)
            else:
                utilities.print_effect('Nada equipado.')
        else:
            utilities.print_effect('Nada equipado.')

    def manage_equipment(self, equip):
        text = "0. Nada.\n1. Desequipar.\n2. Inspeccionar.\n3. Soltar."
        equip_action = utilities.opciones(f'\nElija qué hacer con [{equip.name}]:\n{text}\nElección', ['0', '1', '2', '3'])
        
        def unequip_item(equip):
            equip.nonfunc(self.player, f'\n[{equip.name}] se desequipó.')
            self.player.inventory.append(equip)

        def drop_equipped_item(equip):
            self.room_inv_save(equip, self.player.x, self.player.y, True)
            equip.nonfunc(self.player, f'\n[{equip.name}] se soltó.')

        action_mapping = {
            '0': lambda: None,
            '1': lambda: unequip_item(equip),
            '2': lambda: hud.print_item_stats(equip),
            '3': lambda: drop_equipped_item(equip)
        }

        action_mapping[equip_action]()

    # the name explains it self
    def move_selection(self):   

        # player flanks check
        player_around = [
            self.map[self.player.x - 1][self.player.y], # up
            self.map[self.player.x + 1][self.player.y], # down
            self.map[self.player.x][self.player.y - 1], # left
            self.map[self.player.x][self.player.y + 1], # right
        ]

        print()

        # move control
        move_vector = input_handler.valid_move(self.player.x, self.player.y, self.map, player_around)

        # vertical movement
        if move_vector['direc'] in ['w', 's']:
            self.load_move('x', move_vector, (self.player.x + move_vector['move']), self.player.y, (self.player.x + move_vector['move']))
        # vertical movement end #

        # horizontal movement
        elif move_vector['direc'] in ['a', 'd']:
            self.load_move('y', move_vector, self.player.x, (self.player.y + move_vector['move']), (self.player.y + move_vector['move']))
        # horizontal movement end #

    # execute the movement and everything that entails
    def load_move(self, axis, move_vector, x, y, move): 
        sq = self.map[x][y]
        if not(isinstance(sq, (basic_enemy))): # verifying if the next coor is an enemy

            # player's movement function
            utilities.print_effect(f'\n{move_vector["msg"]}\n')
            self.movement(axis, move, move_vector['move'])

        else: # if the next coor is an enemy
            if sq.state: # if the enemy is alive
                combat_logic.combat_logic(self.player, sq, self.map, self.player)

                # when the player get exp
                lvl = int(levels.find_level(self.player.level, self.player.exp))
                if lvl > self.player.level:
                    utilities.print_effect(f'\nEl jugador subió de nivel [{self.player.level}] a [{lvl}].\n')

                    # when the player goes up more than one level at a time
                    for i in range(self.player.level, lvl + 1):
                        self.player.level = lvl
                        self.player.max_hp += 5
                        self.player.base_damage += 5
                        self.player.base_defense += 5
                        self.player.hp += 3
                        self.player.defense += 5
                        self.player.damage += 5

            else: # if the enemy is dead
                utilities.print_effect(f'\nEs el cuerpo inerte de un/una [{sq.name}].')
                utilities.print_effect(f'\n{move_vector["msg"]}\n')
                self.movement(axis, move, move_vector['move'])

    # to save a item in the room
    def room_inv_save(self, item, x, y, in_use):
        self.room_inv['item'] = item
        self.room_inv['coor_x'] = x
        self.room_inv['coor_y'] = y
        self.room_inv['in_use'] = in_use

    # the player's movement
    def movement(self, axis, new_coor, move_vector):
        # Current and new coordinates
        player_x, player_y = self.player.x, self.player.y
        new_player_coor = new_coor

        # Determine the object at the new location based on the axis
        if axis == 'x':
            thing = self.map[new_player_coor][player_y]
        else:
            thing = self.map[player_x][new_player_coor]

        # Handle if the object/item is an instance of basic_item, basic_equip, or basic_enemy
        if isinstance(thing, (basic_item, basic_equip, basic_enemy)):
            self.handle_item_or_enemy(thing, axis, new_player_coor, player_x, player_y)

        # Handle if the object is a basic_environment_item
        elif isinstance(thing, basic_environment_item):
            self.handle_environment_item(thing, axis, new_player_coor, player_x, player_y)

        # Move the player and check for floor items
        if axis == 'x':
            self.update_player_position(new_player_coor, player_y, move_vector, 'x')
        else:
            self.update_player_position(player_x, new_player_coor, move_vector, 'y')

    # helper function to handle item or enemy
    def handle_item_or_enemy(self, thing, axis, new_player_coor, player_x, player_y):
        if len(self.player.inventory) < self.player.inv_limit and not isinstance(thing, basic_enemy):
            # Pick up the item
            self.player.inventory.append(thing)
            utilities.print_effect(f'[{thing.name}] guardado en el inventario.\n')
            self.update_map(axis, new_player_coor, player_x, player_y, '.')
        else:
            # Handle inventory full or enemy encounter
            self.room_inv_save(thing, new_player_coor if axis == 'x' else player_x, player_y if axis == 'x' else new_player_coor, True)

    # helper function to handle environment items
    def handle_environment_item(self, thing, axis, new_player_coor, player_x, player_y):
        if thing.func():  # Perform the environment item action
            self.dungeon_lvlup = True
        else:
            self.room_inv_save(thing, new_player_coor if axis == 'x' else player_x, player_y if axis == 'x' else new_player_coor, True)

    # helper function to update player position and check for floor items
    def update_player_position(self, new_x, new_y, move_vector, axis):
        if axis == 'x':
            self.player.x = new_x
            self.floor_item_check(self.player.x, self.player.x - move_vector, self.player.y, self.room_inv['coor_x'], (self.room_inv['coor_x'], self.room_inv['coor_y']))
        else:
            self.player.y = new_y
            self.floor_item_check(self.player.y, self.player.x, self.player.y - move_vector, self.room_inv['coor_y'], (self.room_inv['coor_x'], self.room_inv['coor_y']))

    # helper function to update the map
    def update_map(self, axis, new_player_coor, player_x, player_y, new_value):
        if axis == 'x':
            self.map[new_player_coor][player_y] = new_value
        else:
            self.map[player_x][new_player_coor] = new_value

    # to check if where the player is an object/item or just floor
    def floor_item_check(self, used_player_axis, player_x, player_y, room_inv_axis, room_coors):
        if self.room_inv['in_use'] == True and\
              ((room_inv_axis < used_player_axis) or ((room_inv_axis > used_player_axis))): # if it's an object/item
            self.map[room_coors[0]][room_coors[1]] = self.room_inv['item']
            self.room_inv_save(None, 0, 0, False)
        else: # if it's floor
            self.map[player_x][player_y] = '.'


    '''                             ' '' 
        World's and data's loaders
    '' '                             '''
    # setting world elements
    def load_world(self):
        # map's constructions
        self.map_class = (json_handler.load_random_map())
        self.map = self.map_class['map']

        # player
        self.player = self.start_player.mod_player_coords(
            (self.map_class['player_spawn_coords'])[0], 
            (self.map_class['player_spawn_coords'])[1]
        )
        
        # Load items, enemies, and stairs
        self.load_entity(self.map_class, self.items.return_items(), 'items')   # items print
        self.load_entity(self.map_class, self.start_enemies.return_enemies(), 'enemys')  # enemies print
        self.load_entity(self.map_class, self.items.return_stairs(), 'stairs')   # stairs print

    # to load entity
    def load_entity(self, map_coors, start_entities, load_entity):
        for i in range(len(map_coors[load_entity + '_spawn_coords'])):
            while True:
                random_entity_class = random.choice(start_entities)  # Random entity class selected
                
                # Create entity instance directly using __init__
                entity = random_entity_class()  # Create an instance of the entity class
                
                # setting coordinates for each "entity spawn coordinates" in the map
                entity.x = map_coors[load_entity + '_spawn_coords'][i][0]
                entity.y = map_coors[load_entity + '_spawn_coords'][i][1]

                # Check if the entity is an enemy and its range is within dungeon_floor
                if (isinstance(entity, basic_enemy) and entity.range <= self.dungeon_floor) or \
                isinstance(entity, (basic_item, basic_environment_item)):
                    
                    # entity print
                    self.map[entity.x][entity.y] = entity
                    break  # Break the while loop if entity is successfully placed
