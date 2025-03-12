# Program that takes an INPUT of 24-hour time (#:## or ##:##) and outputs:
    # "breakfast time" - 7:00 to 8:00 - inclusive
    # "lunch time" - 12:00 to 13:00 - inclusive
    # "dinner time" - 18:00 to 19:00 - inclusive
# convert will take the string of time and convert it to a float - i.e. 7:30 --> 7.5

#####################

# def main():
#     time_input = input("What time is it? ")
#     converted_time = convert(time_input)
#     meal_determiner(converted_time)

# def convert(time_string):
#     hour, minute = time_string.split(":")
#     minute_as_float = int(minute) / 60
#     converted_time = int(hour) + minute_as_float
#     return converted_time

# def meal_determiner(converted_time):
#     if 7 <= converted_time <= 8:
#         print("breakfast time")
#     elif 12 <= converted_time <= 13:
#         print("lunch time")
#     elif 18 <= converted_time <= 19:
#         print("dinner time")

# if __name__ == "__main__":
#     main()

#####################

# Challenge #1 - Add support for 12-hour times, allowing the user to input times in these formats too: #:## am, ##:## am, #:## pm, or ##:## pm

# def main():
#     time_input = input("What time is it? ")
#     converted_time = convert(time_input)
#     meal_determiner(converted_time)

# def convert(time_string):
#     if time_string.endswith(("am", "pm")):
#         time, time_period = time_string.split(" ")
#         hour, minute = time.split(":")
#         minute_as_float = int(minute) / 60
#         if time_period == "pm" and hour != "12":
#             hour = int(hour) + 12
#         converted_time = int(hour) + minute_as_float
#         return converted_time
#     else:
#         hour, minute = time_string.split(":")
#         minute_as_float = int(minute) / 60
#         converted_time = int(hour) + minute_as_float
#         return converted_time

# def meal_determiner(converted_time):
#     if 7 <= converted_time <= 8:
#         print("breakfast time")
#     elif 12 <= converted_time <= 13:
#         print("lunch time")
#     elif 18 <= converted_time <= 19:
#         print("dinner time")

# if __name__ == "__main__":
#     main()

#####################

# Challenge #2 - Can you figure out how to use the datetime module to do this?

from datetime import datetime
import datetime

time_string_input = input("What time is it? ")

time_string = None
time_format = "%H:%M"

if time_string_input.endswith(("am", "pm")):
    time_string, time_period = time_string_input.split(" ")
    hour, minute = time_string.split(":")
    if time_period == "pm" and hour != "12":
        hour = int(hour) + 12
    time_string = str(hour) + ":" + str(minute)
else:
    time_string = time_string_input

time_object = datetime.datetime.strptime(time_string, time_format).time()

if datetime.time(7, 00, 00) <= time_object <= datetime.time(8, 00, 00):
    print("breakfast time")
elif datetime.time(12, 00, 00) <= time_object <= datetime.time(13, 00, 00):
    print("lunch time")
elif datetime.time(18, 00, 00) <= time_object <= datetime.time(19, 00, 00):
    print("dinner time")
