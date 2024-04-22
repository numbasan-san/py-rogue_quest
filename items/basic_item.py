
class basic_item:

    def __init__(self, code, name, sprite, x, y, func = None, to_player = False):
        self.name = name
        self.code = code
        self.sprite = sprite
        self.x = x
        self.y = y
        self.func = func
        self.to_player = to_player
