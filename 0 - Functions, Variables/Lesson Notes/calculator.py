# Ints
x = int(input("What's x? "))
y = int(input("What's y? "))
# NOTE you need to specify that these are going to be integers, because even though you can input integers, Python will interpret these as strings and concatenate

print(x + y)


# Floats
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

print(round(x + y, 2))
# NOTE round(number to round, number of digits to round to)

z = x + y

print(f"{z:,}")
# format string yaaay! the :, makes it comma syntax (i.e. 1 + 999 = 1,000)