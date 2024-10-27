
from items.basic_environment_item import BasicEnvironmentItem
from common_utilities.utilities import *
from ui import hud

class Stairs(BasicEnvironmentItem):

    def __init__(self, x=1, y=1):
        name = 'Escaleras'
        sprite = '¬'
        super().__init__(name, sprite, x, y, self.use_function)

    def use_function(self):
        opt = utilities.opciones(f'¿Pasar la escalera?', ['y', 'n'])
        if opt == 'y':
            hud.print_effect(f'\nEl jugador pasó por la escalera, cambiando de nivel en la mazmorra.')
            return True
        else:
            return False
