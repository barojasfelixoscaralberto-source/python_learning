''' pida al usuario su nombre y edad
    guarde la informacion en un .txt en modo append
    formato nombre, edad'''

while True:
    try:
        name = str(input("Introduzca su nombre: "))
        age = int(input("Introduzca su edad: "))
        break
    except ValueError:
        print("Introduzca bien el valor")
        

with open("personas.txt", "a") as file:
    file.write(f"Nombre: {name}, Edad: {age}\n")