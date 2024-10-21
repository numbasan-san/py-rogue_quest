
from engine import *
from common_utilities.utilities import *
from common_utilities.title import get_title

utilities.print_title(get_title())
input()

eng = engine()

while not(eng.end_exe):
    eng.run()
