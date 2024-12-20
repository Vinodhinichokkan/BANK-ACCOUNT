class BalanceException(Exception) :
    pass

class BankAccount:
    
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
                f"\n Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
    def withdraw(self, amount):
        try:
            self.viable_transaction (amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete.")
            self.get_balance()
        except BalanceException as error:
            print(f'\n Withdraw interrupted: {error}')
    def transfer(self,amount,account):
        try:
            print('\n*************\n\nBeginning Transfer..')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)

        except  BalanceException as error:
            print(f'\n Transfer interrupted. {error}')

class InterestRewardsAcct(BankAccount):
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print("/n Deposit complete.")
        self.get_balance()

class SavingsAct(InterestRewardsAcct):
    def __init__(self, initial_amount,acct_name):
        super().__init__(initial_amount,acct_name)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\n Withdraw completed.")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')



    




        
