class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"


emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'user', 60000)

print(emp_1.email)
print(Employee.fullname(emp_2))
