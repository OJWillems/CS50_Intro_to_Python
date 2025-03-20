# ARGPARSE
# Provide some context to the program when the user inputs the -h / --help CLI argument

import argparse

# Give the program a description
parser = argparse.ArgumentParser(description="Meow like a cat")
# Give a default number
# Give a description of what the n argument does when -h / --help is invoked
# Specify the type of the argument as int, so you don't have to specify it in the print statement
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

print("meow\n" * args.n, end="")