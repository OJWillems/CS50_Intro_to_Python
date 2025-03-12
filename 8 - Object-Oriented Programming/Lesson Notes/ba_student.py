# CLASSES

class Student:
    ...
    # You can actually leave this blank. You've created the class and any time you call it, you're creating an object of that class.

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    # By calling Student(), you're creating a student object of the Student class
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__":
    main()