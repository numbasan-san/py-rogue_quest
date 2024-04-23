
import input_handler, random, hud, os
import data.map_things.json_handler as json_handler
import data.level_things.levels as levels
import data.safe_game.saved_game_handler as saved_game_handler
import data.safe_game.load_saved_game as load_saved_game

from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from npc.basic_enemy import basic_enemy as enemy
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
            saved_game_handler.save_run(self.map, self.player, self.dungeon_range)


    def run(self):
        # time.sleep(5)
        if self.dungeon_lvlup:
            self.dungeon_range += 1
            self.dungeon_lvlup = False
            self.load_world()
            saved_game_handler.save_run(self.map, self.player, self.dungeon_range)
        else:

            hud.print_hud(self.map, self.player, self.dungeon_range)

            # actions menu
            text = "1. Mirar inventario.\n2. Moverse.\n3. Mirar Equipamento"
            action = utilities.opciones('\nElija una de las opciones:\n' + text + '\nElección', ['1', '2', '3'])

            if action == '1': # look into inventory choice

                hud.print_full_invent(self.player)

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
            # actions menu end #

            getpass('')

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
        if not(isinstance(sq, (enemy))): # verifying if the next coor is an enemy

            # player's movement function
            utilities.print_effect(f'\n{move_vector["msg"]}\n')
            self.movement(axis, move, move_vector['move'])

        else: # if the next coor is an enemy
            if sq.state: # if the enemy is alive
                self.combat_logic(self.player, sq)
                if sq.state:
                    self.combat_logic(sq, self.player)

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
        player_coor_x = self.player.x
        player_coor_y = self.player.y

        # the next map item/object
        thing = (self.map[new_player_coor][player_coor_y]) if axis == 'x' else (self.map[player_coor_x][new_player_coor])

        # if in the way there is an object/item
        if isinstance(thing, (basic_item, basic_equip, enemy)):

            # if the object/item is taken and the inventory is in it's limit
            if (len(self.player.inventory) < self.player.inv_limit) and not(isinstance(thing, (enemy))):

                self.player.inventory.append(thing)
                utilities.print_effect(f'[{thing.name}] guardado en el inventario.\n')

                if axis == 'x':
                    self.map[new_player_coor][player_coor_y] = '.'
                else:
                    self.map[player_coor_x][new_player_coor] = '.'

            else: # if not
                if axis == 'x':
                    self.room_inv_save(thing, new_player_coor, player_coor_y, True)
                else:
                    self.room_inv_save(thing, player_coor_x, new_player_coor, True)

        # if the object/item is a environment item
        elif isinstance(thing, (basic_environment_item)):
            stairs_use = thing.func()
            if stairs_use:
                self.dungeon_lvlup = True
                self.stairs_used = stairs_use
            else:
                if axis == 'x':
                    self.room_inv_save(thing, new_player_coor, player_coor_y, True)
                else:
                    self.room_inv_save(thing, player_coor_x, new_player_coor, True)

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

    # the name explains it self
    def combat_logic(self, attacker, victim):

        damage = int(attacker.damage / (2 ** (victim.defense / attacker.damage))) # + weapon.critic
        damage = damage if damage > 1 else 1
        victim.hp = (victim.hp - damage) if damage < victim.hp else 0

        utilities.print_effect(f'\nEl/La [{attacker.name}] atacó a [{victim.name}]. {str(damage)}')

        if isinstance(attacker, (player)): # if the player is the attacker
            player_sword = attacker.equipment['sword']
            if player_sword != None: # if the player have a weapon
                # if the weapon have an effect and the victim have already an effect
                if (player_sword).battle_effect != None and (victim.alter_status == None):
                    (player_sword).battle_effect(victim)

            player_shield = attacker.equipment['shield']
            if player_shield != None: # if the player have a weapon
                # if the weapon have an effect and the victim have already an effect
                if (player_shield).battle_effect != None and (victim.alter_status == None):
                    (player_shield).battle_effect(victim)

        if victim.alter_status != None: # if the victim doesn't have an altered effect
            (victim.alter_status[0])(victim) # the effect
            victim.alter_status[1] -= 1 # reduction in duration of effect
            if victim.alter_status[1] <= 0: # when the effect ends
                victim.alter_status = None

        if victim.hp <= 0 and victim.state: # death verification
            (self.map[victim.x][victim.y]).state = not(victim.state)
            (self.map[victim.x][victim.y]).sprite = '%'
            utilities.print_effect(f'\n[{victim.name}] murió.\n')
            if isinstance(victim, (player)): # when the player dies
                self.player.state = False
                utilities.print_effect(f'\n M O R T I S \n')

                os.remove('data/safe_game/run_data.json') # delete the saved data
                
                self.end_exe = not(self.end_exe)
            else: # when the enemy dies
                attacker.exp += victim.exp



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
                if isinstance(entity, enemy) and entity.range <= self.dungeon_range:
                    # entity print
                    self.map[entity.x][entity.y] = entity
                    break  # Break the while loop if entity is successfully placed
                elif isinstance(entity, (basic_item, basic_environment_item)):
                    self.map[entity.x][entity.y] = entity
                    break  # Break the while loop if entity is successfully placed
