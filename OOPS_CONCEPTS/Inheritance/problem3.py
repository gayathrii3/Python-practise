class Account:

    def __init__(self,balance,acc_no):
        self.balance = balance
        self.__acc_no = acc_no

    def show_balance(self):
        print(f"Your balance is {self.balance}")

    def credit(self, amount):  
        self.balance += amount
        print(f"RS.{amount} credited to you acc {self.acc_no}")
        print(f"Total balance : {self.balance}")

    def debit(self, amount):  
        self.balance -= amount
        print(f"RS.{amount} debited from you acc {self.acc_no}")
        print(f"Total balance : {self.balance}")



acc1 = Account(1000, '123-45-6')
# acc1.show_balance()
# acc1.debit(1000)
# acc1.show_balance()
# acc1.credit(200)
# acc1.show_balance()
print(acc1.__acc_no)       # can't access private attribute
