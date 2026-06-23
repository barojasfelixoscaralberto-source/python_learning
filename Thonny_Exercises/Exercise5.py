''' Crea un archivo .txt con 5-6 numeros (0-100) escritos manualmente uno por linea.
    Luego escribe un programa que los lea, calcule el promedio e imprima si es aprobatorio (>= 70) o no.'''


import random

numbers = [random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100), random.randint(0,100)]

with open("notas.txt", "w") as file:
    file.write(f"{numbers[0]}\n")
    file.write(f"{numbers[1]}\n")
    file.write(f"{numbers[2]}\n")
    file.write(f"{numbers[3]}\n")
    file.write(f"{numbers[4]}\n")
    
with open("notas.txt", "r") as file:
    content = file.readlines()
    total = 0
    print(str(content))
    for number in content:
        total += int(number)
    average = total / len(content)
    if average >= 70:
        result = "Pass"
    else:
        result = "Fail"
        
    print(average, result)

