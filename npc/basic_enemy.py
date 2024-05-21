
import heapq
from room_inv_handler import room_inv_handler
from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from items.basic_environment_item import basic_environment_item as basic_environment_item

class basic_enemy:

    def __init__(self, code, name, hp, damage, defense, sprite, x, y, exp, range, alter_status = None, strategy_ia = None):
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
        self.handler = room_inv_handler()

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
            
            # Intentar moverse en el eje x primero
            if x != player_position[0]:
                dx = 1 if player_position[0] > x else -1
                nx, ny = x + dx, y
                if 0 <= nx < len(map) and map[nx][ny] not in walls:
                    if isinstance(map[nx][ny], basic_enemy) and map[nx][ny] is not self and map[nx][ny].state:
                        pass
                    elif map[nx][ny] == '.' or map[nx][ny] == player.sprite or (isinstance(map[nx][ny], basic_enemy) and not map[nx][ny].state) or isinstance(map[nx][ny], (basic_item, basic_environment_item, basic_equip)):
                        distance = player_distance.get((nx, ny), float('inf'))
                        possible_moves.append(((nx, ny), distance))

            # Intentar moverse en el eje y si no se puede mover en el eje x
            if y != player_position[1]:
                dy = 1 if player_position[1] > y else -1
                nx, ny = x, y + dy
                if 0 <= ny < len(map[0]) and map[nx][ny] not in walls:
                    if isinstance(map[nx][ny], basic_enemy) and map[nx][ny] is not self and map[nx][ny].state:
                        pass
                    elif map[nx][ny] == '.' or map[nx][ny] == player.sprite or (isinstance(map[nx][ny], basic_enemy) and not map[nx][ny].state) or isinstance(map[nx][ny], (basic_item, basic_environment_item, basic_equip)):
                        distance = player_distance.get((nx, ny), float('inf'))
                        possible_moves.append(((nx, ny), distance))
            
            '''
                Aún persiste el tema de que no suelta el objeto, solo el piso. Pero almenos no se queda quieto ante un objeto.
            '''

            if possible_moves:
                possible_moves.sort(key=lambda pos: pos[1])
                next_move, _ = possible_moves[0]
                if next_move == player_position:
                    print(f"{self.name} ha alcanzado al jugador!")
                else:
                    # Handle item collection and dropping
                    if isinstance(map[self.x][self.y], (basic_item, basic_environment_item, basic_equip)):
                        self.handler.handle_enemy_collect(self, map)
                    else:
                        map[next_move[0]][next_move[1]] = self
                        map[x][y] = '.'
                        self.x, self.y = next_move
                        self.handler.drop_item(self, map)
