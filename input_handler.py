
from utilities import *

def valid_move(x, y, map, player_around):

    len_x = (len(map[x]) - 1)
    len_y = (len(map) - 1)

    walls = ['━', '┃', '┏', '┓', '┗', '┛', '┣', '┫', '┳', '┻', '╋', ' ']

    # directions validation
    move_opt = ['w', 'a', 's', 'd']
    if (x < 1  or y >= len(map[x - 1])) or (player_around[0] in walls): # To remove up when it's in the top.
        move_opt.remove('w')
    if len_y == x or y >= len(map[x + 1]) or (player_around[1] in walls): # To remove down when it's in the bottom.
        move_opt.remove('s')
    if y < 1 or (player_around[2] in walls): # To rigth when it's in the right limit.
        move_opt.remove('a')
    if len_x == y or (player_around[3] in walls): # To left when it's in the left limit.
        move_opt.remove('d')

    key = utilities.opciones('Elija por donde ir', move_opt)

    # move vectors
    if key == 'w':
        return {'move': -1, 'direc': 'w', 'msg': 'El jugador se desplazó hacia arriba.'}
    if key == 'a':
        return {'move': -1, 'direc': 'a', 'msg': 'El jugador se desplazó hacia la izquierda.'}
    if key == 's':
        return {'move': 1, 'direc': 's', 'msg': 'El jugador se desplazó hacia abajo.'}
    if key == 'd':
        return {'move': 1, 'direc':'d', 'msg': 'El jugador se desplazó hacia la derecha.'}
