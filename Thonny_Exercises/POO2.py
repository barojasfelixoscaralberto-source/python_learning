'''
Escribe una clase con
dunder init que reciba name y price
un metodo apply_discount que reduzca el precio segun el porcentaje y devuelva el nuevo precio'''

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def apply_discount(self, discount):
        less = self.price * (discount/100)
        total = self.price - less
        return total

product1 = Product("Tomate", 100)

print(product1.apply_discount(20))