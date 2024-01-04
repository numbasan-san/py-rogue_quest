
class player:

    def __init__(self, hp, damage, defense, sprite, x, y):
        self.hp = hp
        self.damage = damage
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.inv_limit = 10
        self.inventory = []
        self.equipment = []
