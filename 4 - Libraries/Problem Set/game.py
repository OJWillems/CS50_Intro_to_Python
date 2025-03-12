import random
import sys

def main():
    level = set_level()
    number = random.randint(1, level)
    guesses(number)
    
def set_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError or level <= 0:
            pass
        else:
            if level > 0:
                return level

def guesses(number_input):
    # print(number_input)
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess == number_input:
                sys.exit("Just right!")
            elif guess < number_input:
                print("Too small!")
            else:
                print("Too large!")

if __name__ == "__main__":
    main()