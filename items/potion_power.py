
from basic_item import basic_item

class potion_power:

    # name, sprite, x, y, type
    def start_potion_power(x = 1, y = 1):
        return basic_item('power_potion', 'x', x, y, 'item')

    def item_func():
        print('Se debería aumentar la fuerza del jugador si se usa.')
