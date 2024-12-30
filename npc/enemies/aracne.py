
from npc.basic_enemy import BasicEnemy as Enemy

class Aracne(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        super().__init__('Aracne', 100, 5, 10, x, y, 15, 1, 1)
    
    def hability():
    # estoy pensando hacer que su habilidad sea bajar debilitar al jugador
        pass 
