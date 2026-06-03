# Using dunder variable(__name__)

def show_balance(balance):
    print(f"Your balance is ₹{balance:.2f}")

def deposit():
    amount = float(input("Enter deposit amount : "))

    if amount < 0:
        print("Not a valid amount")
        return 0
    else:
        return amount
    
def withdraw(balance):
    amount = float(input("Enter the withdrawl amount :"))

    if amount < 0:
        print("Invalid amount")
        return 0
    elif amount > balance:
        print("Insufficient funds")
    else:
        return amount
    

def main():

    balance = 0
    is_running = True

    while is_running:
        print("-------------BANKING PROGRAM------------")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
            
        select = input("Enter your choice(1-4): ")

        if select == '1':
            show_balance(balance)
        elif select == '2':
            balance += deposit()
        elif select == '3':
            balance -= withdraw(balance)
        elif select == '4':
            is_running = False
        else:
            print("Invalid choice")

    print("Thankyou! have a nice day!")

if __name__ == '__main__':  # can be imported or used as a standalone program

    main()

