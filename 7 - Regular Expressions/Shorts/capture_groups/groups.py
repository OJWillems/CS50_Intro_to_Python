import re

locations = {"+1": "United States and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():
    pattern = r"(?P<phone_number>(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4})"
    number = input("Number: ")
    
    if match := re.search(pattern, number):
        print(f"Valid. Phone number: {match.group("phone_number")}. Country code: {match.group("country_code")}. Location: {locations[match.group("country_code")]}")
    else:
        print("Invalid")
    

if __name__ == "__main__":
    main()