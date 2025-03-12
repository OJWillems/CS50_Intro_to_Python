import sys
import csv
from tabulate import tabulate

def main():
    cli_error_handling()
    tabulate_csv()

def cli_error_handling():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

def tabulate_csv():
    try:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()