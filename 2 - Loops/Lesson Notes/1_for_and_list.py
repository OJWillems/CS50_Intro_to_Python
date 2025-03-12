# NOTE in a for loop, i is automatically set to 0 and automatically increments it

for i in [0, 1, 2]:
    print("meow")

# BETTER:

for i in range(3):
    print("bark")

# BEST:

for _ in range(3):
    print("moo")

# COOL-ISH ALTERNATIVE:

print("oink\n" * 3, end="")