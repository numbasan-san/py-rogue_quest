
def find_level(xp):
    xp_ranges = {
         "1": range(0, (10 - 1)),
         "2": range(10, (20 - 1)),
         "3": range(20, (40 - 1)),
         "4": range(40, (80 - 1)),
         "5": range(80, (160 - 1)),
         "6": range(160, (320 - 1)),
         "7": range(320, (640 - 1)),
         "8": range(640, (1300 - 1)),
         "9": range(1300, (2600 - 1)),
        "10": range(2600, (5200 - 1)),
        "11": range(5200, (13000 - 1)),
        "12": range(13000, (26000 - 1)),
        "13": range(26000, (50000 - 1)),
        "14": range(50000, (100000 - 1)),
        "15": range(100000, (200000 - 1)),
        "16": range(200000, (400000 - 1)),
        "17": range(400000, (800000 - 1)),
        "18": range(800000, (2000000 - 1)),
        "19": range(2000000, (4000000 - 1)),
        "20": range(4000000, (8000000 - 1)),
        "21": range(8000000, (16000000 - 1)),
        "22": range(16000000),
    }

    for level_range, xp_range in xp_ranges.items():
        if xp in xp_range:
            return level_range

    return "22"

# Ejemplo de uso:
# xp = int(input("Ingrese la cantidad de experiencia: "))
# level = find_level(xp)
# print(f"Nivel correspondiente para {xp} de experiencia: {level}")
