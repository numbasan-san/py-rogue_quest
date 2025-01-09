
import random
from items.basic_equip import BasicEquip
import config.setting as sttng
from ui import hud

lan = sttng.get_language()

class ShieldMedusa(BasicEquip):

    def __init__(self, x=1, y=1):
        name = lan["items"]["shield_medusa"]["name"]
        sprite = ']'
        damage = 0
        critic = 0
        defense = 20
        to_player = True
        # name, sprite, x, y, damage, critic, defense, rarity, func, to_player, battle_effect, desc, nonfunc
        super().__init__(name, sprite, x, y, damage, critic, defense, 5, func=self.use_function, to_player=to_player, battle_effect=self.use_alter_status, desc=lan["items"]["shield_medusa"]["desc"], nonfunc=self.nonuse_function)

    def petrification(self, victim):
        victim.hp = 0
        hud.print_effect(f'\n\n[{victim.name}] {lan["items"]["shield_medusa"]["effect"]}.')

    def use_function(self, player):
        if player.equipment['shield'] is None or player.equipment['shield'].name != self.name:
            player.equipment['shield'] = self
            hud.print_effect(f'\n[{self.name}] {lan["game"]["equip_action"]["equipped"]}.')
            player.defense = self.defense + player.base_defense
        else:
            hud.print_effect(f'[{self.name}] {lan["game"]["equip_action"]["already_equipped"]}.')

    def nonuse_function(self, player, msg):
        hud.print_effect(msg)
        player.defense -= player.equipment['shield'].defense
        player.equipment['shield'] = None

    def use_alter_status(self, victim):
        if random.randint(0, 10) > 9:
            victim.alter_status = [self.petrification, 0]

