
from items.basic_equip import BasicEquip
import config.setting as setting
from ui import hud

lan = setting.get_language()

class Sword(BasicEquip):

    def __init__(self, x=1, y=1):
        name = lan["items"]["sword"]["name"]
        sprite = '/'
        damage = 10
        critic = 5
        defense = 0
        to_player = True
        # name, sprite, x, y, damage, critic, defense, rarity, func, to_player, battle_effect, desc, nonfunc
        super().__init__(name, sprite, x, y, damage, critic, defense, 1, func=self.use_function, to_player=to_player, desc=lan["items"]["sword"]["desc"], nonfunc=self.nonuse_function)

    def use_function(self, player):
        if player.equipment['sword'] is None or player.equipment['sword'].name != self.name:
            player.equipment['sword'] = self
            hud.print_effect(f'\n[{self.name}] {lan["game"]["equip_action"]["equipped"]}.')
            player.damage += self.damage
        else:
            hud.print_effect(f'[{self.name}] {lan["game"]["equip_action"]["already_equipped"]}.')

    def nonuse_function(self, player, msg):
        hud.print_effect(msg)
        player.damage -= player.equipment['sword'].damage
        player.equipment['sword'] = None


