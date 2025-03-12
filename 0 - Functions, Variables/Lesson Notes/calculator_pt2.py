def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(x):
    return pow(x, 2)
    # return x ** 2
    # return x * x
    # YOU HAVE TO RETURN THE VALUE

main()