def main():
    string = input("What would you like to say? ")
    shortened_string = shorten(string)
    print(shortened_string)

def shorten(word):
    vowels_list = ["a", "e", "i", "o", "u"]
    for character in word:
        if character.lower() in vowels_list:
            word = word.replace(character, "")
    return word

if __name__ == "__main__":
    main()
