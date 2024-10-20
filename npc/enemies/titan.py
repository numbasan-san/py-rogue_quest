
from npc.basic_enemy import basic_enemy as enemy

class titan(enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy
        super().__init__('Titan', 100, 70, 10, 'T', x, y, 1000, 1, 3)
