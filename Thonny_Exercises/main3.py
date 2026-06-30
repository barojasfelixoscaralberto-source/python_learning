import Exercise8 as school

student1 = school.Student("Oscar", [5, 5, 9])
student2 = school.Student("Lissandro", [9, 10, 9])
student3 = school.Student("Zaid", [10, 6, 7])


students = [student1, student2, student3]
approved = [s.name for s in students if s.average() >= 7]
print(approved)