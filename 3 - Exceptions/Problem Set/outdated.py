# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636.
# Then output that same date in YYYY-MM-DD format. 

# If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

months_dictionary = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}

def main():
    # Begin endless loop:
    while True:
        # Get date input.
        date_input = input("Date: ")
        # Pass date input to date_checker function to check if format is either digital or analog.
        if date_checker(date_input) == "MM/DD/YYYY FORMAT":
            # Pass date input into digital_parser function.
            date_output = digital_parser(date_input)
            # If the digital parser returns a value, print it and break out of endless loop.
            if date_output is not None:
                print(date_output)
                break
        elif date_checker(date_input) == "MONTH DD, YYYY FORMAT":
            # Pass date input into analog_parser function.
            date_output = analog_parser(date_input)
            # If the analog parser returns a value, print it and break out of the endless loop
            if date_output is not None:
                print(date_output)
                break

def date_checker(input):
    if len(input.split("/")) == 3:
        return "MM/DD/YYYY FORMAT"
    if len(input.split(" ")) == 3:
        return "MONTH DD, YYYY FORMAT"

# This is where the heavy lifting for the digital format happens:
def digital_parser(input):
    # Split the string and assign values:
    month, day, year = input.split("/")
    # Strip possible leading and tailing whitespace:
    month = month.strip()
    day = day.strip()
    year = year.strip()
    # Pass month, day, and year variables through padding functions in case they aren't the right length (e.g. 1/1/2025 --> 01/01/2025)
    month = digital_month_padding(month)
    day = digital_day_padding(day)
    year = year_padding(year)
    # Final input validation step and where the transformation of the date_input to the date_output occurs, making sure that the date values are integers AND are within the bounds of normal dates
    try:
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year) <= 9999:
            return str(f"{year}-{month}-{day}")
    except:
        pass

# "MONTH DD, YYYY FORMAT"
def analog_parser(input):
    month_analog, day, year = input.split(" ")
    # Strip possible leading and tailing whitespace:
    month_analog = month_analog.strip()
    day = day.strip()
    year = year.strip()
    # Check that the month is in the dictionary of months and return its numerical value:
    month_digital = analog_month_parsing(month_analog)
    # Get rid of "," in the day string (i.e. "01,") and pad day if necessary
    day_parsed = analog_day_parsing(day)
    # Pad year if necessary
    year = year_padding(year)
    # Final input validation step and where the transformation of the date_input to the date_output occurs, making sure that the date values are integers AND are within the bounds of normal dates
    try:
        if month_digital is not None and 1 <= int(day_parsed) <= 31 and 0 <= int(year) <= 9999:
            return str(f"{year}-{month_digital}-{day_parsed}")
    except:
        pass
    

def year_padding(year_input):
    if len(year_input) == 3:
        return str(f"0{year_input}")
    elif len(year_input) == 2:
        return str(f"00{year_input}")
    elif len(year_input) == 1:
        return str(f"000{year_input}")
    else:
        return year_input

# Digital padding functions:
def digital_day_padding(day_input):
    if len(day_input) < 2:
        return str(f"0{day_input}")
    else:
        return day_input

def digital_month_padding(month_input):
    if len(month_input) < 2:
       return str(f"0{month_input}")
    else:
        return month_input
    
# Analog padding & parsing functions:
def analog_month_parsing(month_input):
    if month_input.title() in months_dictionary.keys():
        return months_dictionary[month_input.title()]
    
def analog_day_parsing(day_input):
    # Make sure there's a comma:
    if day_input.endswith(","):
        # First remove ","
        day_without_comma = day_input.replace(",", "")
        # Now pad if necessary
        if len(day_without_comma) < 2:
            return str(f"0{day_without_comma}")
        else:
            return day_without_comma

main()


# EXTRA CHALLENGE: DATE VALIDATION FOR EACH MONTH (i.e. February only has 28 days, etc.)