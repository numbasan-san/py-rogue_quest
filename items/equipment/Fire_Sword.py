
import random
from utilities import *
from items.basic_equip import basic_equip

class fire_sword:

    # name, sprite, x, y, damage, critic, defense, func, to_player, desc, nonfunc
    def start(self):
        name = 'Espada de fuego'
        sprite = '|'
        damage = 20
        critic = 10
        defense = 0
        to_player = True
        return basic_equip('fs-|', name, sprite, 1, 1, damage, critic, defense, func = self.use_function, to_player = to_player, battle_effect=self.use_alter_status, desc = "Puede causar quemaduras a quien se le ataque", nonfunc = self.nonuse_function)
    
    def burn(self, victim): # sword's efect
        victim.hp -= 1
        utilities.print_effect(f'\n\n[{victim.name}] sufre por quemaduras. Vida reducida por 1 punto.')

    def use_function(self, player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (self.start()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = self.start()
            utilities.print_effect(f'\n[{(self.start()).name}] equipado.')
            player.damage = (player.equipment['sword']).damage + player.damage
        else:
            utilities.print_effect(f'\n[{(self.start()).name}] ya equipado.')
    
    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.damage = player.damage - (player.equipment['sword']).damage
        player.equipment['sword'] = None
        
    def use_alter_status(self, victim): # is the altered state effect of the weapon
        var = random.randint(0, 10)
        if var > 8:
            victim.alter_status = [self.burn, 5]
