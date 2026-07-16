'''
Crea un array del 1 al 20
filtra solo los múltiplos de 3 e imprime su suma
'''

import numpy as np

array = np.arange(1, 21)
print(array)

multiples_of_3 = array % 3 == 0
list_of_mult3 = array[multiples_of_3]
print(list_of_mult3)
sum_mult3 = sum(list_of_mult3)
print(sum_mult3)