
class player:

    def __init__(self, hp, defense, sprite, x, y):
        self.hp = hp
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.inv_limit = 0
        self.inventory = []
