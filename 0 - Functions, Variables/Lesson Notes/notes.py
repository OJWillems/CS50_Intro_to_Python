# command line: 'code notes.py' opens or creates the file
# command line: 'python notes.py' runs it

name = input("What's your name? ").strip().title()

# Remove whitespace from str and capitalize user's name
# name = name.strip().title()

#.capitalize() capitalizes the first letter of the whole string
# name = name.capitalize()

#.title() capitalizes the first letter of each word
# name = name.title()

# Split user's name into first and last name
first, last = name.split(" ")
# NOTE how you created two separate comma-separated variables - first and last and assigned them each side of the split

print("Hello,", name)
# print("Hello, " + name)

# when you use comma syntax (i.e. pass in multiple arguments to print) it automatically adds the " ", because the named parameter sep=" " by default has a space in it)
# there's also another named parameter, end="\n", that by default prints out a new line at the end of the print statement

print("Hello,", name, sep="???", end="fuck \n")

# Escaping characers:
print("Hello, \"friend\"")
# Prints "Hello, "friend""

# f-strings
print(f"Hello, {first}")
# NOTE the f before the string. That tells Python to treat this string in a special, formatted way, so that it can parse the {} brackets


# Interactive Mode
# You can just type 'python' in terminal to enter Interactive Mode


