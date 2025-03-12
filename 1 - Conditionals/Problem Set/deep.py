# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything,
# outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

# No need to convert the user’s input to an int if you check for equality with "42", a str, rather than 42, an int!
# It’s okay if your output or the user’s wraps onto multiple lines.

user_input = input("What is the answer to the Great Question of Life? ").strip().casefold()

def main(input):
    # if input == "42" or input == "forty-two" or input == "forty two":
    #     print("Yes")
    # else:
    #     print("No")
    match input:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main(user_input)