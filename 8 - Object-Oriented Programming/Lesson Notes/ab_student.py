# TUPLES
# Tuples are similar to lists, but they are IMMUTABLE (they cannot in any way be changed)

def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student()
    # Tuples are immutable:
    # if student[0] == "Padma":
    #     student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)
    # return [name, house] if you want a list

if __name__ == "__main__":
    main()