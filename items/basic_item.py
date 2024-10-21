
from colorama import *
from common_utilities import color_mappings

class basic_item:

    def __init__(self, name, sprite, x, y, rarity, func = None, desc = '', to_player = False):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.desc = desc
        self.color = color_mappings.rarity_color_mapping.get(rarity)
        self.rarity = color_mappings.rarity_name_mapping.get(rarity)
        self.func = func
        self.to_player = to_player
