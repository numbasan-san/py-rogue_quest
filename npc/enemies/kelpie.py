
from npc.basic_enemy import basic_enemy as enemy

class kelpie:

    # code, name, hp, damage, defense, sprite, x, y, exp, range
    def start(self):
        return enemy('kp-k', 'Kelpie', 100, 5, 10, 'K', 2, 2, 8, 1)
