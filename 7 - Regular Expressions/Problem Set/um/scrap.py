import re

string = "scum amuse chums plums umpire drums stump um, ,um, ,blum, um"

pattern = r"\bum\b"

matches = re.findall(pattern, string)

print(matches)