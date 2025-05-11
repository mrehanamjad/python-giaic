# This assignment is asking you to create a class called Person with a constructor that sets the name
# of the person. Then, you are instructed to create a subclass called Teacher that inherits from the
# Person class. In the Teacher class, you need to add a field for the subject that the teacher
# teaches.


class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Bilal", "Math")
print(t.name, t.subject)


