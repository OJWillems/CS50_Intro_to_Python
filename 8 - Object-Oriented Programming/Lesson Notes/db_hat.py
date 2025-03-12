# CLASS METHODS

import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    # NOTE: Instead of passing in 'self' as a parameter, the convention for Class Methods is to pass in 'cls'
    def sort(cls, name):
        print(f"{name} is in {random.choice(cls.houses)}")
        # the 'cls' here lets Python reference the Hat Class Variable 'houses'

Hat.sort("Harry")