
from npc.basic_enemy import basic_enemy as enemy

class banshee:

    # Inicialización de la Banshee
    def start(self, x, y):
        self.x = x
        self.y = y
        return enemy('bs-b', 'Banshee', 100, 5, 10, 'B', x, y, 20, 2, strategy_ia=self.strategy_ia)

    # Función de IA de la Banshee
    def strategy_ia(self, map):
        x, y = self.x, self.y
        radius = 2
        
        # Verificar las casillas en el radio especificado
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                    if isinstance(map[nx][ny], enemy) and map[nx][ny] is not self:
                        print("No estoy sola")