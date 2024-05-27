
from items.basic_item import basic_item
from items.basic_equip import basic_equip
from items.basic_environment_item import basic_environment_item
import heapq

class basic_enemy:

    def __init__(self, code, name, hp, damage, defense, sprite, x, y, exp, range, alter_status=None, strategy_ia=None):
        self.name = name
        self.code = code
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

    def dijkstra(self, map, player_position):
        distance = {}
        heap = [(0, player_position)]
        walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']
        while heap:
            d, position = heapq.heappop(heap)
            if position in distance:
                continue
            distance[position] = d
            x, y = position
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] not in walls:
                    heapq.heappush(heap, (d + 1, (nx, ny)))
        return distance

    def move(self, map, player):
        player_position = (player.x, player.y)
        player_distance = self.dijkstra(map, player_position)
        walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']

        x, y = self.x, self.y
        if (x, y) != player_position:
            possible_moves = []

            # Verificar movimientos posibles en las cuatro direcciones
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] not in walls:
                    if isinstance(map[nx][ny], basic_enemy) and map[nx][ny] is not self and map[nx][ny].state:
                        pass
                    else:
                        distance = player_distance.get((nx, ny), float('inf'))
                        possible_moves.append(((nx, ny), distance))
            
            if possible_moves:
                possible_moves.sort(key=lambda pos: pos[1])
                next_move, _ = possible_moves[0]

                # Devolver el objeto guardado a la posición original si existe
                if self.current_item:
                    original_x, original_y = self.item_original_position
                    map[original_x][original_y] = self.current_item
                    self.current_item = None
                    self.item_original_position = None

                # Guardar el objeto en la nueva posición si es de tipo básico
                if isinstance(map[next_move[0]][next_move[1]], (basic_item, basic_equip, basic_environment_item)):
                    self.current_item = map[next_move[0]][next_move[1]]
                    self.item_original_position = (next_move[0], next_move[1])

                # Actualizar la posición del enemigo
                if next_move == player_position:
                    print(f"{self.name} ha alcanzado al jugador!")
                else:
                    if self.current_item:
                        map[x][y] = self.current_item  # Restaurar el objeto en la posición anterior del enemigo
                    else:
                        map[x][y] = '.'  # Dejar una posición vacía si no había objeto
                    self.current_item = None  # Limpiar el objeto actual del enemigo

                    map[next_move[0]][next_move[1]] = self
                    self.x, self.y = next_move
