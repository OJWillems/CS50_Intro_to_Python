# re.match(pattern, string, flags=0)
# re.fullmatch(pattern, string, flags=0)

import re

email = input("What's your email? ")

# re.match(...)
# similar to re.search(...) except you don't have to specify the '^' at the beginning to indicate you want it to start the search at the beginning of the string
if re.match(r"(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# re.fullmatch(...)
# similar to re.search(...) and re.match(...) but now you don't need the '$' at the end either
if re.fullmatch(r"(\w|\.)+@(\w+\.)?\w+\.(edu|com|gov)", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")