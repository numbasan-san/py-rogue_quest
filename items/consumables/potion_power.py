
from items.basic_item import BasicItem
from ui import hud

class PotionPower(BasicItem):

    def __init__(self, x=1, y=1):
        name = 'Poción de Poder'
        sprite = 'x'
        desc = 'Otorga 10 de ataque'
        to_player = True
        # name, sprite, x, y, rarity, func, desc, to_player
        super().__init__(name, sprite, x, y, 2, func=self.use_function, desc=desc, to_player=to_player)

    def use_function(self, player):
        player.damage += 10
        player.base_damage += 10
        hud.print_effect('\nAtaque del jugador aumentado.\n')
        return True
