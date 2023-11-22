
import os, random

PATH = "mapas/"
MAPS_IN_PATH = os.listdir(PATH)
MAP = random.choice(MAPS_IN_PATH) # 'mapa.txt'

def count_line(archive_path): # Counting lines of txt map selected.
    archive = open(archive_path, "r")
    lines = len(archive.readlines())
    return lines

def charge_map(): # Load the map.
    map_path = PATH + MAP

    with open(map_path, "r") as preloaded_map:
        map = []

        for i in range(count_line(map_path)): # Loop for each line of the map.
            chain = []
            line = preloaded_map.readline() # Read the current line.

            for i in range(len(line)): # Append each element in the "chain".
                chain.append(line[i])

            chain.pop(-1) # Drop off the jump line.
            map.append(chain) # Append the "chain" to the map.

        return map


print(f'longitud de mapa: {len(charge_map())}')
for line in charge_map():
    floor = ''
    print(f'longitud de línea: {len(line)}')
    '''for square in line:
        floor += square
    print(floor)'''