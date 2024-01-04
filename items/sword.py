
from basic_item import basic_item

class sword:

    # name, sprite, x, y, tag
    def start_sword(x = 1, y = 1):
        return basic_item('sword', '/', x, y)

    def item_func():
        print('Se debería mejorar el ataque del jugador si se usa.')
