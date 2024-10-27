
from npc.basic_enemy import BasicEnemy as Enemy

class Kelpie(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy/color
        super().__init__('Kelpie', 100, 5, 10, 'K', x, y, 8, 1, 1)
