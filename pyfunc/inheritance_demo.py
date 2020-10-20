
class Person(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print self.firstName, self.lastName


class Student(Person):
    def __init__(self, firstName, lastName, year):
        super(Student, self).__init__(firstName, lastName)
        self.graduationYear = year

    def welcome(self):
        print "Welcome", self.firstName, self.lastName, "to the class of", self.graduationYear


guy = Person("John", "Doe")
guy.printName()

student = Student("Eric", "Yu", 2019)
student.welcome()
