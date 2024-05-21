
from npc.basic_enemy import basic_enemy as enemy

class kelpie:

    # code, name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        return enemy('kp-k', 'Kelpie', x, y, 100, 5, 10, 'K', x, y, 8, 1)
