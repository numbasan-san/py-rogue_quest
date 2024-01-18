
import random
from items.basic_equip import basic_equip

class fire_sword:

    # name, sprite, x, y, damage, critic, defense
    def start_fire_sword(x = 1, y = 1):
        return basic_equip('Espada de fuego', '|', x, y, 20, 10, 0, func = use_fire_sword.use_function, to_player=True, battle_effect=use_fire_sword.use_alter_status)

    def burn(victim): # sword's efect
        victim.hp -= 1
        print(victim.name + ' sufre por quemaduras. Vida reducida por 1 punto.')

class use_fire_sword:

    def use_function(player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (fire_sword.start_fire_sword()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = fire_sword.start_fire_sword()
            print('El jugador se equipó ' + (fire_sword.start_fire_sword()).name + '.')
            player.damage = (player.equipment['sword']).damage + player.base_damage
        else:
            print((fire_sword.start_fire_sword()).name + ' ya equipado.')

    def use_alter_status(victim): # is the altered state effect of the weapon
        var = random.randint(0, 10)
        if var > 8:
            victim.alter_status = [fire_sword.burn, 5]
