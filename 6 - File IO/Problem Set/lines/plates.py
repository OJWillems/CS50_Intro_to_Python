def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if length_requirement(s) and letter_start(s) and numbers_at_the_end(s) and first_number_not_zero(s) and no_periods_spaces_or_punctuation_marks(s):
        return True
    else:
        return False


# Length is 2 - 6 characters:
def length_requirement(string):
    return 2 <= len(string) <= 6 # else print("Fails length requirement.")

# Plate starts with two letters:
def letter_start(string):
    return string[0].isalpha() and string[1].isalpha() # else print("Does not start with 2 letters.")

# Numbers at the end only
def numbers_at_the_end(string):
    number_sequence_ended = False
    for character in reversed(string):
        if number_sequence_ended:
            if character.isdecimal():
                # print("Numbers can only be at the end.")
                return False
        else:
            if character.isalpha():
                number_sequence_ended = True
    return True

# First number cannot be 0
def first_number_not_zero(string):
    for character in string:
        if character.isdecimal():
            if int(character) == 0:
                # print("The first number cannot be 0.")
                return False
            else:
                return True
    return True

# No periods, spaces, or punctuation marks
def no_periods_spaces_or_punctuation_marks(string):
    for character in string:
        if character.isalnum() == False:
            # print("You cannot use periods, spaces, or punctuation marks.")
            return False
    return True

if __name__ == "__main__":
    main()