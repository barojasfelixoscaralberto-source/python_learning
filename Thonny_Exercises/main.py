# Hey there, using "utils.py"

# as a remind to myself, they have to be in the same folder

import utils
print(utils.greet("Oscar"))
print(utils.square(5))

from utils import greet, square
print(greet("LuisitoComunica"))
print(square(25))