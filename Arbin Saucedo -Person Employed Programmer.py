class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, computer):
        super(Employee, self).__init__(name, age)
        self.skills = computer

    def coding(self):
        print("You typed code to make something")


class Programmer(Employee):
    def __init__(self, name, age, computer, make_code):
        super(Programmer, self).__init__(name, age, computer)
        self.job = make_code

    def makeprogram(self):
        print("You have made a program to help your job")
