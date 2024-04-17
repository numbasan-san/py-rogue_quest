
# def find_level(xp):
#     xp_ranges = {
#      "1": range(0, 29),
#      "2": range(30, 89),
#      "3": range(90, 269),
#      "4": range(270, 809),
#      "5": range(810, 2429),
#      "6": range(2430, 7289),
#      "7": range(7290, 21869),
#      "8": range(21870, 21870),
# }

def find_level(lvl, xp):
    xp_limit = (30 * (2 ** (lvl - 1))) - 1

    if xp >= xp_limit:
        while True:
            lvl += 1
            xp_limit = (30 * (2 ** (lvl - 1))) - 1
            if xp <= xp_limit:
                break

    return lvl

# def print_levels():
#     for i in range(1, 46):
#         xp_base = (30 * (2 ** (i - 2)))
#         xp_limit = (30 * (2 ** (i - 1))) - 1
#         print(f'{i}: ({xp_base}, {xp_limit})')

# print_levels()
