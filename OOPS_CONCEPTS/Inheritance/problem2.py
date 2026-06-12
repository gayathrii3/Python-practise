# Bank account(using instance method) ----> functions that belongs to class

class BankAccount():

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def show_balance(self):
        print(f"Your balance is ₹{self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter deposit amount:₹ "))

        if amount < 0:
            print("Invalid range")
        else:
            self.balance += amount
        
    def withdraw(self):
        amount = float(input("Enter the withdrawl amount:₹"))

        if amount < 0:
            print("Invalid amount")
        elif amount > self.balance:
            print(f"Insufficient funds")
        else:
            self.balance -= amount

acc = BankAccount("Gayathri", 1600)

print(f"---------{acc.account_holder}'s Bank Account--------")
acc.show_balance()
acc.deposit()
acc.show_balance()
acc.withdraw()
acc.show_balance()
