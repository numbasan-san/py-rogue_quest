
from colorama import Fore

enemy_color_mapping = {
    1: Fore.GREEN, # beast
    2: Fore.LIGHTBLACK_EX, # undead
    3: Fore.YELLOW, # animated
}

rarity_color_mapping = {
    1: Fore.WHITE, # common
    2: Fore.CYAN, # uncommon
    3: Fore.GREEN, # rare
    4: Fore.YELLOW, # artefact
    5: Fore.MAGENTA, # mith
}

rarity_name_mapping = {
    1: 'common',
    2: 'uncommon',
    3: 'rare',
    4: 'artefact',
    5: 'mith',
}
