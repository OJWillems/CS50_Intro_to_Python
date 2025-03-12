# In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. 
# Assume that the user’s input will indeed be in camel case.

# isupper()	Returns True if all characters in the string are upper case
# join()	Converts the elements of an iterable into a string
# lower()	Converts a string into lower case
# replace()	Returns a string where a specified value is replaced with a specified value

def main():
    camel_variable = input("What is the variable name in camelCase? ")
    for letter in camel_variable:
        if letter.isupper():
            print("HELLO")
            camel_variable = camel_variable.replace(letter, f"_{letter.lower()}")
    print(camel_variable)
    return camel_variable

main()