# Regex groups, return values, .groups(), .group(n), and Walrus Operators

# .         - any character except a new line
# +         - 1 or more repetitions

# (...)     - a group
# (?:...)    - non-capturing version

import re

name = input("What is your name? ").strip()

# Grouping with parentheses in a regex RETURNS what's in the parentheses! If you just want to group, use the (?:...) non-capturing syntax
# If you're trying to capture first and last name where it's formatted as "Willems, Olivier", group the '.+' used to signify the characters for those in parentheses
matches = re.search(r"^(.+), (.+)$", name)

# 
if matches:
    last, first = matches.groups()
    name = f"{first} {last}"

print(f"Hello, {name}")


# Expounded:

matches = re.search(r"^(.+), (.+)$", name)

if matches:
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"Hello, {name}")


# WALRUS OPERATOR:

if matches:= re.search(r"^(.+), (.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"

print(f"Hello, {name}")