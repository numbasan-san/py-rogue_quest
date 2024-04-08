
from items.basic_equip import basic_equip

class shield:

    # name, sprite, x, y, damage, critic, defense
    def start(self, x = 1, y = 1):
        name = 'Escudo'
        sprite = ')'
        damage = 0
        critic = 0
        defense = 10
        to_player = True
        return basic_equip(name, sprite, x, y, damage, critic, defense, func = self.use_function, to_player = to_player)

# class use_shield:

    def use_function(self, player):
        # check if the player have an shield or not.
        if player.equipment['shield'] == None or (player.equipment['shield']).name != (self.start_shield()).name:
            
            # shield in equipment and buff to defense
            player.equipment['shield'] = self.start_shield()
            print('El jugador se equipó ' + (self.start_shield()).name + '.')
            player.defense = (player.equipment['shield']).defense + player.base_defense
        else:
            print((self.start_shield()).name + ' ya equipado.')
