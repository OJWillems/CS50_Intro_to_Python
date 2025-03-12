# .keys() method

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for spacecraft in distances.keys():
        print(f"{spacecraft} is {distances[spacecraft]} AU from Earth")


main()

########################################################################

# .values() method

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for distance in distances.values():
        print(f"{distance:,} AU is {convert(distance):,} meters")
    
def convert(au):
    return au * 149597870700

main()

########################################################################

distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    for spacecraft in distances:
        print(f"{spacecraft} is {distances[spacecraft]:,} Astronomical Units - {convert(distances[spacecraft]):,} meters - away")


def convert(au):
    return au * 149597870700

main()