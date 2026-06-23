class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        return f"Hola, soy {self.name} y tengo {self.age} años"
    
class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
        
    def study(self):
        return f"{self.name} está estudiando {self.major}"
    
oscar = Student("Oscar", 17, "ISC")
print(oscar.greet())
print(oscar.study())