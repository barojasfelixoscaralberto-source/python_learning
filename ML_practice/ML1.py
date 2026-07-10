import numpy as np
import pandas as pd

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9] 
])

print(matriz[0:2]) # fila de 0 a 2 sin incluirlo
print(matriz[:,1]) # todas las filas, columna 1
print(matriz[0:2, 1:3]) # (fila, columna)

