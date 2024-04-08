
import random
from items.basic_equip import basic_equip

class fire_sword:

    # name, sprite, x, y, damage, critic, defense
    def start(self, x = 1, y = 1):
        name = 'Espada de fuego'
        sprite = '|'
        damage = 20
        critic = 10
        defense = 0
        to_player = True
        return basic_equip(name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player, battle_effect=self.use_alter_status)
    
    def burn(self, victim): # sword's efect
        victim.hp -= 1
        print(victim.name + ' sufre por quemaduras. Vida reducida por 1 punto.')

# class use_fire_sword:

    def use_function(self, player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != (self.start_fire_sword()).name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = self.start_fire_sword()
            print('El jugador se equipó ' + (self.start_fire_sword()).name + '.')
            player.damage = (player.equipment['sword']).damage + player.base_damage
        else:
            print((self.start_fire_sword()).name + ' ya equipado.')

    def use_alter_status(self, victim): # is the altered state effect of the weapon
        var = random.randint(0, 10)
        if var > 8:
            victim.alter_status = [self.burn, 5]
