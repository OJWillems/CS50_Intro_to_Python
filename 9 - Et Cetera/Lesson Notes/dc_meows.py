# TYPE HINTS and mypy

# HINTING WHAT THE RETURN VALUE OF THE FUNCTION SHOULD BE WITH ->
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)

# run mypy dc_meows.py

# mypy will now detect that the meow function doesn't return anything, as it's stupidly designed to do,
# and calls you out for creating a variable - meows - that needs it to return something
