# Implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
# and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    ratio_as_float = get_fraction()
    while True:
        if ratio_as_float > 1:
            print("Numerator cannot be larger than denominator")
            ratio_as_float = get_fraction()
        elif ratio_as_float >= 0.99:
            print("F")
            break
        elif ratio_as_float <= 0.01:
            print("E")
            break
        else:
            print(f"{ratio_as_float:.0%}")
            break


def get_fraction():
    while True:
        try:
            fraction = input("What does your fuel gauge say? ")
            numerator, denominator = fraction.split("/")
            numerator = int(numerator)
            denominator = int(denominator)
            ratio = float(numerator / denominator)
        except ValueError:
            print("You must input integers as the numerator and denominator")
        except ZeroDivisionError:
            print("You cannot divide by 0")
        else:
            return ratio

main()