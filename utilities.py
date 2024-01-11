
import sys, time

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

    def print_effect(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)
