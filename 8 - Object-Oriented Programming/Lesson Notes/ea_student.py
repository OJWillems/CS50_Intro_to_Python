# CLASS AND INSTANCE METHODS

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        # You can now instantiate a student object by just using cls that's passed in.
        # Create an object of the current class, whatever cls is, which by definition is Student:
        return cls(name, house)

def main():
    student = Student.get()
    print(student)

# This should be a Class Method!
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     try:
#         return Student(name, house)
#     except ValueError:
#         ...

if __name__ == "__main__":
    main()