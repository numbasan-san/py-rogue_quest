
from items.basic_item import basic_item

class potion_power:

    # name, sprite, x, y
    def start(self, x = 1, y = 1):
        name = 'Poción de Poder'
        sprite = 'x'
        to_player = True
        return basic_item(name, sprite, x, y, self.use_function, to_player = to_player)

# class use_potion_power:

    def use_function(player):
        player.damage += 10
        print('Ataque del jugador aumentado.')
        return True
