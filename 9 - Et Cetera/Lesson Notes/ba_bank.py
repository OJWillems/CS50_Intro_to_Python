# GLOBAL VARIABLES

# Without the 'global balance' variable declaration within the deposit and withdraw functions

# Balance is established as a global variable here:
balance = 0

def main():
    # Global variables can be read within local environments
    print(f"Balance: {balance}")
    deposit(100)
    withdraw(50)
    print(f"Balance: {balance}")

def deposit(n):
    # If you want to write to the global balance variable, you need to declare it as a global variable within the local environments (i.e. functions) that will be editing it
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()