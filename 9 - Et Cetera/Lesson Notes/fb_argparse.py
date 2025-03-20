# ARGPARSE

import argparse

# Create a new instance of an argument parser
parser = argparse.ArgumentParser()
# To that instance, add the -n argument
parser.add_argument("-n")
# Now create a variable that automatically parses the arguments in your CLI using the parse_args() method
# and automatically calls sys (so you don't need to import sys)
args = parser.parse_args()

print("meow\n" * int(args.n), end="")