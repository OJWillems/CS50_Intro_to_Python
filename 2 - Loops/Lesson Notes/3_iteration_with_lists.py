students = ["Hermione", "Harry", "Ron"]

# Your version of iterating through the list:

length = len(students)

for _ in range(length):
    print(students[_])

# WOAH:

students = ["Seamus", "Bill", "Fred"]

for student in students:
    print(student)
    # NOTE you don't need to initalize the student variable, Python will just do it for you here.

# Using len again, this time per the instructor:

students = ["Parvati", "Cedric", "Ginny"]

for i in range(len(students)):
    print(i + 1, students[i])
