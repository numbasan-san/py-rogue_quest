
from npc.basic_enemy import basic_enemy as enemy

class kelpie:

    # name, hp, defense, sprite, x, y, exp
    def start_kelpie():
        return enemy('Kelpie', 100, 5, 10, 'K', 2, 2, 8)
