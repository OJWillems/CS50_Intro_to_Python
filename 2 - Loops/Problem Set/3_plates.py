# In Massachusetts, it’s possible to request a vanity license platee. Among the requirements, are:

    # - “All vanity plates must start with at least two letters.”
    # - “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    # - “Numbers cannot be used in the middle of a plate; they must come at the end. 
    #       For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
    # - The first number used cannot be a ‘0’.”
    # - “No periods, spaces, or punctuation marks are allowed.”
# 
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. 
# Assume that any letters in the user’s input will be uppercase. 
# Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. 
# Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
    

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(string):
    if length_requirement(string) and letter_start(string) and numbers_at_the_end(string) and first_number_not_zero(string) and no_periods_spaces_or_punctuation_marks(string):
        return True
    else:
        return False

# ### TESTING ###
# def is_valid(string):
#     if length_requirement(string):
#         if letter_start(string):
#             if numbers_at_the_end(string):
#                 if first_number_not_zero(string):
#                     if no_periods_spaces_or_punctuation_marks(string):
#                         print("Huzzah!")
#                     else:
#                         print("Fails no periods spaces or punctuation marks")
#                 else:
#                     print("Fails first number not zero")
#             else:
#                 print("Fails numbers at the end.")
#         else:
#             print("Fails letter start.")
#     else:
#         print("Fails length requirement.")

# Length is 2 - 6 characters:
def length_requirement(string):
    return True if 2 <= len(string) <= 6 else print("Fails length requirement.")
    
# Plate starts with two letters:
def letter_start(string):
    return True if string[0].isalpha() and string[1].isalpha() else print("Does not start with 2 letters.")

# Numbers at the end only
def numbers_at_the_end(string):
    number_sequence_ended = False
    for character in reversed(string):
        if number_sequence_ended:
            if character.isdecimal():
                print("Numbers can only be at the end.")
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
            print("You cannot use periods, spaces, or punctuation marks.")
            return False
    return True

main()

# is_valid("CS50")