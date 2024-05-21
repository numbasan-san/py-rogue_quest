
import os

from npc.basic_enemy import basic_enemy as basic_enemy
from npc.ia.enemies import basic_enemie_ia as enemy_ia
from utilities import *
from start_world_elements import player


def enemies_movement(map, player): # enemies movement
    enemies = []
    for x in map:
        for element in x:
            if isinstance(element, (basic_enemy)):
                enemy = element
                if enemy.state:
                    print(f'enemigo detectado: {enemy.sprite} ({element.x}, {element.y})')
                    enemies.append(enemy)
    enemy_ia.move_enemies(map, player, enemies)

# the name explains it self
def combat_logic(map, attacker, victim):

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
        (map[victim.x][victim.y]).state = not(victim.state)
        (map[victim.x][victim.y]).sprite = '%'
        utilities.print_effect(f'\n[{victim.name}] murió.\n')
        if isinstance(victim, (player)): # when the player dies
            player.state = False
            utilities.print_effect(f'\n M O R T I S \n')
            os.remove('data/safe_game/run_data.json') # delete the saved data
            return True
        else: # when the enemy dies
            attacker.exp += victim.exp
