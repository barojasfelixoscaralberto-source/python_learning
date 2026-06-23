''' Pida al usuario una frase
    Cuenta cuantas palabras tiene y guarda el resultado en un .txt
    con formato Frase: x, Palabras: y'''

while True:
    try:
        frase = str(input("Introduzca su frase (Respete los espacios): "))
        break
    except ValueError:
        print("Tiene que ser una frase")
        
cuenta2 = len(frase.split())

print(cuenta2)


with open("log.txt", "a") as file:
    file.write(f"Frase: {frase}, Palabras: {cuenta2}\n")
    
with open("log.txt", "r") as file:
    content = file.read()
    print(content)