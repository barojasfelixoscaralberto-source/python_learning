'''
Crea un archivo students.py con una clase student que tenga name, grades (una lista de numeros)
y un metodo average() que devuelva el promedio de sus notas. En main3.py importa la clase
crea 3 estudiantes con notas distintas y usa list comprehension para obtener solo los nombres de
los estudiantes con promedio mayor o igual a 70
'''

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        
    def average(self):
        length = len(self.grades)
        summatory = 0
        for number in self.grades:  
            summatory += number
        aver = summatory / length
        return aver