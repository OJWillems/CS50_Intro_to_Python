def main():
    while True:
        input_as_fraction = input("What does your fuel gauge say? ")
        try:
            percentage_as_int = convert(input_as_fraction)
        except ValueError:
            print("You must input integers as the numerator and denominator and the numerator may not be greater than the denominator")
        except ZeroDivisionError:
            print("You cannot divide by 0")
        else:
            print(gauge(percentage_as_int))
            break

def convert(fraction):
    numerator, denominator = fraction.split("/")
    numerator = int(numerator)
    denominator = int(denominator)
    if numerator > denominator and denominator != 0:
        raise ValueError
    else:
        return int(round((numerator / denominator) * 100))

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
