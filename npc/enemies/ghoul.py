
from npc.basic_enemy import basic_enemy as enemy

class ghoul:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        return enemy('gh-g', 'Ghoul', 100, 5, 10, 'G', x, y, 15, 1)
