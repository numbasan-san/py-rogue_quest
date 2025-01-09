
"""

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

"""
from items.basic_environment_item import BasicEnvironmentItem
from common_utilities.utilities import *
import config.setting as sttng
from ui import hud

lan = sttng.get_language()

class Stairs(BasicEnvironmentItem):

    def __init__(self, x=1, y=1):
        name = lan["items"]["stairs"]["name"]
        sprite = '¬'
        super().__init__(name, sprite, x, y, self.use_function)

    def use_function(self):
        opt = utilities.opciones(f'{lan["items"]["stairs"]["prompt"]}', ['y', 'n'])
        if opt == 'y':
            hud.print_effect(f'\n{lan["items"]["stairs"]["level_up"]}.')
            return True
        else:
            return False