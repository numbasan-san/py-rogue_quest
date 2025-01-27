
import random
from ui import hud
import config.setting as sttng
from items.basic_equip import BasicEquip

class FireSword(BasicEquip):

    # name, sprite, x, y, damage, critic, defense
    def __init__(self, x=1, y=1):
        name = (sttng.get_language())["items"]["fire_sword"]["name"]
        sprite = '|'
        damage = 20
        critic = 10
        defense = 0
        to_player = True
        # name, sprite, x, y, damage, critic, defense, rarity, func, to_player, battle_effect, desc, nonfunc
        super().__init__(name, sprite, x, y, damage, critic, defense, 5, "fs-|", func = self.use_function, to_player = to_player, battle_effect=self.use_alter_status, desc = (sttng.get_language())["items"]["fire_sword"]["desc"], nonfunc = self.nonuse_function)
    
    def burn(self, victim): # sword's efect
        victim.hp -= 1
        hud.print_effect(f'\n\n[{victim.name}] {(sttng.get_language())["items"]["fire_sword"]["effect"]}.')

    def use_function(self, player):
        
        # check if the player have an sword or not
        if player.equipment['sword'] == None or (player.equipment['sword']).name != self.name:

            # sword in equipment and buff to damage
            player.equipment['sword'] = self
            hud.print_effect(f'\n[{self.name}] {(sttng.get_language())["game"]["equip_action"]["equipped"]}.')
            player.damage = (player.equipment['sword']).damage + player.damage
        else:
            hud.print_effect(f'\n[{self.name}] {(sttng.get_language())["game"]["equip_action"]["already_equipped"]}.')
    
    def nonuse_function(self, player, msg):
        hud.print_effect(msg)
        player.damage = player.damage - (player.equipment['sword']).damage
        player.equipment['sword'] = None
        
    def use_alter_status(self, victim): # is the altered state effect of the weapon
        var = random.randint(0, 10)
        if var > 8:
            victim.alter_status = [self.burn, 5]

