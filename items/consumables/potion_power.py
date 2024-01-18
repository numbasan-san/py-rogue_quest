
from items.basic_item import basic_item

class potion_power:

    # name, sprite, x, y
    def start_potion_power(x = 1, y = 1):
        return basic_item('Poción de Poder', 'x', x, y, use_potion_power.use_function, True)

class use_potion_power:

    def use_function(player):
        player.damage += 10
        print('Ataque del jugador aumentado.')
        return True
