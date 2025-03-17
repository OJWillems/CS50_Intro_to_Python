# Alternative to global variable using OOP

class Account:
    def __init__(self):
        self._balance = 0
    
    # getter
    @property
    def balance(self):
        return self._balance
    
    # @balance.setter
    # def balance(self, balance):
    #     self._balance = balance
    
    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print(f"Balance: {account.balance}")
    # account.balance = 1000
    account.deposit(50)
    account.withdraw(25)
    print(f"Balance: {account.balance}")

if __name__ == "__main__":
    main()