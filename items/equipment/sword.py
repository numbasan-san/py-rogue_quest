
from items.basic_equip import basic_equip

class sword:

    # name, sprite, x, y, damage, critic, defense
    def start_sword(x = 1, y = 1):
        return basic_equip('Espada', '/', x, y, 10, 5, 0)

    def item_func():
        print('Se debería mejorar el ataque del jugador si se usa.')
