# SET DATATYPE

# Sets don't allow for duplicates!

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()

for student in students:
    # NOTE: It's .add() for a set, not .append() like for a list
    houses.add(student["house"])

for house in sorted(houses):
    print(house)