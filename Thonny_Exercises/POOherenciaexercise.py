'''
Crea una clase Animal con name y sound, y un metodo make_sound() que devuelva f{name} hace {sound}"
Luego crea una clase dog que herede de animal, y que agregue un metodo propio fetch() que devuelva f"{name} trae la pelota"
'''

class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
        
    def __str__(self):
        return f"Animal: {self.name}, Sonido: {self.sound}"
        
    def make_sound(self):
        return f"El {self.name} hace {self.sound}"
    
class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name, sound)
    
    def fetch(self):
        return f"{self.name} ve por la pelota"
    
animal = Animal("Perro", "woof")
print(animal)
    
animalito = Dog("Perro", "woof")
print(animalito.make_sound())
print(animalito.fetch())


# __init__ >>
# __str__ >>
