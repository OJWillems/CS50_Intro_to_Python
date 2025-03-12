# CLASSES & Instance Methods - Properties, Getters and Setters

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # Getter for the house property
    @property
    # @property tells Python that this is the Getter method for the 'house' property for instances of the Student class. 
    # You MUST give the method the same name as the property whose value you're trying to access
    def house(self):
        print(f"Test Getter: {self._house}")
        return self._house
    
    # Setter for the house property
    @house.setter
    # @house.setter tells Python that this is the Setter method for the 'house' property for instances of the Student class.
    # You MUST give the method the same prefix as the name of the property whose value you're trying to initialize or alter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
        print(f"Test Setter: {self._house}")

def main():
    student = get_student()
    # student.house = "Test invalid circumnaviation of the student object initalization house conditional"
    print(student)
    student.house = "Ravenclaw"
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    try:
        return Student(name, house)
    except ValueError:
        ...

if __name__ == "__main__":
    main()