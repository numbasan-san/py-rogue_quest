
from items.basic_equip import basic_equip

class shield:

    # name, sprite, x, y, damage, critic, defense
    def start_shield(x = 1, y = 1):
        return basic_equip('Escudo', ')', x, y, 0, 0, 10, func = use_shield.use_function, to_player=True)

class use_shield:

    def use_function(player):
        # check if the player have an shield or not.
        if player.equipment['shield'] == None or (player.equipment['shield']).name != (shield.start_shield()).name:
            
            # shield in equipment and buff to defense
            player.equipment['shield'] = shield.start_shield()
            print('El jugador se equipó ' + (shield.start_shield()).name + '.')
            player.defense = (player.equipment['shield']).defense + player.base_defense
        else:
            print((shield.start_shield()).name + ' ya equipado.')
