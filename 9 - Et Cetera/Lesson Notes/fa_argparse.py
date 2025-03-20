# ARGPARSE

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    # NOTE: '-n' is a flag you're dictating for your Command-Line Argument that in this case is to specify the number of meows
    n = int(sys.argv[2])
    print("meow\n" * n, end="")
else:
    print("usage: meows.py")

# All this gets really complicated and painful as you add flags and parameters to your CLI arguments. Introducing: argparse!