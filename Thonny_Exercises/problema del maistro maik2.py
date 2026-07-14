'''
crea un codigo que defina dos clases padre, una como jugador y otra como enemigo
jugador como clase padre va a tener: recibir daño, atacar, curar
obvio como atributos van a estar las estadisticas
clases hijas (3 por jugador y/o enemigo), en cada una cambiar cierta cosa
(ataque diferente o reciba diferente)
enemigo igual atacar, recibir daño, dar recompensa
'''

'''
en otro archivo traer esas clases y hacer el rpg en consola
'''

class Player:
    def __init__(self, name):
        self.name = name
        
    def stadistics(self, health, attack):
        self.health = health
        self.attack = attack

# Tank receives less damage from enemy
class Tank(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 20
    
    def stadisticstank(self):
        return f"Las estadisticas para el tanque son: {self.health} HP y {self.attack_power} de daño"
        
        
    
# Explorer receives less health but restores more health
class Explorer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.attack_power = 30
        
    def stadisticsexplorer(self):
        return f"Las estadisticas para el explorador son: {self.health} HP y {self.attack_power} de daño"
        
# Soldier receives the same damage but makes more damage
class Soldier(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 50        
    def stadisticssoldier(self):
        return f"Las estadisticas para el soldado son: {self.health} HP y {self.attack_power} de daño"
        
        
        
class Enemy:
    def __init__(self, name):
        self.name = name
        
    def stadistics(self, health, attack):
        self.health = health
        self.attack = attack
        
# Demon it's the default soldier for enemies
class Demon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 50
        
    def stadisticsdemon(self):
        return f"Te enfrentaras a un demonio cuya vida es de {self.health} HP y daño de {self.attack_power}"
        
# Beast works as a tank but for enemies
class Beast(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 15
        
    def stadisticsbeast(self):
        return f"Te enfrentaras a una bestia cuya vida es de {self.health} HP y daño de {self.attack_power}"
        
# Witch is like the explorer but for enemies
class Witch(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.attack_power = 30
        
    def stadisticswitch(self):
        return f"Te enfrentaras a una bruja cuya vida es de {self.health} HP y daño de {self.attack_power}"
    
# Here starts the UX from the user (all of it will work from an import)

import random

# When the code starts, all of these will start

while True:
        print("Bienvenido viajero, ¿listo para una travesía?. Seleccione si o no")
        decision = input("ponga aqui su eleccion: ").strip().lower()
        if decision == "si":
            nameplayer = input("ponga su nombre: ")
            jugador = Player(nameplayer)
            break
        elif decision == "no":
            print("pues que haces aqui entonces >:v")
        else:
            print("creo que no me di a entender bien...")
            print("SI O NO")
            
            
# Here the player choses his rol

while True:
    print(f"Buena desicion {nameplayer}, escoja su rol: ")
    rol = input("Escoge entre: Soldado, Tanque o Explorador. ").strip().lower()
    
    if rol == "soldado":
        jugador = Soldier(nameplayer)
        print(jugador.stadisticssoldier())
        print("Ahora eres un soldado")
        break
    elif rol == "tanque":
        jugador = Tank(nameplayer)
        print(jugador.stadisticstank())
        print("Ahora eres un tanque")
        break
    elif rol == "explorador":
        jugador = Explorer(nameplayer)
        print(jugador.stadisticsexplorer())
        print("Ahora eres un explorador")
        break
    else:
        print("Por favor, escoja uno de los roles indicados")
        
# Now, lets choose the enemy

while True:
    print("Ahora escoge a tu enemigo, puede ser un demonio, una bestia o una bruja")
    enemy = input("Ponga aqui su eleccion: ").strip().lower()
    
    if enemy == "demonio":
        nameenemy = "Demonio"
        enemigo = Demon(nameenemy)
        print(enemigo.stadisticsdemon())
        print("El enemigo será un Demonio")
        break
    elif enemy == "bestia":
        nameenemy = "Bestia"
        enemigo = Beast(nameenemy)
        print(enemigo.stadisticsbeast())
        print("El enemigo será una bestia")
        break
    elif enemy == "bruja":
        nameenemy = "Bruja"
        enemigo = Witch(nameenemy)
        print(enemigo.stadisticswitch())
        print("El enemigo será una bruja")
        break
    else:
        print("Lo que pusiste no está entre las opciones, intenta de nuevo")
        
# Now with both chosen, let's deal a fight between them

while jugador.health > 0 and enemigo.health > 0:
    print(f"\n{jugador.name} HP: {jugador.health} | {enemigo.name} HP: {enemigo.health}")
    action = input("¿Que hacer? (atacar/curar): ").strip().lower()
    
    if action == "atacar":
        enemigo.health -= jugador.attack_power
        
    elif action == "curar":
        jugador.health += 15
        
    else:
        print("que layos elegiste")
    
    desiciones = ["atacar", "curar", "no hace nada"]
    desicion_enemigo = random.choice(desiciones)
    
    if desicion_enemigo == "atacar":
        print("¡El enemigo ataca!")
        jugador.health -= enemigo.attack_power
        
    elif desicion_enemigo == "no hace nada":
        print("XD no hace nada")
        
    else:
        print("¡El enemigo se cura!")
        enemigo.health += 15
        
if enemigo.health <= 0:
    print("FELICIDADES HAS GANADO")
else:
    print("EL ENEMIGO HA GANADO")

        
        
    
    
    


        
    