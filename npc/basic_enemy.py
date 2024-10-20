
import math, combat_logic
from colorama import *
from items.basic_equip import basic_equip
from items.basic_item import basic_item
from items.basic_environment_item import basic_environment_item

color_mapping = {
    1: Fore.GREEN, # beast
    2: Fore.LIGHTBLACK_EX, # undead
    3: Fore.YELLOW, # animated
}

class basic_enemy:

    def __init__(self, name, hp, damage, defense, sprite, x, y, exp, range, color, alter_status=None, move_ia=None, strategy_ia=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.exp = exp
        self.range = range
        self.color = color_mapping.get(color, Fore.WHITE)
        self.state = True
        self.alter_status = alter_status
        # Asignar el movimiento estándar si no se proporciona uno específico
        self.move_ia = self.move if move_ia is None else move_ia
        self.strategy_ia = strategy_ia

    def move(self, game_map, player):
        player_coords = (player.x, player.y)
        
        # Coordenadas adyacentes (Derecha, Izquierda, Arriba, Abajo)
        near_coords = [
            (self.x + 1, self.y),  # Derecha
            (self.x - 1, self.y),  # Izquierda
            (self.x, self.y - 1),  # Arriba
            (self.x, self.y + 1)   # Abajo
        ]

        # Obtener las coordenadas más cercanas ordenadas al jugador
        sorted_coords = self.nearest_coordinates(near_coords, player_coords, game_map)

        if not sorted_coords:
            return  # No hay movimiento posible

        # Verificar si la coordenada más cercana está ocupada por un enemigo
        next_coords = sorted_coords[0]  # Coordenada más cercana
        second_coords = sorted_coords[1] if len(sorted_coords) > 1 else None  # Segunda coordenada más cercana

        target = game_map[next_coords[0]][next_coords[1]]  # El objeto en la siguiente coordenada

        def update_move(new_coords, sq):
            game_map[self.x][self.y] = sq  # Liberar la posición actual
            self.x, self.y = new_coords  # Actualizar las coordenadas del enemigo
            game_map[new_coords[0]][new_coords[1]] = self  # Mover al enemigo a la nueva posición

        if next_coords == player_coords:
            if isinstance(target, type(player)):  # Verificar si es el jugador
                print(f'El enemigo atacó al jugador en las coordenadas: {player_coords}')
                # Aquí puedes llamar a la lógica de combate
                combat_logic.combat_logic(self, player, game_map, player)

        elif not isinstance(target, type(self)):
            # Si la coordenada más cercana no tiene un enemigo
            if isinstance(target, (basic_item, basic_equip, basic_environment_item)):
                # Si hay un objeto en la siguiente coordenada, intercambiar
                update_move(next_coords, target)
            else:
                # Si no hay objeto, mover al enemigo a la nueva posición
                update_move(next_coords, '.')
        elif isinstance(target, type(self)):
            # Si la coordenada más cercana está ocupada por otro enemigo, moverse a la segunda más cercana
            if second_coords:
                second_target = game_map[second_coords[0]][second_coords[1]]
                if not isinstance(second_target, type(self)):  # Si no hay otro enemigo en la segunda coordenada
                    if isinstance(second_target, (basic_item, basic_equip, basic_environment_item)):
                        # Si hay un objeto en la segunda coordenada, intercambiar
                        update_move(second_coords, second_target)
                    else:
                        # Si no hay objeto, moverse a la segunda coordenada más cercana
                        update_move(second_coords, '.')                    

    def nearest_coordinates(self, coords, player, game_map):
        walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']  # Conjunto en lugar de lista para búsquedas más rápidas

        # Filtramos las coordenadas válidas, descartando aquellas que contengan paredes
        valid_coords = [coord for coord in coords if (game_map[coord[0]][coord[1]] not in walls)]

        # Si no hay coordenadas válidas, devolvemos None
        if not valid_coords:
            return None

        # Devuelve la coordenada más cercana al jugador
        sorted_coords = sorted(valid_coords, key=lambda coord: math.dist(coord, player))
        return sorted_coords
