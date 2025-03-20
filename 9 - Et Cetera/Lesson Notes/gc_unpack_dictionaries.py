# UNPACKING

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(f"{total(galleons=100, sickles=50, knuts=25):,} Knuts")

# How about using a dictionary?
coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(f"{total(coins["galleons"], coins["sickles"], coins["knuts"]):,} Knuts")

# OR YOU CAN UNPACK THE DICTIONARY LIKE THIS: **coins
print(f"{total(**coins):,} Knuts")
# This is basically passing in the keys and their values, separated by equals signs, like you started with at the top of this file