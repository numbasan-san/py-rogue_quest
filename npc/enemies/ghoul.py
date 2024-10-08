
from npc.basic_enemy import basic_enemy as enemy

class ghoul:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        self.x = x
        self.y = y
        return enemy('Ghoul', 100, 5, 10, 'G', x, y, 15, 1, move_ia=None)
