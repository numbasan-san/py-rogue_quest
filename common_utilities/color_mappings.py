
from colorama import Fore
import config.setting as setting

def get_enemy_color_mapping():
    enemy_color_mapping = {
        1: Fore.GREEN, # beast
        2: Fore.LIGHTBLACK_EX, # undead
        3: Fore.YELLOW, # alchemical
    }
    return enemy_color_mapping

def get_enemy_taxonomy_mapping():
    enemy_taxonomy_mapping = {
        1: (setting.get_language())["taxonomy"]['beast'],
        2: (setting.get_language())["taxonomy"]['undead'],
        3: (setting.get_language())["taxonomy"]['alchemical']
    }
    return enemy_taxonomy_mapping

def get_rarity_color_mapping():
    rarity_color_mapping = {
        1: Fore.WHITE, # common
        2: Fore.CYAN, # uncommon
        3: Fore.GREEN, # rare
        4: Fore.YELLOW, # artefact
        5: Fore.MAGENTA, # mith
    }
    return rarity_color_mapping

def get_rarity_name_mapping():
    rarity_name_mapping = {
        1: (setting.get_language())["rarity"]['common'],
        2: (setting.get_language())["rarity"]['uncommon'],
        3: (setting.get_language())["rarity"]['rare'],
        4: (setting.get_language())["rarity"]['artefact'],
        5: (setting.get_language())["rarity"]['mith'],
    }
    return rarity_name_mapping
