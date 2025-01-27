
from npc.basic_enemy import BasicEnemy as Enemy
import config.setting as setting

class Banshee(Enemy):

    def __init__(self, x=1, y=1):
        # name, hp, damage, defense, x, y, exp, range, taxonomy/color
        desc = (setting.get_language())["enemies"]["banshee"]["description"]
        super().__init__('Banshee', 100, 5, 10, x, y, 20, 1, 2, "bs-B",desc=desc, strategy_ia=self.strategy_ia)
        self.hability_cooldown = 0

    def strategy_ia(self, game_map):
        x, y = self.x, self.y

        directions = [
            (x, y - 1), # up
            (x, y + 1), # down
            (x - 1, y), # left
            (x + 1, y), # right
            (x + 1, y + 1), # down right
            (x + 1, y - 1), # up right
            (x - 1, y + 1), # down left
            (x - 1, y - 1), # up left
        ]

        # banshee checks if she can apply skill
        for (nx, ny) in directions:
            if 0 <= nx < len(game_map) and 0 <= ny < len(game_map[0]):
                cell = game_map[nx][ny]
                if isinstance(cell, Enemy) and self.hability_cooldown >= 5:
                    # print(f"\nBanshee ({self.x}, {self.y}) detecta un aliado ({cell.name}) en la dirección ({nx}, {ny}).")
                    self.damage_buff(cell)
                    self.hability_cooldown = 0

        self.hability_cooldown += 1

    def damage_buff(self, ally):
        print(f"\nBanshee aumenta en 2 puntos el ataque a {ally.name}.")
        ally.damage += 2  # damage buff
