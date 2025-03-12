name = input("What's your name? ")

# WITH: creates a context in which something happens. NOTE the 'as file' syntax for variable assignment.
# with will automatically close() the file once its block is done running
with open("names.txt", "a") as file:
    file.write(f"{name}\n")