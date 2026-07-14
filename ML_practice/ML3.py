import numpy as np
import pandas as pd

datos = np.array([4, 7, 2, 9, 1, 5, 8, 3, 6])

mask = datos > 5
print(mask) # in arrays, the statement above works as a boolean. 
# it shows the entire list but on booleans values

print(datos[mask]) # these two work but the same
print(datos[datos > 5])

array = np.arange(1, 10)
print(array)
print(array.reshape(3, 3))