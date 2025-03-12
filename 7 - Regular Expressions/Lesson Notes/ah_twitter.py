# re.sub(pattern, replacement, string, count=0, flags=0)

import re

url = input("URL: ").strip()

# Using .replace(string, replacement)
username = url.replace("https://twitter.com/", "")
print(f"Username url.replace: {username}")

# Using .removeprefix(string)
username = url.removeprefix("https://twitter.com/")
print(f"Username url.removeprefix: {username}")

# Using re.sub(...)
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username re.sub(...): {username}")

# Using re.search(...) and re.sub(...)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)", url, re.IGNORECASE):
    print(f"Username re.match(...): {matches.group(1)}")
else:
    print("Nope")