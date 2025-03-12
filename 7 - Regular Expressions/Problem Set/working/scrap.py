import re

string = "scum amuse chums plums drums stump"

pattern = r"um"

matches = re.findall(pattern, string)