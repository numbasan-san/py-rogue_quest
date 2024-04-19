
class basic_enemy:

    def __init__(self, name, hp, damage, defense, sprite, x, y, exp, range, alter_status = None):
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
