class BalanceException(Exception) :
    pass
    def __init__(self, initial_amount,acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(
            f"\nAccount '{self.name}'created.\n Balance = ${self.balance}"
        )
    

    def get_balance(self):
        print(f"\n account '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit complete.") 
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >=amount:
            return
        else:
            raise BalanceException(
                f"\n Sorry,account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
        except:





    
