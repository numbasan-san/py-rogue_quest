
from npc.basic_enemy import basic_enemy as enemy

class kelpie:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        self.x = x
        self.y = y
        return enemy('Kelpie', 100, 5, 10, 'K', x, y, 8, 1, move_ia=None)
