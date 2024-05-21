 
# 1: (0, 29)
# 2: (30, 59)
# 3: (60, 119)
# 4: (120, 239)
# 5: (240, 479)
# 6: (480, 959)
# 7: (960, 1919)
# 8: (1920, 3839)
# 9: (3840, 7679)
# 10: (7680, 15359)
# 11: (15360, 30719)
# 12: (30720, 61439)
# 13: (61440, 122879)
# 14: (122880, 245759)
# 15: (245760, 491519)
# 16: (491520, 983039)
# 17: (983040, 1966079)
# 18: (1966080, 3932159)
# 19: (3932160, 7864319)
# 20: (7864320, 15728639)

def find_level(lvl, xp):
    """
        Create a geometric progression based on 30 to determine the amount of experience for the next level up.
    """
    xp_limit = (30 * (2 ** (lvl - 1))) - 1

    if xp >= xp_limit:
        while True:
            lvl += 1
            xp_limit = (30 * (2 ** (lvl - 1))) - 1
            if xp < xp_limit:
                break

    return lvl

def print_levels():
    for i in range(1, 46):
        xp_base = (30 * (2 ** (i - 2)))
        xp_limit = (30 * (2 ** (i - 1))) - 1
        print(f'{i}: ({xp_base}, {xp_limit})')

# print_levels()
# find_level(1, 0)
