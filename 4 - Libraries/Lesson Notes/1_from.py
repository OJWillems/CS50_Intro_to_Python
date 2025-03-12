# If you want to be more specific than 'import'ing the whole module, use 'from'

from random import choice

# NOTE you don't need to specify the choice function from the random module (i.e. random.choice(...)).
coin = choice(["heads", "tails"])

print(coin)