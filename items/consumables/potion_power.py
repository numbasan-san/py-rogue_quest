
from items.basic_item import basic_item

class potion_power:

    # name, sprite, x, y
    def start_potion_power(x = 1, y = 1):
        return basic_item('Poción de Poder', 'x', x, y)

    def item_func():
        print('Se debería aumentar la fuerza del jugador si se usa.')
