
class basic_environment_item:

    def __init__(self, code, name, sprite, x, y, func = None):
        self.name = name
        self.code = code
        self.sprite = sprite
        self.x = x
        self.y = y
        self.func = func
