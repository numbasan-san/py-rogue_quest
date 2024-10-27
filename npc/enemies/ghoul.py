
from npc.basic_enemy import BasicEnemy as Enemy

class Ghoul(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy/color
        super().__init__('Ghoul', 100, 5, 10, 'G', x, y, 15, 2, 2)
