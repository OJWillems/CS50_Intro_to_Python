import emoji # type: ignore

def main():
    string_input = input("Input: ")
    emojized_output = emoji.emojize(string_input, language="alias")
    print(emojized_output)

if __name__ == "__main__":
    main()