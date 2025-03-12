import random

def main():
    level = get_level()
    i = 1
    score = 0
    while i <= 10:
        mistakes = 0
        X = generate_integer(level)
        Y = generate_integer(level)
        correct_answer = X + Y
        while mistakes < 3:
            try:
                user_answer = int(input(f"{X} + {Y} = "))
                if user_answer != correct_answer:
                    raise ValueError
            except ValueError:
                print("EEE")
                mistakes += 1
                if mistakes == 3:
                    print(correct_answer)
            else:
                score += 1
                mistakes = 0
                break
        i += 1
    print(score)

def get_level():
    while True:
        try:
            level_input = int(input("Level: "))
            if level_input <= 0:
                raise ValueError
        except ValueError:
            pass
        else:
            return level_input

def generate_integer(level):
    start = 10 ** (level - 1)
    end = 10 ** level
    if level == 1:
        return random.randrange(0, 10)
    else:
        return random.randrange(start, end)


if __name__ == "__main__":
    main()