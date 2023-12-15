
from basic_item import basic_item

class potion:

    # name, sprite, x, y, tag
    def start_potion(x = 1, y = 1):
        return basic_item('potion', '+', x, y, 'item')

    def item_func():
        print('Se debería recuperar la salud del jugador si se usa.')
