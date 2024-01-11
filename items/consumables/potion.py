
from items.basic_item import basic_item

class potion:

    # name, sprite, x, y
    def start_potion(x = 1, y = 1):
        return basic_item('Poción', '+', x, y)

    def item_func(player):
        player.hp += 10
        return 'Se debería recuperar la salud del jugador si se usa.'
