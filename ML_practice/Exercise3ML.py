'''
Dado este array:
datos = np.array([15, 3, 22, 8, 47, 1, 33, 12, 5, 28])
imprime el maximo, el minimo, media.
filtra los valores que estan por encima de la media
'''

import numpy as np
datos = np.array([15, 3, 22, 8, 47, 1, 33, 12, 5, 28])

print(datos.min())
print(datos.max())
media = datos.mean()
print(media)
print("Valores filtrados: ", datos[datos > media])
