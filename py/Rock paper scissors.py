import random

opciones = ["piedra", "papel", "tijeras"]

usuario = input("Escoja piedra, papel o tijeras: ").strip().lower()
if usuario not in opciones:
    print("que es eso chaval, una de las tres >:v")
    exit()

cpu = random.choice(opciones)
print(f"La cpu escogio: {cpu} ¿cagaste?")

# ganador
if usuario == cpu:
    print("faaah empate")
elif usuario == "piedra" and cpu == "tijeras":
    print("ganaste causa")
elif usuario == "papel" and cpu == "piedra":
    print("ganaste causa")
elif usuario == "tijeras" and cpu == "papel":
    print("ganaste causa")
else:
    print("Perdiste pe causita")
