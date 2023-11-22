
class character:

    def __init__(self, hp, defense, sprite, x, y, player = False):
        self.hp = hp
        self.defense = defense
        self.sprite = sprite
        self.x = x
        self.y = y
        self.inventory = None
        if player:
            self.inventory = []
