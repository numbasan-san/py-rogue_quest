

from items.basic_item import basic_item

class potion:

    def start_potion():
        return basic_item('Poción', '+', 1, 1, use_potion.use_function, to_player = True)

class use_potion:

    def use_function(player):
        if player.hp < player.max_hp:
            player.hp = (player.hp + 10) if (player.hp + 10) < player.max_hp else player.max_hp
            print('Se debería recuperar la salud del jugador si se usa. y si el jugador tiene menos vida que la máxima.')
            return True
        else:
            print('No se puede usar la poción, ya que la vida del jugador está al máximo.')
            return False


# # Definir la variable inicial
# mi_variable = 91

# # Definir una función lambda que añade 10 a la variable si es menor a 100
# # y la establece en 100 si el resultado es mayor a 100, sin hacer nada si ya es 100
# actualizar_variable = lambda x: (x + 10) if (x < 100) and (x + 10) < 100 else 100 if (x + 10) > 100 else x

# # Aplicar la función lambda a la variable
# mi_variable = actualizar_variable(mi_variable)

# # Imprimir el resultado
# print(mi_variable)