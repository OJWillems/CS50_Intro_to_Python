import re
import sys

def main():
    hours_worked = input("Hours: ")
    print(convert(hours_worked))

def convert(input_string):
    pattern = r"(?P<first_hour>[1-9]|1[0-2])(?P<first_minutes>:[0-5][0-9])? (?P<first_meridiem>[AP]M) to (?P<second_hour>[1-9]|1[0-2])(?P<second_minutes>:[0-5][0-9])? (?P<second_meridiem>[AP]M)"
    if match := re.fullmatch(pattern, input_string):
        
        first_hour = int(match.group("first_hour"))
        if first_hour == 12:
            if match.group("first_meridiem") == "AM":
                first_hour = 0
        elif first_hour != 12 and match.group("first_meridiem") == "PM":
            first_hour += 12

        first_minutes = match.group("first_minutes")
        if first_minutes == None:
            first_minutes = ":00"


        second_hour = int(match.group("second_hour"))
        if second_hour == 12:
            if match.group("second_meridiem") == "AM":
                second_hour = 0
        if second_hour != 12 and match.group("second_meridiem") == "PM":
            second_hour += 12

        second_minutes = match.group("second_minutes")
        if second_minutes == None:
            second_minutes = ":00"

        return f"{first_hour:02}{first_minutes} to {second_hour:02}{second_minutes}"
    
    else:
        raise ValueError

if __name__ == "__main__":
    main()