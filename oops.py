from bank_accounts import *

Vinodhini = BalanceException(1000, "Vinodhini")
Abirami = BalanceException(2000, "Abirami")

Vinodhini.get_balance()
Abirami.get_balance()

Vinodhini.deposit(500)
Abirami.deposit(2)

Vinodhini.withdraw(100)
Vinodhini.transfer(200,Abirami)

Mani = InterestRewardsAcct(100, "Mani")
Mani.get_balance()
Mani.deposit(100)

Kani = SavingsAct(1000, "kani")
Kani.get_balance()
Kani.withdraw(100)
Kani.transfer(5, Vinodhini)