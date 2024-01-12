
from items.basic_item import basic_item

class potion(basic_item):

    # name, sprite, x, y
    def __init__(self, x = 1, y = 1):
        super().__init__('Poción', '+', x, y, func=self.item_func)

    def item_func(self, player):
        if player.hp < player.max_hp:
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            print('Se debería recuperar la salud del jugador si se usa. y si el jugador tiene menos vida que la máxima.') 
            return True
        else:
            return False
