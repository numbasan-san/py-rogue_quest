
import platform

def load_config():

    system = platform.system()

    if system.lower() == "linux":
        return "clear"
    else:
        return "cls"
