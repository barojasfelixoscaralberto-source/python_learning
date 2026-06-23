'''programa con while True que pida productos (nombre y precio) hasta que el usuario escriba salir.
    guarda cada uno en una lista de diccionarios, al final imprime el promedio de precios'''


inventory = []

while True:
    try:
        name = str(input("Indique el nombre del producto: "))
        price = int(input("Indique el precio del producto (solo los numeros): "))
        inventory.append({"nombre": name, "precio": price})
        leaving = input("Salir?, Indique Si o No. ").strip().lower()
        if leaving == "si":
            break
        elif leaving == "no":
            print("continue con otro producto")
        else:
            print("Por favor ponga el resultado")
    except ValueError:
        print("El precio debe ser en numeros")
print(inventory)


def generalaverage(list1):
   total = 0
   for product in list1:
       total += product["precio"]
   average = total / len(list1)
   return average
    
    
print(f"Promedio de precios: {generalaverage(inventory)}")