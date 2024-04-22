
import random
from items.basic_equip import basic_equip
from utilities import *

class shield_medusa:

    # name, sprite, x, y, damage, critic, defense, func, to_player, desc, nonfunc
    def start(self, x = 1, y = 1):
        name = 'Escudo de Medusa'
        sprite = ']'
        damage = 0
        critic = 0
        defense = 20
        to_player = True
        return basic_equip('sm-]', name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player, battle_effect=self.use_alter_status, desc = "Puede convertir en piedra a quien ataque al portador", nonfunc = self.nonuse_function)

    def petrification(self, victim):
        victim.hp = 0
        utilities.print_effect(f'\n\n[{victim.name}] activó la maldición de Medusa en su ataque y se convirtió en piedra.')

    def use_function(self, player):
        # check if the player have an shield or not.
        if player.equipment['shield'] == None or (player.equipment['shield']).name != (self.start()).name:
            
            # shield in equipment and buff to defense
            player.equipment['shield'] = self.start()
            utilities.print_effect(f'\n[{(self.start()).name}] equipado.')
            player.defense = (player.equipment['shield']).defense + player.base_defense
        else:
            utilities.print_effect(f'[{(self.start()).name}] ya equipado.')
    
    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.defense = player.defense - (player.equipment['shield']).defense
        player.equipment['shield'] = None
    
    def use_alter_status(self, victim): # is the altered state effect of the weapon
        var = random.randint(0, 10)
        if var > 9:
            victim.alter_status = [self.petrification, 0]
