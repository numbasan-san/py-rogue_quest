
from items.basic_equip import basic_equip
from utilities import *

class sword:

    # name, sprite, x, y, damage, critic, defense
    def start(self, x = 1, y = 1):
        name = 'Espada'
        sprite = '/'
        damage = 10
        critic = 5
        defense = 0
        to_player = True
        return basic_equip(name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player, desc = 'Es una espada normal', nonfunc = self.nonuse_function)

    def use_function(self, player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (self.start()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = self.start()
            utilities.print_effect(f'\n[{(self.start()).name}] equipado.')
            player.damage = (player.equipment['sword']).damage + player.damage
        else:
            utilities.print_effect(f'[{(self.start()).name}] ya equipado.')

    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.damage = player.damage - (player.equipment['sword']).damage
        player.equipment['sword'] = None
