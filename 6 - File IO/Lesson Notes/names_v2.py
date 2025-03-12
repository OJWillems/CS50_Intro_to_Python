name = input("What's your name? ")

# OPEN
# First argument is the name of the file you want to store these names in
# Second argument - "w" - signifies you want to write to this file or if it doesn't exist yet, it will create the file

# file = open("names.txt", "w")
# PROBLEM: each time you run open("names.txt", "w") it's going to overwrite the previous name you've typed.

# SOLUTION: "a"
file = open("names.txt", "a")
# PROBLEM: it's appending the names without spaces or lines between them.

# Solution: manually adding \n to the write function
file.write(f"{name}\n")

file.close()
