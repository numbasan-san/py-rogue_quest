
from items.basic_equip import basic_equip
from utilities import *

class shield:

    # name, sprite, x, y, damage, critic, defense
    def start(self, x = 1, y = 1):
        name = 'Escudo'
        sprite = ')'
        damage = 0
        critic = 0
        defense = 10
        to_player = True
        return basic_equip(name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player, desc = 'Es un escudo normal')

    def use_function(self, player):
        # check if the player have an shield or not.
        if player.equipment['shield'] == None or (player.equipment['shield']).name != (self.start()).name:
            
            # shield in equipment and buff to defense
            player.equipment['shield'] = self.start()
            utilities.print_effect('\nEl jugador se equipó ' + (self.start()).name + '.')
            player.defense = (player.equipment['shield']).defense + player.base_defense
        else:
            utilities.print_effect((self.start()).name + ' ya equipado.')

    def nonuse_function(self, player):
        player.equipment['shield'] = None
        utilities.print_effect('\nEl jugador se desequipó ' + (self.start()).name + '.')
        player.damage = player.damage - (player.equipment['shield']).damage
