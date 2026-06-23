''' Tienes una lista de productos con nombre y precio
    Escribe una funcion que devuelva solo los productos que cuestan menos de $100'''

products = [
    {"name": "Mouse", "price": 150},
    {"name": "Teclado", "price": 80},
    {"name": "Monitor", "price": 900},
    {"name": "Audífonos", "price": 50}
           ]
def below100(list1):
    list2 = []
    for product in list1:
        if product["price"] <= 100:
            list2.append(product)
    return list2

result = below100(products)
print(result)
