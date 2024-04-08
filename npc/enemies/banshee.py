
from npc.basic_enemy import basic_enemy as enemy

class banshee:

    # name, hp, damage, defense, sprite, x, y, exp
    def start(self):
        return enemy('Banshee', 100, 5, 10, 'B', 2, 2, 20)
