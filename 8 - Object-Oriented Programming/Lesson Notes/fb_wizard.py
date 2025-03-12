# INHERITANCE

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

# With the following syntax, you're specifying that Sutdent is a subclass of Wizard, the superclass
class Student(Wizard):
    def __init__(self, name, house):
        # to initialize the Student name, you're calling on the Wizard superclass' __init__ function and passing in the student's name
        super().__init__(name)
        self.house = house
    ...

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")