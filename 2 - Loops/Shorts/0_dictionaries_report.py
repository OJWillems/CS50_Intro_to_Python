def main():
    spacecraft = {
        "name": "Voyager 1",
        "distance": 163,
    }
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]}

    ==========================
    """

main ()

########################################################################

# Adding to an initialized dictionary:

def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft["distance"] = 0.01
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU

    ==========================
    """

main()

########################################################################

# .get() method

def main():
    spacecraft = {"name": "Hive Fleet Leviathan"}
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU

    ==========================
    """

main()

########################################################################

# .update() method

def main():
    spacecraft = {
        "name": "Nostromo", 
        "distance": 15
    }
    spacecraft.update({"distance": 10, "orbit": "Mars"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}

    ==========================
    """

main()