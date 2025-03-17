students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

print(students[0]["name"])

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")