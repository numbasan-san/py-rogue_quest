
from colorama import Fore
import config.setting as setting

lan = setting.get_language()

enemy_color_mapping = {
    1: Fore.GREEN, # beast
    2: Fore.LIGHTBLACK_EX, # undead
    3: Fore.YELLOW, # alchemical
}

enemy_taxonomy_mapping = {
    1: lan["taxonomy"]['beast'],
    2: lan["taxonomy"]['undead'],
    3: lan["taxonomy"]['alchemical']
}

rarity_color_mapping = {
    1: Fore.WHITE, # common
    2: Fore.CYAN, # uncommon
    3: Fore.GREEN, # rare
    4: Fore.YELLOW, # artefact
    5: Fore.MAGENTA, # mith
}

rarity_name_mapping = {
    1: lan["rarity"]['common'],
    2: lan["rarity"]['uncommon'],
    3: lan["rarity"]['rare'],
    4: lan["rarity"]['artefact'],
    5: lan["rarity"]['mith'],
}
