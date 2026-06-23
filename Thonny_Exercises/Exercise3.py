'''Escribe una funcion que reciba dos numeros y los divida, manejando tanto ValueError
    como ZeroDivisionError, y que en caso de éxito devuelva el resultado'''

def divide(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return None
while True:
    try:
        print("pon dos numeros y el resultado será la division")
        number1 = int(input("Introduzca el primer numero: "))
        number2 = int(input("Introduzca el segundo numero: "))
        result1 = divide(number1,number2)
        if result1 is None:
            print("Imposible dividir entre cero, intente de nuevo")
            continue
        break
    except ValueError:
        print("Eso no es un numero, intente de nuevo")
print(f"El resultado es {result1}")