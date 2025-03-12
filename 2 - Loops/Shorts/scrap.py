# List Comprehension:

list = ["hello", "World", "FUCK", "ShOt GlAsS MiLk"]

# Regular way:
lowercase_list = []
for word in list:
    lowercase_list.append(word.lower())

print(lowercase_list)

# Comprehension way:
lowercase_list = [word.lower() for word in list]

print(lowercase_list)


# Dictionary Methods:

words = {"Fuck": 4, "Shit": 2}

print(words.items())