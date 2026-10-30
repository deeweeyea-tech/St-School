class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")


s1 = Student("Anil", 101, 89)
s2 = Student("Divya", 102, 99)
s1.display_details()
print()
s2.display_details()