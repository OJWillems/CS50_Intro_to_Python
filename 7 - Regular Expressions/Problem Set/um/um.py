import re
import sys

def main():
    user_input = input("Text ").strip()
    print(count(user_input))

def count(input_string):
    pattern = r"\bum\b"
    return len(re.findall(pattern, input_string, flags=re.IGNORECASE))

if __name__ == "__main__":
    main()