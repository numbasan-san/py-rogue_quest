
from getpass import getpass
import math, combat_logic
from items.basic_equip import basic_equip
from items.basic_item import basic_item
from items.basic_environment_item import basic_environment_item

class basic_enemy:

    def __init__(self, name, hp, damage, defense, sprite, x, y, exp, range, alter_status = None, move_ia = None, strategy_ia = None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.exp = exp
        self.range = range
        self.state = True
        self.alter_status = alter_status
        self.move_ia = self.move if move_ia is None else move_ia
        self.strategy_ia = strategy_ia

    def move(self, game_map, player):
        player_coords = (player.x, player.y)
        
        # Coordenadas adyacentes (Right, Left, Up, Down)
        near_coords = [
            (self.x + 1, self.y),  # Derecha
            (self.x - 1, self.y),  # Izquierda
            (self.x, self.y - 1),  # Arriba
            (self.x, self.y + 1)   # Abajo
        ]

        # Obtener la coordenada más cercana al jugador
        next_coords = self.nearest_coordinate(near_coords, player_coords, game_map)

        if next_coords:
            target = game_map[next_coords[0]][next_coords[1]]  # El objeto en la siguiente coordenada
            
            def update_move(sq):
                game_map[self.x][self.y] = sq  # Liberar la posición actual
                self.x, self.y = next_coords  # Actualizar las coordenadas del enemigo
                game_map[next_coords[0]][next_coords[1]] = self  # Mover al enemigo a la nueva posición

            if next_coords == player_coords:
                if isinstance(target, type(player)):  # Verificar si es realmente el jugador
                    print(f'El enemigo atacó al jugador en las coordenadas: {player_coords}')
                    # Aquí puedes llamar a la lógica de combate
                    combat_logic.combat_logic(self, player, game_map, player)

            elif not isinstance(target, type(self)):
                # Si la siguiente coordenada no tiene un enemigo
                if isinstance(target, (basic_item, basic_equip, basic_environment_item)):
                    # Si hay un objeto en la siguiente coordenada, intercambiar
                    update_move(target)
                else:
                    # Si no hay objeto, mover al enemigo a la nueva posición
                    update_move('.')
            elif isinstance(target, type(self)):
                if not target.state:
                    update_move('.')

                

    def nearest_coordinate(self, coords, player, game_map):
        walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']  # Conjunto en lugar de lista para búsquedas más rápidas

        # Filtramos las coordenadas válidas, descartando aquellas que contengan paredes
        valid_coords = [coord for coord in coords if (game_map[coord[0]][coord[1]] not in walls)]

        # Si no hay coordenadas válidas, devolvemos None
        if not valid_coords:
            return None

        final_coords = min(valid_coords, key=lambda coord: math.dist(coord, player))

        # Ordenamos las coordenadas válidas por la distancia al jugador y devolvemos la más cercana
        return final_coords
