# In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input,
# replacing each space with ... (i.e., three periods).

def main():
    user_input = input("Say what you want to say: ").replace(" ", "...", -1)
    print(user_input)
    return user_input

main()