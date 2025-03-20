students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

print("# ---------------------------------------------------------------------------------------------- #")

# Using enumerate:

for i, student in enumerate(students):
    print(i + 1, student)