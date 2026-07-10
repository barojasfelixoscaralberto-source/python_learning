# On this lesson, we'll see numpy and pandas

# as a way to import it from shell (windows CMD) you have to put:
# pip install numpy pandas

'''
from Thonny go to Tools, then manage packages and search for numpy, pandas and install them
for updates go the same but upgrade
'''

# whereas if you're in linux, go to bash and put:
# pip3 install numpy pandas --break-system-packages

# to check if all went well: (pd and np are mostly used)
import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)


lista = [1, 2, 3, 4, 5]

# Array from NumPy
array = np.array(lista)
print(array + 2)

# Arrays work instead of taking the entire list as an obj, it takes every element by itself without using "for" or another list

print(array + 5)
print(array * 2)
print(array > 25)

# Now more methods:

# This one creates a list and puts the number of zeros as every element by separated
print(np.zeros(5))

# This one does the same for .zeros but puts ones
print(np.ones(5))

# This one acts as range() but its "beggining, finish, pass"
# from zero to ten puts numbers but passes two by two
print(np.arange(0, 10, 2))

# This one acts as range but for floats
# divides the range from 0 to 1 in exactly 5 points equally separated (used for graphics)
print(np.linspace(0, 1, 5))



matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matriz)



