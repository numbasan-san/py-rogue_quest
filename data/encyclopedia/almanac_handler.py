

import json

PATH = 'data/encyclopedia/data/'

def write_almanac(item):
    almanac_data = get_almanac()
    if not (any(item.name == thing["name"] for thing in almanac_data)):

        # mapping equipment attributes, excluding somes attributes
        item_data = {
            k: v for k, v in vars(item).items() if k not in ['battle_effect', 'x', 'y', 'func', 'to_player', 'nonfunc']
        }

        almanac_data.append(item_data)

        with open(f'{PATH}almanac.json', 'w',) as json_file:
            json.dump(almanac_data, json_file, indent=4)

def get_almanac():
    try:
        file = json.load(open(f'{PATH}almanac.json', 'r', encoding='utf-8'))
        return file
    except:
        return []
