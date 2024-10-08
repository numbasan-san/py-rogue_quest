
from npc.basic_enemy import basic_enemy as enemy

class banshee:

    # name, hp, damage, defense, sprite, x, y, exp, range
    def start(self, x = 1, y = 1):
        self.x = x
        self.y = y
        return enemy('Banshee', 100, 5, 10, 'B', x, y, 20, 2, move_ia=None, strategy_ia=self.strategy_ia)

    def strategy_ia(self, map):
        x, y = self.x, self.y
        radius = 1
        
        # Verificar las casillas en el radio especificado
        for dx in range(-radius, radius + 1):
            for dy in range(-radius, radius + 1):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                    if isinstance(map[nx][ny], enemy) and map[nx][ny] is not self:
                        print("\nNo estoy sola")