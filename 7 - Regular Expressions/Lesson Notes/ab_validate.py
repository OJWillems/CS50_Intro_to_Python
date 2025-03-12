# re.search(pattern, string)

# re.search symbols:
# .         - any character except a new line
# *         - 0 or more repetitions
# +         - 1 or more repetitions
# ?         - 0 or 1 repetitions
# {m}       - m repetitions
# {m, n}    - m-n repetitions
# ^         - matches the start of the string
# $         - matches the end of the string or just before the new line at the end of the string

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    # NOTE the 'r' before the pattern string parameter. Specifies you want Python to interpet this as a RAW string to indicate to python that it shouldn't try to interpret any backslashes in any particular way.
    # By specifying it's a raw string in this case, you are telling Python to interpret that escaped ('\') third '.' not as a REGEX symbol, but as a literal '.'
    # GOOD PRACTICE TO USE RAW STRINGS FOR ALL YOUR REGEXES
    print("Valid")
else:
    print("Invalid")