results = ["Mario", "Luigi"]

# Add to a list using the append method:
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")

# How to append multiple racers?

# This will literally append this second list as a single element to the results list, not what we're looking to do.
results.append(["Bowser", "Donkey Kong Jr."])
results.remove(["Bowser", "Donkey Kong Jr."])

# You could use the append method nested within a for loop, still not very elegant:
for racer in ["Bowser", "Donkey Kong Jr."]:
    results.append(racer)
results.remove("Bowser")
results.remove("Donkey Kong Jr.")

# Use the extend method:
results.extend(["Bowser", "Donkey Kong Jr."])

# Let's check out the insert method:
results.remove("Bowser")
results.insert(0, "Bowser")

# Let's reverse:
results.reverse()

print(results)