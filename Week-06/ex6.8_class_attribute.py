class Employee:
    company = 'DataPulse Analytics'

    def __init__(self, name, department, salary):
        self.name = name,
        self.department = department, 
        self.salary = salary

    def display_info(self):
        print(f"Company: {Employee.company}")
        print(f"Employee Name: {self.name}")
        print(f"Deparment: {self.department}")
        print(f"Salary: ${self.salary:.2f}")
        print("--------------------")

    def annual_bonus(self):
        bonus = self.salary * 0.10
        print(f"Bonus: ${bonus:.2f}")
        print("--------------------")

print("--- ENTER EMPLOYEE 1 ---")
name1 = input("Enter employee name: ")
department1 = input("Enter employee department: ")
salary1 = float(input("Enter employee salary: $"))

print("|\n --- ENTER EMPLOYEE 2 ---")
name2 = input("Enter employee name: ")
department2 = input("Enter employee department: ")
salary2 = float(input("Enter employee salary: $"))

employee1 = Employee(name1, department1, salary1)
employee2 = Employee(name2, department2, salary2)

employee1.display_info()
employee1.annual_bonus()

employee2.display_info()
employee2.annual_bonus()