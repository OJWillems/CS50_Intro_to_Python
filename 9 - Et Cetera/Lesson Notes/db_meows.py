# TYPE HINTS and mypy

# TYPE HINT AS PARAMETER!!!
def meow(n: int):
    for _ in range(n):
        print("meow")

# TYPE HINT WHILE SETTING VARIABLE
number: int = int(input("Number: "))
meow(number)

# run mypy db_meows.py
