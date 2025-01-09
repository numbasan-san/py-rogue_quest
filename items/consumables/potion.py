
"""
from items.basic_item import BasicItem
from ui import hud

class Potion(BasicItem):

    def __init__(self, x=1, y=1):
        name = 'Poción'
        sprite = '+'
        to_player = True
        desc = "Recupera 10 puntos de salud como máximo"
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            hud.print_effect(f'\nSalud recuperada en [{hp_txt}].')
            return True
        else:
            hud.print_effect('\nTe detienes un segundo y piensas: "Mejor no lo desperdicio. No tengo heridas ahora".')
            return False

"""
from items.basic_item import BasicItem
import config.setting as setting
from ui import hud

lan = (setting.get_language())

class Potion(BasicItem):

    def __init__(self, x=1, y=1):
        name = lan["items"]["potion"]["name"]
        name = 'Poción'
        sprite = '+'
        to_player = True
        desc = lan["items"]["potion"]["desc"]
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        if player.hp < player.max_hp:
            hp_txt = '10' if (player.hp + 10) < player.max_hp else (player.max_hp - player.hp)
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            hud.print_effect(f'\n{lan["items"]["potion"]["healed"]} [{hp_txt}].')
            return True
        else:
            hud.print_effect(f'\n{lan["items"]["potion"]["no_heal"]}.')
            return False