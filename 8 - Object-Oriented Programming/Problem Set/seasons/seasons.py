# Asks user for input of their birth date: YYYY-MM-DD
# Prints how old they are in minutes, rounded to nearest integer ("Five hundred twenty-five thousand, six hundred minutes")

import sys
import re
from datetime import date
import inflect
p = inflect.engine()

def main():
    date_input = input("Date of Birth: ")
    date_of_birth = user_date_input_validation(date_input)
    minute_differential = get_minute_differential(date_of_birth)
    print(f"{minute_phrase_parser(minute_differential)} minutes")

# Function asking for user input and validates that input
def user_date_input_validation(date_input):
    pattern = r"(?P<year>\d\d\d\d)-(?P<month>(0[1-9])|(1[0-2]))-(?P<day>([0-2]\d)|(3[01]))"
    if match := re.fullmatch(pattern, date_input):
        return {"year": int(match.group("year")), "month": int(match.group("month")), "day": int(match.group("day"))}
    else:
        sys.exit("Invalid date")
 
# Function parsing input as datetime object and returning the delta between today's date and the date input in minutes
def get_minute_differential(date_input):
    date_of_birth_object = date(date_input["year"], date_input["month"], date_input["day"])

    current_date_object = date.today()

    if not date_of_birth_object > current_date_object:
        date_differential = current_date_object - date_of_birth_object
        return date_differential.days * 24 * 60
    else:
        sys.exit("You can't be born in the future")

# Function translating that datetime object to words
def minute_phrase_parser(minute_differential_input):
    return p.number_to_words(minute_differential_input).replace(" and", "").capitalize()

if __name__ == "__main__":
    main()