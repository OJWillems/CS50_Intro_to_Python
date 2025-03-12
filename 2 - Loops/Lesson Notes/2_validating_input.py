# while True:
# # NOTE: Deliberately creating an infinite loop: while True will always be True! 
# # NOTE: That's why we have to tell the loop to **continue** / **break** using conditionals within the loop
#     n = int(input("What's n? "))
#     if n < 0:
#         continue
#     else:
#         break

# BETTER:

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# # NOTE: interesting that n is accessible in the for loop since it's defined in the while loop

# BEST:

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
            # NOTE return also breaks out of a loop

def meow(n):
    for _ in range(n):
        print("meow")

main()