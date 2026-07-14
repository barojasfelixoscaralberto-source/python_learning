import numpy as np
import pandas as pd

matriz = np.array([
    [1, 2, 3], # fila 0
    [4, 5, 6], # fila 1
    [7, 8, 9]  # fila 2
])#col0 col1 col2

print(matriz[0:2]) # fila de 0 a 2 sin incluirlo
print(matriz[:,1]) # todas las filas, columna 1
print(matriz[0:2, 1:3]) # (fila, columna)

