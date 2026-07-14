'''
Crea una matriz 4x4 con numeros del 1 al 16.
Imprime la segunda fila, la tercera columna 
y el promedio de toda la matriz
'''

import numpy as np

# I'd rather use the method starting from an horizontal list then using reshape
# because imagine I have to make a 15x12 matriz, It's only better for me

listation = np.arange(1,17)
matriz = listation.reshape(4, 4)
print(matriz)

# (fila, columna)
print(matriz[1]) # segunda fila (indice 1)
print(matriz[:,2]) # tercera columna (indice 2)
print(np.mean(matriz))
