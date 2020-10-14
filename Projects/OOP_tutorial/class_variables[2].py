class Employee:

    num_of_emps = 0
    raise_amount = 1.04  # Class variables assessible to all instances

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'user', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)


# print(emp_1.__dict__)
# print(Employee.__dict__) # Shows raise amount now


Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)


# emp_1.raise_amount = 1.05
# print(emp_1.__dict__) # A new raise amount attribute is added to emp_1!!!
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(Employee.num_of_emps)
# emp_1 = Employee('corey', 'schafer', 50000)
# emp_2 = Employee('test', 'user', 60000)
# print(Employee.num_of_emps)