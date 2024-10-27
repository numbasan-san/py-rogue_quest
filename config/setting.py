
import platform

def get_clear_cmd():
    system = platform.system()
    if system.lower() == "linux": return "clear" 
    else: return "cls"
