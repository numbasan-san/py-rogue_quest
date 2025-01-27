
from colorama import *
from common_utilities import color_mappings

class BasicItem:

    def __init__(self, name, sprite, x, y, rarity, code, func = None, desc = '', to_player = False):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.desc = desc
        self.color = (color_mappings.get_rarity_color_mapping()).get(rarity)
        self.rarity = rarity
        self.func = func
        self.to_player = to_player
        self.code = code
