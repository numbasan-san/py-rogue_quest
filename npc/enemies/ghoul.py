
from npc.basic_enemy import basic_enemy as enemy

class ghoul:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self):
        return enemy('gh-g', 'Ghoul', 100, 5, 10, 'G', 2, 2, 15, 1)
