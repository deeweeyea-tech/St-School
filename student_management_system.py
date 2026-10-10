
class Student:
    def __init__(self, student_id, name, gender, age):
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.age = age

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Gender: {self.gender}, Age: {self.age}")


s1 = Student(1, "Divya", "Female", 25)
s2 = Student(2, "Rizwan", "Male", 22)
s3 = Student(3, "Vaishnavi", "Female", 21)
s4 = Student(4, "Monica", "Female", 21)
s5 = Student(5, "Rishith", "Male", 21)
s6 = Student(6, "Srinivas", "Male", 22)
s7 = Student(7, "Durga Prasad", "Male", 22)
s8 = Student(8, "Sathvik", "Male", 21)

s1.display()
s2.display()
s3.display()
s4.display()
s5.display()
s6.display()
s7.display()
s8.display()

print(s1.age)
print(s1.name)
print(s2.gender)
print(s3.student_id)
print(s5.name, s5.student_id, s5.gender)
print(s1.age >= 18)
print(s1.age == s2.age)
print(s3.name.upper())
print(len(s4.name))
print(s6.student_id, s6.name, s6.age)