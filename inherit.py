
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(self.name)
        print(self.age)


class Student(Person):
    pass


student1 = Student("Anuradha", 20)
student1.intro()
