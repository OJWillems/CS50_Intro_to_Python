def get_guess():
    guess = round(float(input("Guess a number: ")))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct!")
    else:
        print("Incorrect!")

main()