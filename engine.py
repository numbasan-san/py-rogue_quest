
import input_handler, random, hud, os, combat_logic
import data.map_things.json_handler as json_handler
import data.level_things.levels as levels
import data.safe_game.saved_game_handler as saved_game_handler
import data.safe_game.load_saved_game as load_saved_game

from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from npc.basic_enemy import basic_enemy as basic_enemy
from items.basic_environment_item import basic_environment_item as basic_environment_item

from getpass import getpass
from utilities import *
from start_world_elements import start_player, start_enemies, start_items, player

class engine:

    def __init__(self):
        self.room_inv = {
            'item': None,
            'coor_x': 0,
            'coor_y': 0,
            'in_use': False
        }
        self.end_exe = False
        self.start_enemies = start_enemies() # to return the enemies
        self.items = start_items() # to return the items
        self.player = start_player.return_player() # to return the player
        self.map = None
        self.dungeon_range = 1
        self.dungeon_lvlup = False

        if os.path.exists('data/safe_game/run_data.json'):
            self.load_save_run()
            self.dungeon_lvlup = False
        else:
            self.load_world()
            saved_game_handler.save_run(self.map, self.player, self.dungeon_range, self.map_class['name'])


    def run(self):
        # time.sleep(5)
        if self.dungeon_lvlup:
            self.dungeon_range += 1
            self.dungeon_lvlup = False
            self.load_world()
            saved_game_handler.save_run(self.map, self.player, self.dungeon_range, self.map_class['name'])
        else:

            hud.print_hud(self.map, self.player, self.dungeon_range)

            # actions menu
            text = "1. Mirar inventario.\n2. Moverse.\n3. Mirar Equipamento"
            action = utilities.opciones('\nElija una de las opciones:\n' + text + '\nElección', ['1', '2', '3'])
            end_player_turn = self.menu_actions(action)
            # actions menu end #

            # enemies movement
            if end_player_turn:
                for x in range(len(self.map)):
                    for y in range(len(self.map[x])):
                        if isinstance(self.map[x][y], basic_enemy):
                            enemy = self.map[x][y]
                            if enemy.state:
                                enemy.move_ia(self.map, self.player)
                                if not(enemy.strategy_ia == None):
                                    enemy.strategy_ia(self.map)

            getpass('')

    # menu's actions
    def menu_actions(self, action):
        if action == '1': # look into inventory choice

            hud.print_full_inventory(self.player)

            opt = (utilities.pregunta('Elija qué usar (0 para nada): ', 0, len(self.player.inventory))) - 1

            if opt == -1:
                pass
            else: # choose what to do with the selected object
                item = self.player.inventory[opt]
                text = "0. Nada.\n1. Usar.\n2. Soltar."
                inv_action = utilities.opciones(f'\nElija qué hacer con [{item.name}]:\n' + text + '\nElección', ['0', '1', '2'])
                if inv_action == '1': # use it
                    item_used = item.func(self.player) if ((item.to_player)) else item.func()
                    if item_used:
                        (self.player.inventory).pop(opt)
                    elif isinstance(item, (basic_equip)):
                        (self.player.inventory).pop(opt)
                if inv_action == '2': # drop it
                    utilities.print_effect(f'[{(self.player.inventory[opt]).name}] se soltó.')
                    self.room_inv_save(item, self.player.x, self.player.y, True)
                    (self.player.inventory).pop(opt)
                if inv_action == '0':
                    pass

        elif action == '2': # move choice
            self.move_selection()
            return True

        elif action == '3': # look into equipment choice
            hud.print_full_equip(self.player)
            if self.player.equipment["sword"] != None or self.player.equipment["shield"] != None:
                equip_opt = utilities.opciones(f'Elije (0 salir): ', ['0', '1', '2'])
                equip = self.player.equipment["sword"] if equip_opt == '1' else self.player.equipment["shield"]
                if equip != None:
                    text = "0. Nada.\n1. Desequipar.\n2. Inspeccionar.\n3. Soltar."
                    equip_action = utilities.opciones(f'\nElija qué hacer con [{equip.name}]:\n{text}\nElección', ['0', '1', '2', '3'])

                    # equipment actions menu
                    if equip_action == '1': # unequip
                        equip.nonfunc(self.player, f'\n{(equip).name} se desequipó.')
                        (self.player.inventory).append(equip)
                    if equip_action == '2': # inspect
                        hud.print_equip_stats(equip)
                    if equip_action == '3': # drop it
                        self.room_inv_save(equip, self.player.x, self.player.y, True)
                        equip.nonfunc(self.player, f'\n{(equip).name} se soltó.')
                    if equip_action == '0': # nothing
                        pass
                    # equipment actions menu end #

                else: utilities.print_effect('\nNada equipado.')
            else:
                utilities.print_effect('\nNada equipado.')

        return False

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

        else: # if the next coor is an enemy combat
            if sq.state: # if the enemy is alive
                combat_logic.combat_logic(self.map, self.player, sq)
                if sq.state:
                    player_death = combat_logic.combat_logic(self.map, sq, self.player)
                    if player_death:
                        self.end_exe = True

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

        # setting the new coor and actuals coors
        new_player_coor = new_coor
        player_coor_x, player_coor_y = self.player.x, self.player.y

        new_coords = (new_player_coor, player_coor_y) if axis == 'x' else (player_coor_x, new_player_coor)

        # the next map item/object
        thing = self.map[new_coords[0]][new_coords[1]]

        # if in the way there is an object/item
        if isinstance(thing, (basic_item, basic_equip, basic_enemy)):

            # if the object/item is taken and the inventory is in it's limit
            if (len(self.player.inventory) < self.player.inv_limit) and not(isinstance(thing, (basic_enemy))):

                self.player.inventory.append(thing)
                utilities.print_effect(f'[{thing.name}] guardado en el inventario.\n')

                self.map[new_coords[0]][new_coords[1]] = '.'

            else: # if not
                self.room_inv_save(thing, new_coords[0], new_coords[1], True) if axis == 'x' else self.room_inv_save(thing, new_coords[0], new_coords[1], True)

        # if the object/item is a environment item
        elif isinstance(thing, (basic_environment_item)):
            stairs_use = thing.func()
            if stairs_use:
                self.dungeon_lvlup = True
                self.stairs_used = stairs_use
            else:
                self.room_inv_save(thing, new_coords[0], new_coords[1], True) if axis == 'x' else self.room_inv_save(thing, new_coords[0], new_coords[1], True)


        # player's axis move
        if axis == 'x': # in horizontal axis
            self.player.x = new_player_coor
            self.floor_item_check(self.player.x, (self.player.x - move_vector), self.player.y, 
                                  self.room_inv['coor_x'], (self.room_inv['coor_x'], self.room_inv['coor_y'])
                                 )
        else: # in vertical axis
            self.player.y = new_player_coor
            self.floor_item_check(self.player.y, self.player.x, 
                                  (self.player.y - move_vector), self.room_inv['coor_y'], 
                                  (self.room_inv['coor_x'], self.room_inv['coor_y'])
                                 )
        # player's axis move end #

    # to check if where the player is an object/item or just floor
    def floor_item_check(self, used_player_axis, player_x, player_y, room_inv_axis, room_coors):
        if self.room_inv['in_use'] == True and\
              ((room_inv_axis < used_player_axis) or ((room_inv_axis > used_player_axis))): # if it's an object/item
            self.map[room_coors[0]][room_coors[1]] = self.room_inv['item']
            self.room_inv_save(None, 0, 0, False)
        else: # if it's floor
            self.map[player_x][player_y] = '.'



    '''                             '' '
        world's and data's loaders
    ' ''                             '''

    def load_save_run(self):
        self.map = (load_saved_game.load_map())
        self.player = (load_saved_game.load_player()) # player
        self.dungeon_range = (load_saved_game.load_dungeon_range()) # dungeon range
        
    # setting world elements
    def load_world(self):
        # map's constructions
        self.map_class = (json_handler.load_random_map())
        self.map = self.map_class['map']

        # player
        self.player.x = (self.map_class['player_spawn_coords'])[0]
        self.player.y = (self.map_class['player_spawn_coords'])[1]
        self.load_entity(self.map_class, self.items.return_items(), 'items') # items print
        self.load_entity(self.map_class, self.start_enemies.return_enemies(), 'enemys') # enemies print
        self.load_entity(self.map_class, self.items.return_stairs(), 'stairs') # stairs print

    # to load entity
    def load_entity(self, map_coors, start_entities, load_entity):
        for i in range(len(map_coors[load_entity + '_spawn_coords'])):
            while True:
                random_entity = random.choice(start_entities) # A random entity selected
                entity = random_entity.start() # starting the entity

                # setting coors for each "entity spawn coors" in the map in turn
                entity.x = map_coors[load_entity + '_spawn_coords'][i][0]
                entity.y = map_coors[load_entity + '_spawn_coords'][i][1]

                # Check if the entity is an enemy and its range is within dungeon_range
                if isinstance(entity, basic_enemy) and entity.range <= self.dungeon_range:
                    # entity print
                    self.map[entity.x][entity.y] = entity
                    break  # Break the while loop if entity is successfully placed
                elif isinstance(entity, (basic_item, basic_environment_item)):
                    self.map[entity.x][entity.y] = entity
                    break  # Break the while loop if entity is successfully placed
