
from npc.basic_enemy import basic_enemy as enemy

class ghoul(enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy
        super().__init__('Ghoul', 100, 5, 10, 'G', x, y, 15, 2, 2)
