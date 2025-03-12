# re.search(pattern, string)
# More regex symbols

# re.search symbols:
# .         - any character except a new line
# *         - 0 or more repetitions
# +         - 1 or more repetitions
# ?         - 0 or 1 repetitions
# {m}       - m repetitions
# {m, n}    - m-n repetitions
# ^         - matches the start of the string
# $         - matches the end of the string or just before the new line at the end of the string

# []        - set of characters
# [^]       - complementing the set (i.e. anything BUT what's after the carrot in this list)

# \d        - decimal digit
# \D        - not a decimal digit
# \s        - whitespace characters
# \S        - not a whitespace character
# \w        - word character (as well as numbers and underscores)
# \W        - not a word character (or number or underscore)

# A|B       - either A or B
# (...)     - a group
# (?:...)    - non-capturing version

import re

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")

# Alternatively:
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-z0-9+]+\.edu$", email):
    # Regexes are cool with ranges like a through z, A through Z, 0 through 9, and also an underscore for good measure
    print("Valid")
else:
    print("Invalid")

# Alternatively:
if re.search(r"^\w+@\w+\.edu$", email):
    # \w represents a word character, commonly known as an alphanumeric symbol or an underscore
    print("Valid")
else:
    print("Invalid")

# Alternatively:
if re.search(r"^\w+@\w+\.(edu|com|gov)$", email):
    # you can group characters in parentheses and use '|' to dictate one or the other
    print("Valid")
else:
    print("Invalid")