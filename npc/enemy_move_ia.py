
import math

from game_logic.combat import combat_logic
from items.basic_equip import BasicEquip
from items.basic_item import BasicItem
from items.basic_environment_item import BasicEnvironmentItem

def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def move(enemy, game_map, player):
    player_coords = (player.x, player.y)
    enemy_coords = (enemy.x, enemy.y)

    # Verificar si el jugador está a 3 casillas o menos de distancia
    if calculate_distance(player_coords, enemy_coords) > 30:
        return

    from npc.basic_enemy import BasicEnemy
    player_coords = (player.x, player.y)

    # Coordenadas adyacentes (Derecha, Izquierda, Arriba, Abajo)
    near_coords = [
        (enemy.x + 1, enemy.y),  # Derecha
        (enemy.x - 1, enemy.y),  # Izquierda
        (enemy.x, enemy.y - 1),  # Arriba
        (enemy.x, enemy.y + 1)   # Abajo
    ]

    # Obtener las coordenadas más cercanas ordenadas al jugador
    sorted_coords = nearest_coordinates(near_coords, player_coords, game_map)

    if not sorted_coords:
        return  # No hay movimiento posible

    # Verificar si la coordenada más cercana está ocupada por un enemigo
    next_coords = sorted_coords[0]  # Coordenada más cercana
    second_coords = sorted_coords[1] if len(sorted_coords) > 1 else None  # Segunda coordenada más cercana

    target = game_map[next_coords[0]][next_coords[1]]  # El objeto en la siguiente coordenada

    def update_move(new_coords, sq):
        game_map[enemy.x][enemy.y] = sq  # Liberar la posición actual
        enemy.x, enemy.y = new_coords  # Actualizar las coordenadas del enemigo
        game_map[new_coords[0]][new_coords[1]] = enemy  # Mover al enemigo a la nueva posición

    if next_coords == player_coords:
        if isinstance(target, type(player)):  # Verificar si es el jugador
            # print(f'El enemigo atacó al jugador en las coordenadas: {player_coords}')
            combat_logic.combat_logic(enemy, player, game_map, player)

    elif not isinstance(target, BasicEnemy):
        # Si la coordenada más cercana no tiene un enemigo
        if isinstance(target, (BasicItem, BasicEquip, BasicEnvironmentItem)):
            # Si hay un objeto en la siguiente coordenada, intercambiar
            update_move(next_coords, target)
        else:
            # Si no hay objeto, mover al enemigo a la nueva posición
            update_move(next_coords, '.')
    elif isinstance(target, BasicEnemy):
        # Si la coordenada más cercana está ocupada por otro enemigo, moverse a la segunda más cercana
        if second_coords:
            second_target = game_map[second_coords[0]][second_coords[1]]
            if not(isinstance(second_target, BasicEnemy)):  # Si no hay otro enemigo en la segunda coordenada
                if isinstance(second_target, (BasicItem, BasicEquip, BasicEnvironmentItem)):
                    # Si hay un objeto en la segunda coordenada, intercambiar
                    update_move(second_coords, second_target)
                else:
                    # Si no hay objeto, moverse a la segunda coordenada más cercana
                    update_move(second_coords, '.')                    

def nearest_coordinates(coords, player, game_map):
    walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']  # Conjunto en lugar de lista para búsquedas más rápidas

    # Filtramos las coordenadas válidas, descartando aquellas que contengan paredes
    valid_coords = [coord for coord in coords if (game_map[coord[0]][coord[1]] not in walls)]

    # Si no hay coordenadas válidas, devolvemos None
    if not valid_coords:
        return None

    # Devuelve la coordenada más cercana al jugador
    sorted_coords = sorted(valid_coords, key=lambda coord: math.dist(coord, player))
    return sorted_coords
