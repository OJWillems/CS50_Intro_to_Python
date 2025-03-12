import sys
import random
from pyfiglet import Figlet  # type: ignore

figlet = Figlet()

figlet_fonts_list = figlet.getFonts()

def main():
    if len(sys.argv) == 1:
        random_font()
    elif len(sys.argv) == 3:
        # Check that the two additional arguments to the command line input are correct:
        if (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet_fonts_list:
            specified_font()
        # Wrong two arguments: either not '-f', '--f', or not a figlet font
        else:
            sys.exit("Invalid usage")
    # Too many or too few arguments:
    else:
        sys.exit("Invalid usage")

def random_font():
    user_input = input("Input: ")
    random_font = random.choice(figlet_fonts_list)
    figlet.setFont(font=random_font)
    print(figlet.renderText(user_input))

def specified_font():
    user_input = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main()