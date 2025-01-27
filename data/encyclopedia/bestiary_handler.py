
import json

PATH = 'data/encyclopedia/data/'

def write_bestiary(monster):
    bestiary_data = get_bestiary()
    if not (any(monster.code == beast["code"] for beast in bestiary_data)):
        enemy_data = {
            "code": monster.code
        }

        bestiary_data.append(enemy_data)

        with open(f'{PATH}bestiary.json', 'w') as json_file:
            json.dump(bestiary_data, json_file, indent=4)

def get_bestiary():
    try:
        file = json.load(open(f'{PATH}bestiary.json', 'r', encoding='utf-8'))
        return file
    except:
        return []
    
