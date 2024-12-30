
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

    # check if the player is 3 squares or less away
    if calculate_distance(player_coords, enemy_coords) >= 4:
        return

    from npc.basic_enemy import BasicEnemy
    player_coords = (player.x, player.y)

    near_coords = [
        (enemy.x + 1, enemy.y),  # right
        (enemy.x - 1, enemy.y),  # left
        (enemy.x, enemy.y - 1),  # up
        (enemy.x, enemy.y + 1)   # down
    ]

    # get the nearest coordinates ordered to the player
    sorted_coords = nearest_coordinates(near_coords, player_coords, game_map)

    if not sorted_coords:
        return  # no movement possible

    next_coords = sorted_coords[0] # nearest coordinate
    second_coords = sorted_coords[1] if len(sorted_coords) > 1 else None # second nearest coordinate

    target = game_map[next_coords[0]][next_coords[1]]  # El objeto en la siguiente coordenada

    # update the map
    def update_move(new_coords, sq):
        game_map[enemy.x][enemy.y] = sq
        enemy.x, enemy.y = new_coords
        game_map[new_coords[0]][new_coords[1]] = enemy

    if next_coords == player_coords: # check if it is the player
        if isinstance(target, type(player)):
            # print(f'El enemigo atacó al jugador en las coordenadas: {player_coords}')
            combat_logic.combat_logic(enemy, player, game_map, player)

    elif not isinstance(target, BasicEnemy): # if the nearest coordinate does not have an enemy
        if isinstance(target, (BasicItem, BasicEquip, BasicEnvironmentItem)):
            update_move(next_coords, target)
        else: # if there is no object
            update_move(next_coords, '.')

    # if the nearest coordinate is occupied by another enemy, move to the second closest
    elif isinstance(target, BasicEnemy):
        if second_coords:
            second_target = game_map[second_coords[0]][second_coords[1]]
            if not(isinstance(second_target, BasicEnemy)):
                if isinstance(second_target, (BasicItem, BasicEquip, BasicEnvironmentItem)):
                    update_move(second_coords, second_target)
                else:
                    update_move(second_coords, '.')                    

def nearest_coordinates(coords, player, game_map):
    walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ', '#']

    # coordinate filtering
    valid_coords = [coord for coord in coords if (game_map[coord[0]][coord[1]] not in walls)]

    # no valid coords? return None
    if not valid_coords:
        return None

    # returns the closest coordinate to the player
    sorted_coords = sorted(valid_coords, key=lambda coord: math.dist(coord, player))
    return sorted_coords
