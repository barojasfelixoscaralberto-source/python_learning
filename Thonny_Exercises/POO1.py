class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hola, soy {self.name} y tengo {self.age} años"
    
    def celebrate_birthday(self, years):
        self.age += years
        return f"{self.name} ahora tiene {self.age} años"
    
oscar = Person("Oscar", 17)
print(oscar.greet())
print(oscar.celebrate_birthday(50))
print(oscar.greet())


