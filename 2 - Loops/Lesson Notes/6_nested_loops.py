def main():
    # column 3 blocks high
    print_column(3)

    # row 4 blocks wide
    print_row(4)

    # 5 x 5 square
    print_square(5)

    # 5 x 2 rectangle
    print_rectangle(5, 2)

    

def print_column(height):
    # for _ in range(height):
    #     print("#")
    print("#\n" * height, end="")

def print_row(width):
#     for _ in range(width):
#         print("#", end="")
    print("#" * width)

def print_square(size):
    for _ in range(size):
        print("#  " * size)

def print_rectangle(height, width):
    for _ in range(height):
        print("  #" * width)

main()