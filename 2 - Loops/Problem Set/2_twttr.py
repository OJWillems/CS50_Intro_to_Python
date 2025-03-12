# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. 
# In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

# input string
# do a for loop that iterates over the input string
#   if letter.lowercase() in [a,e,i,o,u]
# input string.replace(letter, "")


def main():
    string = input("What would you like to say? ")
    vowels_list = ["a", "e", "i", "o", "u"]
    for character in string:
        if character.lower() in vowels_list:
            string = string.replace(character, "")
    print(string)

# def main():
#     string = input("What would you like to say? ")
#     vowels_list = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
#     for character in vowels_list:
#         string = string.replace(character, "")
#     print(string)

main()