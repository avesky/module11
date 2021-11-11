"""
Program: class_method.override.py
Author: Andy Volesky
Last date modified: 11/10/2021

The purpose of this program:

Create two derived classes, SalariedEmployee and HourlyEmployee.

SalariedEmployee with members start_date and salary and methods give_raise() that updates salary and display() that returns a string.
Include a driver that
Creates a SalariedEmployee object (select a meaningful name) with your name, start date today, starting salary $40,000.
Displays the Employee object
Changes salary to $45,000
Displays the Employee object
HourlyEmployee has hourly_pay, start_date, method give_raise() that updates salary and display() that returns a string.
Include a driver that
Creates a HourlyEmployee object (select a meaningful name) with your name, start date today, starting hourly_pay $10.00
Displays the Employee object
Changes hourly_pay to $12.00 an hour
Displays the Employee object
"""

class Employee:
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phnum):
        self.last_name = lname
        self.first_name = fname
        self.address = addy
        self.phone_number = phnum


    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        if self.salaried == True:
            return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n"+str(self.salary) + "\n"+str(self.start_date)
        else:
            return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n"+str(self.hourly) + "\n"+str(self.start_date)

class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phnum, st_date, slry):
        super().__init__(lname, fname, addy, phnum)
        self.start_date = st_date
        self.salary = slry

    def give_raise(self, slry):
        self.salary = slry

    def display(self):
        return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n" + str(self.salary) + "\n" + str(self.start_date)

class HourlyEmployee(Employee):
    def __init__(self, lname, fname, addy, phnum, st_date, hrly):
        super().__init__(lname, fname, addy, phnum)
        self.start_date = st_date
        self.hourly = hrly

    def give_raise(self, hrly):
        self.hourly = hrly

    def display(self):
        return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n" + str(self.hourly) + "\n" + str(self.start_date)

# Driver
emp = SalariedEmployee('Ruiz', 'Matthew', '123 Main St.\nCarroll, IA 50401', '5159991111', '6-20-22', '$40,000 per year')
print(emp.display())
print('')
SalariedEmployee.give_raise(emp, '$45,000')
print(emp.display())
print('')
emp2 = HourlyEmployee('Davis', 'Karla', '4545 5th St.\nAmes, IA 51041', '5159991111', '12-25-21', '$7.25 per hour')
print(emp2.display())
print('')
HourlyEmployee.give_raise(emp2, '$12.00 per hour')
print(emp2.display())
del emp
del emp2