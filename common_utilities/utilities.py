
import sys, time
from colorama import Fore

class utilities:

    @staticmethod
    def opciones(texto, opciones):
        valor = "".lower()
        while not valor in opciones:
            valor = input(f'{texto} {opciones}: ').lower()
        return valor
    
    @staticmethod
    def pregunta(texto, min, max):
        valor = input(texto)
        while True:
            if valor.isdigit():
                valor = int(valor)
                if (valor >= min) and (valor <= max):
                    return valor
            valor = input(texto)

    def print_effect(s, color = Fore.RESET):
        for c in s:
            sys.stdout.write(color + c)
            sys.stdout.flush()
            time.sleep(0.05)

    def print_title(s):
        simbols = ['_','(',')','~','|']
        for i, c in enumerate(s):
            color = Fore.LIGHTYELLOW_EX if c == '~' else Fore.LIGHTBLACK_EX if c in simbols else Fore.WHITE
            c = '█' if c == '*' else c
            sys.stdout.write(color + c + Fore.RESET)
            sys.stdout.flush()
            time.sleep(0.001)
