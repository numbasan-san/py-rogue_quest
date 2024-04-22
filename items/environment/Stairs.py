
from items.basic_environment_item import basic_environment_item
from utilities import *

class stairs:

    # name, sprite, x, y, func
    def start(self, x = 1, y = 1):
        name = 'Escaleras'
        sprite = '¬'
        return basic_environment_item('st-¬', name, sprite, x, y, self.use_function)

    def use_function(self):
        # utilities.print_effect(f'\n¿Cómo se supone que haga esta cosa funcionar?\n')
        opt = utilities.opciones(f'¿Pasar la escalera?', ['y', 'n'])
        if opt == 'y':
            utilities.print_effect(f'\nEl jugador pasó por la escalera, cambiando de nivel en la mazmorra.')
            return True
        else:
            return False
