
class basic_item:

    def __init__(self, name, sprite, x, y, func=None):
        self.name = name
        self.sprite = sprite
        self.x = x
        self.y = y
        self.func = func

    def funtion(msg, efect, used_player = False):
        return {
            'msg': msg,
            'efect': efect,
            'used_player': used_player
        }



# class basic_item:

#     def __init__(self, name, sprite, x, y, func=None):
#         self.name = name
#         self.sprite = sprite
#         self.x = x
#         self.y = y
#         self.item_func = func  # Asegúrate de asignar func al atributo item_func

#     def use_item(self, player):
#         if self.item_func is not None:
#             return self.item_func(player)
#         else:
#             print(f'Error: {self.name} no tiene una función asociada.')
#             return False
