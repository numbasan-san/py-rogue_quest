
from npc.basic_enemy import BasicEnemy as Enemy
from npc.enemy_move_ia import move as movement_ia

class Titan(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy/color
        super().__init__('Titan', 100, 70, 10, 'T', x, y, 1000, 10, 3)
