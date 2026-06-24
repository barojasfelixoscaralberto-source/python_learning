numbers = [1,2,3,4,5]
squares = [number ** 2 for number in numbers]
print(squares)
evensquare = [number ** 2 for number in numbers if number % 2 == 0]
print(evensquare)

'''
list comprehension
list = [expresion & for (therefore next to these u can put conditionals)]
'''

words = ["hola", "mundo", "python", "es", "genial"]
result = [word.upper() for word in words if len(word) > 4]
print(result)


# The append goes automatically as the list comprehension works so it is no needed to put it into the list
