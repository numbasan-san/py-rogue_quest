
import json, platform

def get_clear_cmd():
    system = platform.system()
    if system.lower() == "linux":
        return "clear"
    else:
        return "cls"

def get_language():
    # Abrir el archivo de configuración y obtener el idioma.
    with open(f'config/data/data_settings.json', 'r', encoding='utf-8') as settings_file:
        lan = json.load(settings_file)['lan']

    # Ahora abrir el archivo de idioma correspondiente.
    with open(f'config/data/languajes/{lan}.json', 'r', encoding='utf-8') as lang_file:
        file = json.load(lang_file)
    
    return file

def set_language(selected_lan):
    FILE_PATH = 'config/data/data_settings.json'
    with open(f'{FILE_PATH}', 'w') as json_file:
        lang = {
            "lan": f"{selected_lan}"
        }
        json.dump(lang, json_file, indent=4)
