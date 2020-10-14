class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first.title()} {self.last.title()}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):  # cls for class variable while self for instance variable
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod  # Does not require instance/class variables but is still related to the logic of the class
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


'''
emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'user', 60000)

Employee.set_raise_amt(1.05)  # Same as Employee.raise_amt = 1.05
# emp_1.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)  # Using class methods as alternative constructors

print(new_emp_1.email)
print(new_emp_1.pay)
'''

emp_1 = Employee('corey', 'schafer', 50000)
emp_2 = Employee('test', 'user', 60000)

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_work_day(my_date))
my_date = datetime.date(2016, 7, 11)
print(Employee.is_work_day(my_date))
