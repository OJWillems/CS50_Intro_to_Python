# UNPACKING

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(f"{total(coins[0], coins[1], coins[2]):,} Knuts")

# OR YOU CAN UNPACK THE LIST DOING THIS: *coins
print(f"{total(*coins):,} Knuts")
