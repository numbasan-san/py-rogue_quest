
from npc.basic_enemy import basic_enemy as enemy

class titan:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        self.x = x
        self.y = y
        return enemy('Titan', 100, 70, 10, 'T',  x, y, 1000, 2, move_ia=None)
