
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Kelpie(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["kelpie"]["description"]
        super().__init__('Kelpie', 100, 5, 10, x, y, 8, 1, 1, "kp-K", desc=desc)
