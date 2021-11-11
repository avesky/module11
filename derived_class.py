"""
Program: derived_class.py
Author: Andy Volesky
Last date modified: 11/10/2021

The purpose of this program:

Implement derived class Student

In the constructor
Add attribute major, default value 'Computer Science'
Add attribute gpa, default value '0.0'
Add attribute student_id, not optional

Consider all private

Override method display()

"""

class Person:
    """Person class using class Student, Class Composition"""
    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'+ self.student.display()

class Student(Person):
    """Student Class"""
    def __init__(self, stid, lname, fname, maj="Computer Science", gpa="0.0"):
        super().__init__(lname, fname)
        self.student_id = stid
        self.major = maj
        self.student_gpa = gpa

    def change_major(self, maj):
        self.major = maj

    def update_gpa(self, gpa):
        self.student_gpa = gpa

    def display(self):
        return(self.last_name +  ', ' + self.first_name +  ': ''(' + str(self.student_id) + ') ' + self.major + ' ' + 'GPA ' + str(self.student_gpa))

# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student