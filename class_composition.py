"""
Program: class_composition.py
Author: Andy Volesky
Last date modified: 11/10/2021

The purpose of this program:

create a class with a data member of the type of a class you defined.

Student is a Person with a major, a start date and a gpa. Use the Person class defined above.
Define a Student class with methods change_major(), update_gpa() and display() that returns a string.

Include a driver that
Creates a student object (select a meaningful name) with your name, major, start date and 4.0 gpa
Displays the student
Changes the major to 'Being Awesome!'
Updates the gpa to 3.0
Displays the student
Performs garbage collection
"""

class Person:
    """Person class using class Student, Class Composition"""
    def __init__(self, lname, fname, stdnt=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.student = stdnt

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name) + '\n'+ self.student.display()

class Student(Person):
    """Student Class"""
    def __init__(self, maj, strt_dt, gpa):
        self.major = maj
        self.start_date = strt_dt
        self.student_gpa = gpa

    def change_major(self, maj):
        self.major = maj

    def update_gpa(self, gpa):
        self.student_gpa = gpa

    def display(self):
        return(self.major + ' ' + self.start_date + ' ' + self.student_gpa)

# Driver
student = Student('Python', 'August 29', '4.0')
person1 = Person('Volesky', 'Andrew', student)
print(person1.display())

Student.change_major(student, 'Being Awesome')
Student.update_gpa(student, '3.0')

print(person1.display())

del(student)
del(person1)