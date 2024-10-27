
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
