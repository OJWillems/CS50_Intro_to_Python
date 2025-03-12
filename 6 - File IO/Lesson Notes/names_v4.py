# OK:
with open("names.txt", "r") as file:
    lines = file.readlines()
    print(lines)

for line in lines:
    print("hello,", line.rstrip())

# Better:
with open("names.txt", "r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}.")