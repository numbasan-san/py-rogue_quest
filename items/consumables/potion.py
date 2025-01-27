
from items.basic_item import BasicItem
import config.setting as setting
from ui import hud

class Potion(BasicItem):

    def __init__(self, x=1, y=1):
        name = (setting.get_language())["items"]["potion"]["name"]
        sprite = '+'
        to_player = True
        desc = (setting.get_language())["items"]["potion"]["desc"]
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, "pt-+", func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            hud.print_effect(f'\n{(setting.get_language())["items"]["potion"]["healed"]} [{hp_txt}].')
            return True
        else:
            hud.print_effect(f'\n{(setting.get_language())["items"]["potion"]["no_heal"]}.')
            return False