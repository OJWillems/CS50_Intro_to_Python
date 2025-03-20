# LIST COMPREHENSIONS

# From hb_map.py:
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

print("# ---------------------------------------------------------------------------------------------- #")

# Using a list comprehension:
def main():
    yell("This", "is", "CS50")

def yell(*words):
    # LIST COMPREHENSION:
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()