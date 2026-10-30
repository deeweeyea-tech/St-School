class Employee:
    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Salary:", self.salary)


employee1 = Employee(101, "Divya", 350000)
employee2 = Employee(102, "Rayyan", 450000)
employee3 = Employee(103, "Rita", 435000)

employee1.display_details()
print()
employee2.display_details()
print()
employee3.display_details()