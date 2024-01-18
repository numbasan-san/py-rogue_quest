
from npc.basic_enemy import basic_enemy as enemy

class ghoul:

    # name, hp, defense, sprite, x, y, exp
    def start_ghoul():
        return enemy('Ghoul', 100, 5, 10, 'G', 2, 2, 10)
