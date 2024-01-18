
from items.basic_equip import basic_equip

class sword:

    # name, sprite, x, y, damage, critic, defense
    def start_sword(x = 1, y = 1):
        return basic_equip('Espada', '/', x, y, 10, 5, 0, func = use_sword.use_function, to_player=True)

class use_sword:

    def use_function(player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (sword.start_sword()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = sword.start_sword()
            print('El jugador se equipó ' + (sword.start_sword()).name + '.')
            player.damage = (player.equipment['sword']).damage + player.base_damage
        else:
            print((sword.start_sword()).name + ' ya equipado.')
