
class player:

    def __init__(self, hp, damage, defense, sprite, x, y, alter_status = None):
        self.max_hp = hp
        self.hp = hp - 5
        
        self.base_damage = damage
        self.damage = damage

        self.base_defense = defense
        self.defense = defense

        self.sprite = sprite
        self.x = x
        self.y = y
        self.alter_status = alter_status

        self.inv_limit = 10
        self.inventory = []
        self.equipment = {
            'sword': None,
            'shield': None
        }
