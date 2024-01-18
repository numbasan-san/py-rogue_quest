
from npc.basic_enemy import basic_enemy as enemy

class titan:

    # name, hp, defense, sprite, x, y, exp
    def start_titan():
        return enemy('Titan', 100, 70, 10, 'T', 2, 2, 10)
