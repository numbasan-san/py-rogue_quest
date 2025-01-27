
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Dragon(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["dragon"]["description"]
        super().__init__('Dragon', 100, 5, 10, x, y, 15, 1, 1, "dg-D", desc=desc)
    
    def hability():
    # estoy pensando hacer que su habilidad sea bajar debilitar al jugador
        pass 
