students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco" : "Slytherin"
}

print(students["Hermione"])

for student in students:
    print(student)
    # NOTE will iterate over the keys, not the values
    print(student, students[student], sep=", ")