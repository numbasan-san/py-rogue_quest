
PATH = "mapas/"

def count_line(archive_path): # Counting lines of txt map selected.
    archive = open(archive_path, "r")
    lines = len(archive.readlines())
    return lines

def set_map(map_name): # Load the map.
    map_path = PATH + map_name # map_set()

    with open(map_path, "r") as preloaded_map:
        map = []

        for i in range(count_line(map_path)): # Loop for each line of the map.
            chain = []
            line = preloaded_map.readline() # Read the current line.
            line = line.replace(":", "┗").replace("|", "┃").replace('-', '━').replace('_', '┛').replace('&', '┓').replace('!', '┏')
            
            for i in range(len(line)): # Append each element in the "chain".
                chain.append(line[i])
            # print(line)
            chain.pop(-1) # Drop off the jump line.
            map.append(chain) # Append the "chain" to the map.
            
        return map

# set_map('test_map2.txt')

'''
━ ┃ ┏ ┓ ┗ ┛ ┣ ┫ ┳ ┻ ╋
'''