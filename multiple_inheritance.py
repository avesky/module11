"""
Program: multiple_inheritance.py
Author: Andy Volesky
Last date modified: 11/10/2021

The purpose of this program:

Write a class Manager that inherits from Person and Employee.

Add attribute department
Add list direct_reports of type Employee that report to the manager
Include a driver that
Creates a Manager object (select a meaningful name) with your name, start date today, starting salary $40,000
Displays the Manager object
Creates at least 3 direct_reports of type Employee that report to Manager
Displays the Manager object's direct_reports including Employee object name, start_date, salary%3CmxGraphModel%3E%3Croot%3E%3CmxCell%20id%3D%220%22%2F%3E%3CmxCell%20id%3D%221%22%20parent%3D%220%22%2F%3E%3CmxCell%20id%3D%222%22%20value%3D%22%22%20style%3D%22rounded%3D0%3BorthogonalLoop%3D1%3BjettySize%3Dauto%3Bhtml%3D1%3B%22%20edge%3D%221%22%20parent%3D%221%22%3E%3CmxGeometry%20relative%3D%221%22%20as%3D%22geometry%22%3E%3CmxPoint%20x%3D%22218.70370370370392%22%20y%3D%22170%22%20as%3D%22sourcePoint%22%2F%3E%3CmxPoint%20x%3D%22251.29629629629653%22%20y%3D%22250%22%20as%3D%22targetPoint%22%2F%3E%3C%2FmxGeometry%3E%3C%2FmxCell%3E%3C%2Froot%3E%3C%2FmxGraphModelee
Change salary to $42,000
Displays the Manager object
"""

class Person:
    """Person class"""
    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname


    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'+ self.student.display()

class Employee(Person):
    '''Employee Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phnum):
        super().__init__(lname, fname)
        self.address = addy
        self.phone_number = phnum

    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def display(self):
        return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n" + str(self.phone_number)


class SalariedEmployee(Employee):
    def __init__(self, lname, fname, addy, phnum, st_date, slry):
        super().__init__(lname, fname, addy, phnum)
        self.start_date = st_date
        self.salary = slry

    def give_raise(self, slry):
        self.salary = slry

    def display(self):
        return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n" + str(self.salary) + "\n" + str(self.start_date)

class Manager(SalariedEmployee):
    '''Manager Class '''
    # Constructor
    def __init__(self, lname, fname, addy, phnum, st_date, slry, dept, reports=[]):
        super().__init__(lname, fname, addy, phnum, st_date, slry)
        self.department = dept
        self.direct_reports = reports

    def __str__(self):
        return f"Employee: {self.direct_reports}"

    def create_reports(self, reports):
        self.direct_reports = reports

    def display(self):
        return str(self.first_name) + ", " + str(self.last_name) + "\n" + str(self.address) + "\n" + str(self.phone_number) + "\n" + str(self.start_date) + "\n" + str(self.salary)  + "\n" + str(self.department)  + "\n" + self.direct_reports.__str__() #I can't figure out how to get this to display as not the Employee object.

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

emp = Manager('Ruiz', 'Matthew', '156 Mulberry St.', '5159991111', '11/10/21', '$40,000 per year', 'Marketing')
print(emp.display())
print("")
Manager.create_reports(emp, [Employee('Smith', 'Dave', '123 Main', '515 225 2657'), Employee('Tate', 'Ingred', '456 2nd St', '515 225 2657'), Employee('McNab', 'Larry', '789 Blueberry Ln', '515 225 2657')])
print("")
print(emp.display())
print("")
SalariedEmployee.give_raise(emp, '$42,000')
print(emp.display())
del emp