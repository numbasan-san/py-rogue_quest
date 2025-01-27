
from items.basic_item import BasicItem
import config.setting as setting
from ui import hud

lan = (setting.get_language())

class PotionPower(BasicItem):

    def __init__(self, x=1, y=1):
        name = (setting.get_language())["items"]["potion_power"]["name"]
        sprite = 'x'
        desc = (setting.get_language())["items"]["potion_power"]["desc"]
        to_player = True
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, "pp-x", func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        player.damage += 10
        player.base_damage += 10
        hud.print_effect(f'\n{(setting.get_language())["items"]["potion_power"]["used"]}\n')
        return True