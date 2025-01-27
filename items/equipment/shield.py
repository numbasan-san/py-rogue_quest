
from items.basic_equip import BasicEquip
import config.setting as sttng
from ui import hud

class Shield(BasicEquip):

    def __init__(self, x=1, y=1):
        name = (sttng.get_language())["items"]["shield"]["name"]
        sprite = ')'
        damage = 0
        critic = 0
        defense = 10
        to_player = True
        # name, sprite, x, y, damage, critic, defense, rarity, func, to_player, battle_effect, desc, nonfunc
        super().__init__(name, sprite, x, y, damage, critic, defense, 1, "sh-)", func=self.use_function, to_player=to_player, desc=(sttng.get_language())["items"]["shield"]["desc"], nonfunc=self.nonuse_function)

    def use_function(self, player):
        if player.equipment['shield'] is None or player.equipment['shield'].name != self.name:
            player.equipment['shield'] = self
            hud.print_effect(f'\n[{self.name}] {(sttng.get_language())["game"]["equip_action"]["equipped"]}.')
            player.defense = self.defense + player.base_defense
        else:
            hud.print_effect(f'[{self.name}] {(sttng.get_language())["game"]["equip_action"]["already_equipped"]}.')

    def nonuse_function(self, player, msg):
        hud.print_effect(msg)
        player.defense -= player.equipment['shield'].defense
        player.equipment['shield'] = None

