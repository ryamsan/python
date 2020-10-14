class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):  # Dunder init !!
        self.first = first
        self.last = last
        self.email = f'{first}.{last}@company.com'
        self.pay = pay

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(len('test'))
print('test'.__len__())

print(len(emp_1))

# print(emp_1 + emp_2)

# print(emp_1)
# print(repr(emp_1))
# print(str(emp_1))

# print(emp_1.__repr__())
# print(emp_1.__str__())

# print(1+2)
# print('a' + 'b')
# print(int.__add__(1, 2))
# print(str.__add__('a', 'b'))