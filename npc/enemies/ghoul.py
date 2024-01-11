
from npc.enemy import enemy

class ghoul:

    # name, hp, defense, sprite, x, y, exp
    def start_ghoul():
        return enemy('Ghoul', 100, 5, 10, 'G', 2, 2, 10)
