
from items.basic_equip import basic_equip
from utilities import *
import random

class shield_medusa(basic_equip):

    def __init__(self, x=1, y=1):
        name = 'Escudo de Medusa'
        sprite = ']'
        damage = 0
        critic = 0
        defense = 20
        to_player = True
        super().__init__(name, sprite, x, y, damage, critic, defense, func=self.use_function, to_player=to_player, battle_effect=self.use_alter_status, desc="Puede convertir en piedra a quien ataque al portador", nonfunc=self.nonuse_function)

    def petrification(self, victim):
        victim.hp = 0
        utilities.print_effect(f'\n\n[{victim.name}] activó la maldición de Medusa en su ataque y se convirtió en piedra.')

    def use_function(self, player):
        if player.equipment['shield'] is None or player.equipment['shield'].name != self.name:
            player.equipment['shield'] = self
            utilities.print_effect(f'\n[{self.name}] equipado.')
            player.defense = self.defense + player.base_defense
        else:
            utilities.print_effect(f'[{self.name}] ya equipado.')

    def nonuse_function(self, player, msg):
        utilities.print_effect(msg)
        player.defense -= player.equipment['shield'].defense
        player.equipment['shield'] = None

    def use_alter_status(self, victim):
        if random.randint(0, 10) > 9:
            victim.alter_status = [self.petrification, 0]
