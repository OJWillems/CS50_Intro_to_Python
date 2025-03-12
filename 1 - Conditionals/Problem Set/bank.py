# In a file called bank.py, implement a program that prompts the user for a greeting.
# If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.
# Be sure to give $0 not only for “hello” but also “hello there”, “hello, Newman”, and the like.

greeting = input("What greeting would you like to use? ").strip().casefold()

def main(input):
    # if greeting prefix == "hello" return / print $0
    if input.startswith("hello"):
        print("$0")
        return "$0"
    # elif greeting index 0 == "h" return / print $20
    elif input.startswith("h"):
        print("$20")
        return "$20"
    # else return $100
    else:
        print("$100")
        return "$100"

main(greeting)
