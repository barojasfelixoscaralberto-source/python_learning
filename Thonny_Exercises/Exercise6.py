'''
Tienes una lista de temperaturas en Celcius
Conviertelas a Farenheit usando list comprehension
y filtra solo las que sean mayores a 100°F
F = (c * 9/5) + 32
'''

celsius = [0, 20, 37, 50, 100, -10, 25]

farenheit = [(temperature * 9/5) + 32 for temperature in celsius if ((temperature * 9/5) + 32) >= 100]
print(farenheit)