
from items.basic_item import basic_item as basic_item
from items.basic_equip import basic_equip as basic_equip
from items.basic_environment_item import basic_environment_item as basic_environment_item

class room_inv_handler:

    def __init__(self):
        self.enemies_room_inv = {
            'in_use': False,
            'elements': []  # room_inv should be stored in this part.
        }
    
    def room_inv_used(self):
        return self.enemies_room_inv['in_use']

    def handle_enemy_collect(self, enemy, map):
        """
            Checks if an enemy passes over an item and stores the item
            in the enemies_room_inv if the condition is met
        """
        enemy_x, enemy_y = enemy.x, enemy.y
        item = map[enemy_x][enemy_y]
        
        if isinstance(item, (basic_item, basic_environment_item, basic_equip)):  # Assuming items are represented by digits
            self.enemies_room_inv['elements'].append({
                'item': item,
                'coor_x': enemy_x,
                'coor_y': enemy_y
            })
            map[enemy_x][enemy_y] = '.'  # Remove item from the map
            self.enemies_room_inv['in_use'] = True
            print(f"Enemy {enemy.sprite} collected the item '{item}' at ({enemy_x}, {enemy_y})")

    def drop_item(self, enemy, map): # This method allows an enemy to drop an item at its current position
        enemy_x, enemy_y = enemy.x, enemy.y
        if self.enemies_room_inv['in_use']:
            for element in self.enemies_room_inv['elements']:
                if element['coor_x'] == enemy_x and element['coor_y'] == enemy_y:
                    map[enemy_x][enemy_y] = element['item']  # Place item back on the map
                    self.enemies_room_inv['elements'].remove(element)
                    print(f"Enemy {enemy.sprite} dropped item '{element['item']}' at ({enemy_x}, {enemy_y})")
                    if len(self.enemies_room_inv['elements']) <= 0:
                        self.enemies_room_inv['in_use'] = False
                    break
