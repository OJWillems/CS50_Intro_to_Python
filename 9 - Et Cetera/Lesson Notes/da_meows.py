# TYPE HINTS and mypy

def meow(n):
    for _ in range(n):
        print("meow")

# This fucks up because input returns a string by default
# number = input("Number: ")
number = int(input("Number: "))
meow(number)