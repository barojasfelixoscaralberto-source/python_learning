'''
Crea un archivo calculator.py con una clase calculator que tenga 4 metodos
add, substract, multiply y divide (con ZeroDivisionError)
luego importa la clase en main2.py y prueba los 4 metodos
'''

class calculator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def add(self):
        summatory = self.number1 + self.number2
        return f"La suma da {summatory}"
    
    def subtract(self):
        subtraction = self.number1 - self.number2
        return f"La resta da {subtraction}"
    
    def multiply(self):
        mult = self.number1 * self.number2
        return f"La multiplicacion da {mult}"
    
    def divide(self):
        try:
            division = self.number1 / self.number2
            return f"La division da {division}"
        except ZeroDivisionError:
            return "Error: Imposible dividir entre 0"
            