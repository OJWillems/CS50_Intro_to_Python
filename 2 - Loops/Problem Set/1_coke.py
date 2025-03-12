# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.

def main():
    coke_amount = 50
    total_inserted = 0
    while total_inserted < coke_amount:
        amount_inserted = int(input("Please insert a coin: "))
        if amount_inserted == 25:
            total_inserted = total_inserted + amount_inserted
        elif amount_inserted == 10:
            total_inserted = total_inserted + amount_inserted
        elif amount_inserted == 5:
            total_inserted = total_inserted + amount_inserted
        else:
            print("Please insert a valid denomination")
        
        if total_inserted < coke_amount:
            print(f"Amount Due: {int(coke_amount - total_inserted)} cents")
            
    print(f"Change Owed: {total_inserted - coke_amount} cents")

main()