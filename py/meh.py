def function(a, b):
    while True:
        try:
            div = int(input("Introduzca el dividendo "))
            if div == 0:
                print("Imposible dividir entre cero")
                continue
            break
        except ValueError: 
            print("Tiene que ser un numero, intente de nuevo")
    result = (a * b) / div
    return result


print("Bienvenido, introduce dos numeros que se multiplicaran entre si y escoge el dividendo)")
while True:
    try:
        n1 = int(input("Introduzca el primer numero: "))
    except ValueError:
        print("Solo numeros")
        
        n2 = int(input("Introduzca el segundo numero: "))
        break
    except ValueError:
        print("Solo numeros")

print(function(n1, n2))
    