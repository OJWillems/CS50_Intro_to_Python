import sys

def main():
    error_handling()
    try:
        with open(sys.argv[1]) as file:
            lines_list = file.readlines()
    except FileNotFoundError:
        sys.exit("File not found")
    count_lines(lines_list)

def error_handling():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

def count_lines(list_of_lines):
    lines_of_code = 0
    for line in list_of_lines:
        if not line.lstrip().startswith("#") and not line.isspace():
            lines_of_code += 1
    print(lines_of_code)

if __name__ == "__main__":
    main()