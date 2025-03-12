# re.search(pattern, string, flags=0)
# FLAGS parameter

# re.IGNORECASE     - Ignores case of user input
# re.MULTILINE      - Ignores multiple lines in an input
# re.DOTALL         - Makes the '.' special character match any character at all, INCLUDING a newline (otherwise it wouldn't recognize '\n')

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# What if you have subdomains? i.e. ollie@willems.gmail.com
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    # You are grouping that first set of word characters followed by an escaped '.' after the the '@' and specifying that it may appear once or not at all with the '?' modifier
    print("Valid")
else:
    print("Invalid")