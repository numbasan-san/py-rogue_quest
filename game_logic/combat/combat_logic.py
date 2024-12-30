
import data.encyclopedia.bestiary_handler as bestiary_handler
from colorama import init, Fore
from ui import hud

def combat_logic(attacker, victim, game_map, player):

    # calculate damage based on opponent's attack and defense
    damage = max(1, int(attacker.damage / (2 ** (victim.defense / attacker.damage))))
    victim.hp -= damage

    # determine appropriate names for the attacker and the victim
    attacker_name = 'player' if attacker is player else attacker.name
    victim_name = 'player' if victim is player else victim.name

    # show the result of the attack
    hp_count = f' ({victim.hp}/{victim.max_hp})' if not(victim is player) else ''
    hud.print_effect(f'\nEl/La [{attacker_name}] atacó a [{victim_name}]{hp_count}.')

    # specific logic if the attacker is the player
    if attacker is player:
        for equip in ['sword', 'shield']:
            item = attacker.equipment.get(equip)
            if item and item.battle_effect and not victim.alter_status:
                item.battle_effect(victim)

    # apply status effects if you have them
    if victim.alter_status:
        victim.alter_status[0](victim)
        victim.alter_status[1] -= 1
        if victim.alter_status[1] <= 0:
            victim.alter_status = None

    # check if the victim has died
    if victim.hp <= 0:
        if not(victim is player):
            bestiary_handler.write_bestiary(victim)
        game_map[victim.x][victim.y] = f'{victim.color}%{Fore.RESET}'

        if not victim is player:
            hud.print_effect(f'\n[{victim_name}] murió.')

        # if the enemy dies, player receives the enemy's experience
        if victim is not player:
            attacker.exp += victim.exp
