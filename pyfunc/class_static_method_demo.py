# Python program to demonstrate
# use of class method and static method.
#
# We generally use class method to create factory methods.
# Factory methods return class object (similar to a constructor) for different use cases.
# We generally use static methods to create utility functions.

from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18


person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print date.today().year
print "**************"
print person1.age
print person2.age
print person2.name
print "**************"
print Person.isAdult(22)
