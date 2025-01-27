
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Cerberos(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["cerberos"]["description"]
        super().__init__('Cerberos', 100, 5, 10, x, y, 15, 1, 1, "cb-C", desc=desc)
    
    def hability():
    # estoy pensando hacer que su habilidad sea bajar debilitar al jugador
        pass 
