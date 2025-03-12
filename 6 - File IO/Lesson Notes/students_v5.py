import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students_v4.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])