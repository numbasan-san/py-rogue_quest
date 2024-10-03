
import math, combat_logic

class basic_enemy:

    def __init__(self, name, hp, damage, defense, sprite, x, y, exp, range, alter_status=None, strategy_ia=None):
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
        self.move_ia = self.move
        self.strategy_ia = strategy_ia
        self.current_item = None  # Almacena el objeto actual
        self.item_original_position = None  # Almacena la posición original del objeto

    
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
            if next_coords == player_coords:
                # Si las coordenadas coinciden con las del jugador, el enemigo lo atacaría (puede agregar lógica de ataque)
                combat_logic.combat_logic(self, game_map[player_coords[0]][player_coords[1]], game_map)
                print(f'{self.name} intenta atacar al jugador.')
            elif not isinstance(game_map[next_coords[0]][next_coords[1]], type(self)):
                # Si no hay otro enemigo en esa posición, mover a 'self'
                game_map[self.x][self.y] = '.'  # Liberar la posición actual
                game_map[next_coords[0]][next_coords[1]] = self  # Mover a la nueva posición
                self.x, self.y = next_coords  # Actualizar las coordenadas del enemigo


    def nearest_coordinate(self, coords, player, game_map):
        walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']  # Conjunto en lugar de lista para búsquedas más rápidas

        # Filtramos las coordenadas válidas, descartando aquellas que contengan paredes
        valid_coords = [coord for coord in coords if game_map[coord[0]][coord[1]] not in walls]

        # Si no hay coordenadas válidas, devolvemos None
        if not valid_coords:
            return None

        # Ordenamos las coordenadas válidas por la distancia al jugador y devolvemos la más cercana
        return min(valid_coords, key=lambda coord: math.dist(coord, player))
