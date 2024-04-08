

from items.basic_item import basic_item

class potion:

    def start(self):
        name = 'Poción'
        sprite = '+'
        to_player = True
        return basic_item(name, sprite, 1, 1, self.use_function, to_player = to_player)

# class use_potion:

    def use_function(player):
        if player.hp < player.max_hp:
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            print('Se debería recuperar la salud del jugador si se usa. y si el jugador tiene menos vida que la máxima.')
            return True
        else:
            print('No se puede usar la poción, ya que la vida del jugador está al máximo.')
            return False
