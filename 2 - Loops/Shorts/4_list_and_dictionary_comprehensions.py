def main():
    # counts = {}
    words = get_words("address.txt")
    
    # List Comprehension to create a lowercase list of words:
    simple_list_comprehension_example = [word for word in words]
    # You're basically moving the body of the for loop to right before the 'for' statement

    lowercase_words = []
    for word in words:
        lowercase_words.append(word.lower())

    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # Dictionary Comprehension:

    # Regular for loop:
    # for word in words:
    #     if word in counts:
    #         counts[word] += 1
    #     else:
    #         counts[word] = 1

    # Dictionary Comprehension:
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    save_counts(counts)


main()