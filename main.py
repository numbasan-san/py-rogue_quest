
import os, time
import config.setting as setting
from engine import engine
from ui import hud
from ui.titles.titles import get_big_title, get_little_title
from common_utilities.utilities import utilities

def new_game():
    eng = engine()
    while not eng.end_exe:
        eng.run()

def resume_game():
    pass

def encyclopedia():
    pass

def main(shortcut = False):
    if shortcut:
        new_game()
    else:
        os.system(setting.get_clear_cmd())
        hud.print_title_style(f"{get_big_title()}Developed by numbasan-san")
        time.sleep(2)
        os.system(setting.get_clear_cmd())

        menu_text = '\n[1] Nueva Partida\n[2] # Continuar #\n[3] # Enciclopedia #\n[0] Salir'
        hud.print_title_style(get_little_title() + menu_text)

        action = utilities.opciones('\nElija una opción', ['1', '2', '3', '0'])
        action_mapping = {
            '1': new_game, 
            # '2': resume_game, 
            # '3': encyclopedia, 
            '0': exit, 
        }

        action_mapping.get(action, lambda: print("Función no implementada."))()


if __name__ == '__main__':
    main()
