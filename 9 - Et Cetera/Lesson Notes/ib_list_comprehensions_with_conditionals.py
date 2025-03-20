students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor)

print("# ---------------------------------------------------------------------------------------------- #")

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

# Filter, like map, takes in a function as an argument
gryffindors = filter(is_gryffindor, students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor["name"])

print("# ---------------------------------------------------------------------------------------------- #")

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

# Passing in a lambda function instead of creating an is_gryffindor function
gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
    print(gryffindor["name"])