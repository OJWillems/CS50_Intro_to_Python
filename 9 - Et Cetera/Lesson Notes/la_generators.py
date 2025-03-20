# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock

# if __name__ == "__main__":
#     main()

# The above will break if you try to print out a million sheep

# print("# ---------------------------------------------------------------------------------------------- #")

# YIELD

def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        # YIELD is returning an ITERATOR
        yield "🐑" * i

if __name__ == "__main__":
    main()