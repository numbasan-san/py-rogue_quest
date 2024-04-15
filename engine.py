
import input_handler, random, hud
import data.map_things.json_handler as json_handler
import data.level_things.levels as levels

from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from npc.basic_enemy import basic_enemy as enemy

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
        self.start_player = start_player() # to return the player
        self.start_enemies = start_enemies() # to return the enemies
        self.items = start_items() # to return the items

        # map's constructions
        self.map_class = (json_handler.load_random_map())
        self.map = self.map_class['map']

        # player
        self.player = self.start_player.return_player((self.map_class['player_spawn_coors'])[0], (self.map_class['player_spawn_coors'])[1])
        self.load_entity(self.map_class, self.items.return_items(), 'items') # items print
        self.load_entity(self.map_class, self.start_enemies.return_enemies(), 'enemys') # enemies print

    def run(self):
        # time.sleep(5)

        hud.print_hud(self.map, self.player)

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
                inv_action = utilities.opciones(f'\nElija qué hacer con {item.name}:\n' + text + '\nElección', ['0', '1', '2'])
                if inv_action == '1': # use it
                    item_used = item.func(self.player) if ((item.to_player)) else item.func()
                    if item_used:
                        (self.player.inventory).pop(opt)
                if inv_action == '2': # drop it
                    utilities.print_effect(f'{(self.player.inventory[opt]).name} se soltó.')
                    self.room_inv_save(item, self.player.x, self.player.y, True)
                    (self.player.inventory).pop(opt)
                if inv_action == '0':
                    pass

        if action == '2': # move choice
            self.move_selection()

        if action == '3': # look into equipment choice
            hud.print_full_equip(self.player)
            if self.player.equipment["sword"] != None or self.player.equipment["shield"] != None:
                equip_opt = utilities.opciones(f'Elije (0 salir): ', ['0', '1', '2'])
                equip = self.player.equipment["sword"] if equip_opt == '1' else self.player.equipment["shield"]
                text = "0. Nada.\n1. Desequipar.\n2. Inspeccionar."
                equip_action = utilities.opciones(f'\nElija qué hacer con {equip.name}:\n{text}\nElección', ['0', '1', '2'])

                # equipment actions menu
                if equip_action == '1': # drop it
                    utilities.print_effect(f'{(self.player.inventory[equip_opt]).name} se desequipó.')
                    self.room_inv_save(equip, self.player.x, self.player.y, True)
                    (self.player.inventory).add()
                if equip_action == '2': # inspect
                    hud.print_equip_stats(equip)
                if equip_action == '0': # nothing
                    pass
                # equipment actions menu end #

            else:
                utilities.print_effect('No hay nada equipado.')
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
                lvl = int(levels.find_level(self.player.exp))
                if lvl > self.player.level:
                    utilities.print_effect(f'\nEl jugador subió de nivel {self.player.level} a {lvl}.\n')

                    # when the player goes up more than one level at a time
                    for i in range(self.player.level, lvl + 1):
                        self.player.level = lvl
                        self.player.max_hp += 5
                        self.player.base_damage += 5
                        self.player.base_defense += 5
                        self.player.hp += 3
                        self.player.defense += 3
                        self.player.damage += 3

            else: # if the enemy is dead
                utilities.print_effect(f'\nEs el cuerpo inerte de un/una {sq.name}.')
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
                utilities.print_effect(f'{thing.name} guardado en el inventario.\n')

                if axis == 'x':
                    self.map[new_player_coor][player_coor_y] = '.'
                else:
                    self.map[player_coor_x][new_player_coor] = '.'

            else: # if not
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
        victim.hp -= damage

        attacker_name = attacker.name if type(attacker) != type(self.player) else 'player'
        victim_name = victim.name if type(victim) != type(self.player) else 'player'

        utilities.print_effect(f'\nEl/La {attacker_name} atacó a {victim_name}. {str(damage)}')

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
            utilities.print_effect(f'\n{victim_name} murió.\n')
            if isinstance(victim, (player)): # when the player dies
                utilities.print_effect(f'\n M O R T I S \n')
                self.end_exe = not(self.end_exe)
            else: # when the enemy dies
                attacker.exp += victim.exp



    # to load entity
    def load_entity(self, map_coors, start_entities, load_entity):
        for i in range(len(map_coors[load_entity + '_spawn_coors'])):
            random_entity = random.choice(start_entities) # A random entity selected
            entity = random_entity.start() # starting the entity

            # setting coors for each "entity spawn coors" in the map in turn
            entity.x = (((map_coors[load_entity + '_spawn_coors'])[i]))[0]
            entity.y = (((map_coors[load_entity + '_spawn_coors'])[i]))[1]

            # entity print
            self.map[entity.x][entity.y] = entity
