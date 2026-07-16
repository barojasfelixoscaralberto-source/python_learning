import numpy as np
import pandas as pd

datos = np.array([4, 7, 2, 9, 1, 5, 8, 3, 6])

print(datos.min()) # works as the minimum but for arrays
print(datos.max()) # works as the maximum but for arrays
print(datos.mean()) # mean talks about average
print(np.median(datos)) # it's the medium value of the list
                        # when u order them from min to max
print(round(np.std(datos), 2)) # it's the standard deviation
