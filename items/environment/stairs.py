
from items.basic_environment_item import BasicEnvironmentItem
from common_utilities.utilities import *
import config.setting as sttng
from ui import hud

class Stairs(BasicEnvironmentItem):

    def __init__(self, x=1, y=1):
        name = (sttng.get_language())["items"]["stairs"]["name"]
        sprite = '¬'
        super().__init__(name, sprite, x, y, "st-¬", self.use_function)

    def use_function(self):
        opt = utilities.opciones(f'{(sttng.get_language())["items"]["stairs"]["prompt"]}', ['y', 'n'])
        if opt == 'y':
            hud.print_effect(f'\n{(sttng.get_language())["items"]["stairs"]["level_up"]}.')
            return True
        else:
            return False