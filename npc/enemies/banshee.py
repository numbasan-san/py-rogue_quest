
from npc.basic_enemy import basic_enemy as enemy

class banshee(enemy):

    def __init__(self, x=1, y=1):
        # Inicializar la clase básica (enemy) con los parámetros de la Banshee
        # name, hp, damage, defense, sprite, x, y, exp, range, taxonomy
        super().__init__('Banshee', 100, 5, 10, 'B', x, y, 20, 1, 2, strategy_ia=self.strategy_ia)

    def strategy_ia(self, game_map):
        x, y = self.x, self.y

        # Posibles posiciones alrededor de la Banshee (arriba, abajo, izquierda, derecha)
        directions = [
            (x, y - 1), # up
            (x, y + 1), # down
            (x - 1, y), # left
            (x + 1, y), # right
        ]

        # Verificar si hay un aliado (otro enemigo) en las casillas alrededor
        i = 0
        for (nx, ny) in directions:
            # Asegurarse de que las coordenadas estén dentro del mapa
            if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
                cell = game_map[nx][ny]
                if isinstance(cell, enemy) and cell is not self:
                    if cell.state:
                        i += 1
                        print(f"Banshee detecta un aliado ({cell.name}) en la dirección ({nx}, {ny}).")
        
        # Si no detecta a ningún aliado
        if i > 0:
            print(f"Banshee detecta {i} aliados.")
            return True  # Hay aliados cerca
        else:
            print("Banshee no detecta aliados cercanos.")
            return False  # No hay aliados cercanos
