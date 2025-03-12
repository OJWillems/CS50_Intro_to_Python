# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def main():
    groceries = {}
    while True:
        try:
            item = input().upper()
            if item not in groceries.keys():
                groceries[item] = 1
            else:
                groceries[item] += 1
        except EOFError:
            print_groceries(groceries)
            break

def print_groceries(dictionary):
    sorted_dictionary = dict(sorted(dictionary.items()))
    for key, value in sorted_dictionary.items():
        print(value, key)

main()