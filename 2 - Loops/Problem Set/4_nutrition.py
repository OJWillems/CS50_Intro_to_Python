# In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) 
# and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits. 
# Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.

# Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a dict to associate a fruit with its calories!
    # If k is a str and d is a dict, you can check whether k is a key in d with code like:
        # if k in d:
        #     ...
# Take care to output the fruit’s calories, not calories from fat!

fruits = [
    {"fruit": "apple", "calories": 130},
    {"fruit": "avocado", "calories": 50},
    {"fruit": "banana", "calories": 110},
    {"fruit": "cantaloupe", "calories": 50},
    {"fruit": "grapefruit", "calories": 60},
    {"fruit": "grapes", "calories": 90},
    {"fruit": "honeydew melon", "calories": 50},
    {"fruit": "kiwifruit", "calories": 90},
    {"fruit": "lemon", "calories": 15},
    {"fruit": "lime", "calories": 20},
    {"fruit": "nectarine", "calories": 60},
    {"fruit": "orange", "calories": 80},
    {"fruit": "peach", "calories": 60},
    {"fruit": "pear", "calories": 100},
    {"fruit": "pineapple", "calories": 50},
    {"fruit": "plum", "calories": 70},
    {"fruit": "strawberries", "calories": 50},
    {"fruit": "sweet cherries", "calories": 100},
    {"fruit": "tangerine", "calories": 50}, 
    {"fruit": "watermelon", "calories": 80}
]

fruits_and_calories = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plum": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

# print(fruits[1]["fruit"], fruits[1]["calories"], sep=", ")

def main():
    fruit_name = input("What fruit do you want caloric information for? ").lower()
    for fruit_details in fruits:
        if fruit_details["fruit"] == fruit_name:
            print(f"Calories: {fruit_details["calories"]}")

# def main():
#     fruit_name = input("What fruit do you want caloric information for? ").lower()
#     if fruit_name in fruits_and_calories:
#         print(f"Calories: {fruits_and_calories[fruit_name]}")

main()