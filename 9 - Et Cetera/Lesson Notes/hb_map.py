# MAP

# Without using map from ha_map.py:
def main():
    yell("This", "is", "CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

print("# ---------------------------------------------------------------------------------------------- #")

# Using map:
def main():
    yell("This", "is", "CS50")

def yell(*words):
    # map takes two arguments: the name of a function you want to map onto a sequence of values
    uppercased = map(str.upper, words)
    # NOTE: you're not calling upper here, hence why you're not adding the () to str.upper, map does that itself for each value
    print(*uppercased)

if __name__ == "__main__":
    main()