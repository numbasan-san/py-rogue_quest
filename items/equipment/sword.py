
from items.basic_equip import basic_equip

class sword:

    # name, sprite, x, y, damage, critic, defense
    def start(self, x = 1, y = 1):
        name = 'Espada'
        sprite = '/'
        damage = 10
        critic = 5
        defense = 0
        to_player = True
        return basic_equip(name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player)

# class use_sword:

    def use_function(self, player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (self.start_sword()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = self.start_sword()
            print('El jugador se equipó ' + (self.start_sword()).name + '.')
            player.damage = (player.equipment['sword']).damage + player.base_damage
        else:
            print((self.start_sword()).name + ' ya equipado.')
