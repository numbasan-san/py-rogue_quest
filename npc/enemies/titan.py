
from npc.basic_enemy import basic_enemy as enemy

class titan:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self):
        return enemy('Titan', 100, 70, 10, 'T', 2, 2, 1000, 2)
