import re

def main():
    code = input("Hexadecimal color code: ")
    pattern = r"^#?([a-f0-9]{6})$"
    match = re.search(pattern, code, re.IGNORECASE)
    if match:
        print(f"Valid. Color code is: {match.group(1)}")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()