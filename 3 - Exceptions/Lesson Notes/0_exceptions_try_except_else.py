# # Syntax Error:
# print("hello, world)
      
# # Runtime Error:
# x = int(input("What's x? "))
# print(f"x is {x}")
# # Say the user inputs 'cat' into an int()

# try & except & else:
def main():
    x = get_int()
    print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             y = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return y
#     # NOTE: The 'else' clause is associated with the 'try' not with the 'except'

# Better:
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()