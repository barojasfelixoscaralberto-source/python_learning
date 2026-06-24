'''
Before using NumPy we have to complete comprehension about modules & its imports
In simply words it is a form to reuse a document ".py" in another dc
'''

# first one: random

import random

#prints a random number
number1 = random.randint(0, 100)
print(number1)
print(random.randint(101, 200))

# prints a number between that range
print(random.randrange(0, 100))

# only prints float numbers
print(random.random())

# prints a float number between that range
print(random.uniform(10, 11))

# now using lists

listation = [1,2,3,4,5]

print(random.choices(listation))
print(random.sample(listation, 4))

print(" " * 20)

'''
Now with math and os
'''

import math
print(math.sqrt(16))
print(math.pi)

import os
print(os.getcwd())

'''
another form to use it
'''

from math import sqrt, pi
print(sqrt(25))
print(pi)



    