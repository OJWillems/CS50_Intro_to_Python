import sys
import csv

def main():
    cli_error_handling()
    scourgify()

def cli_error_handling():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("One or both of the files are not CSV files")

def scourgify():
    try:
        with open(sys.argv[1], "r") as input, open(sys.argv[2], "w", newline="") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(", ")
                fixed_row = {"first": first, "last": last, "house": row["house"]}
                writer.writerow(fixed_row)
    except FileNotFoundError:
        sys.exit("File not found")

if __name__ == "__main__":
    main()